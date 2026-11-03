"""ตรวจว่ามี secret หรือข้อมูลส่วนตัวหลุดเข้าไปใน commit หรือไม่ ก่อน commit หรือก่อน push

repo นี้เป็น Public ใช้ตรวจแทนการ grep เองทุกรอบ รายละเอียดอยู่ใน scripts/check_secrets.md

โหมด (เลือกอย่างเดียว ถ้าไม่ระบุ = --commit):
  --commit     ไฟล์ที่ `git add -A` จะเพิ่มเข้า commit ถัดไป (แก้ไข ใหม่ และที่ stage ไว้) · ใช้ก่อน commit
  --unpushed   บรรทัดที่เพิ่มในทุก commit ที่ยังไม่ถูก push (origin/main..HEAD) · ใช้ก่อน push
  --history    บรรทัดที่เพิ่มในทุก commit ของทุก branch · ใช้ตรวจย้อนหลังทั้ง repo
  --all-files  ทุกไฟล์ที่ track อยู่ตอนนี้

ผลลัพธ์: FAIL = เจอสิ่งที่ห้ามขึ้น (exit 1) · WARN = ควรดูด้วยตา ไม่บล็อก (exit 0)
สคริปต์ไม่พิมพ์ค่าที่เจอเต็ม ๆ (ปิดบังส่วนท้าย) เพื่อไม่ให้ secret ไปโผล่ในจอหรือ log
"""
import argparse
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# เนื้อหา: (ชื่อ, regex, ระดับ)
CONTENT_RULES = [
    ("คีย์ OpenAI/Anthropic (sk-...)", re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}"), "FAIL"),
    ("GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"), "FAIL"),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "FAIL"),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{30,}"), "FAIL"),
    ("Slack token", re.compile(r"\bxox[abpr]-[A-Za-z0-9\-]{10,}"), "FAIL"),
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "FAIL"),
    ("กำหนดค่า key/secret/password", re.compile(
        r"(?i)\b(?:api[_-]?key|secret|token|passwd|password)\b\s*[:=]\s*['\"]?[A-Za-z0-9/+_\-]{12,}"), "FAIL"),
    ("อีเมล", re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)+"), "FAIL"),
    ("เลข 13 หลัก (อาจเป็นเลขบัตรประชาชน)", re.compile(r"(?<![\dA-Za-z.,])\d{13}(?![\dA-Za-z.,])"), "WARN"),
]

# อีเมลที่อนุญาตให้มีได้ (ไม่ใช่ข้อมูลส่วนตัว)
EMAIL_ALLOW = re.compile(r"(?i)@(?:example\.(?:com|org)|users\.noreply\.github\.com)$|^noreply@")

# ชื่อไฟล์ที่ห้ามขึ้น (เทียบกับชื่อไฟล์และพาธ)
FORBIDDEN_NAMES = [
    ".env", ".env.*", "*.pem", "*.key", "*.p12", "*.pfx", "credentials*", "secrets*", "*token*",
    "*SETSMART*", "setsmart/*", "data/private/*", "private/*", "data/raw/*",
]
LARGE_FILE_BYTES = 5 * 1024 * 1024


def git(*args):
    out = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, encoding="utf-8", errors="replace")
    if out.returncode != 0:
        sys.exit(f"git {' '.join(args)} ล้มเหลว: {out.stderr.strip()}")
    return out.stdout


def mask(s):
    s = s.strip()
    return s[:4] + "*" * min(len(s) - 4, 8) if len(s) > 4 else "****"


def scan_line(path, lineno, text, findings):
    for name, rx, level in CONTENT_RULES:
        for m in rx.finditer(text):
            val = m.group(0)
            if name == "อีเมล" and EMAIL_ALLOW.search(val):
                continue
            findings.append((level, f"{path}:{lineno}", f"{name} → {mask(val)}"))


def check_name(path, findings, size=None):
    p = path.replace("\\", "/")
    base = p.rsplit("/", 1)[-1]
    for pat in FORBIDDEN_NAMES:
        if fnmatch.fnmatch(base, pat) or fnmatch.fnmatch(p, pat):
            findings.append(("FAIL", p, f"ชื่อไฟล์ที่ห้ามขึ้น (ตรงกับ {pat})"))
            break
    if size and size > LARGE_FILE_BYTES:
        findings.append(("WARN", p, f"ไฟล์ใหญ่ {size // 1024 // 1024} MB ลองดูว่าเป็นเอกสารต้นฉบับหรือข้อมูลที่ซื้อมาหรือไม่"))


def scan_files(paths, findings):
    for rel in paths:
        f = ROOT / rel
        if not f.is_file():
            continue
        check_name(rel, findings, f.stat().st_size)
        raw = f.read_bytes()
        if b"\0" in raw[:4096]:  # ไฟล์ไบนารี ข้ามเนื้อหา
            continue
        for i, line in enumerate(raw.decode("utf-8", "replace").splitlines(), 1):
            scan_line(rel, i, line, findings)


def scan_patch(log_args, findings):
    """อ่านเฉพาะบรรทัดที่ 'เพิ่ม' ใน commit ถ้าลบข้อความออกในภายหลัง ประวัติยังเก็บของเดิม จึงต้องดูทุก commit"""
    patch = git("log", "-p", "-U0", "--no-color", "--format=commit %h", *log_args)
    commit, path, lineno = "", "", 0
    for line in patch.splitlines():
        if line.startswith("commit "):
            commit = line.split()[1]
        elif line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else line[4:]
            if path != "/dev/null":
                check_name(path, findings)
        elif line.startswith("@@"):
            m = re.search(r"\+(\d+)", line)
            lineno = int(m.group(1)) if m else 0
        elif line.startswith("+") and not line.startswith("+++"):
            scan_line(f"{commit}:{path}", lineno, line[1:], findings)
            lineno += 1


def commit_candidates():
    """ไฟล์ที่ `git add -A` จะเพิ่ม: แก้ไข + ใหม่ที่ไม่ถูก ignore + ที่ stage ไว้ (ไม่รวมไฟล์ที่ลบ)"""
    names = set(git("diff", "--name-only", "--diff-filter=d").splitlines())
    names |= set(git("diff", "--cached", "--name-only", "--diff-filter=d").splitlines())
    names |= set(git("ls-files", "--others", "--exclude-standard").splitlines())
    return sorted(n for n in names if n)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--commit", action="store_true")
    g.add_argument("--unpushed", action="store_true")
    g.add_argument("--history", action="store_true")
    g.add_argument("--all-files", action="store_true")
    a = ap.parse_args()

    findings = []
    if a.unpushed:
        upstream = git("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}").strip()
        mode = f"commit ที่ยังไม่ push ({upstream}..HEAD)"
        scan_patch([f"{upstream}..HEAD"], findings)
    elif a.history:
        mode = "ทุก commit ของทุก branch"
        scan_patch(["--all"], findings)
    elif a.all_files:
        mode = "ทุกไฟล์ที่ track"
        scan_files(git("ls-files").splitlines(), findings)
    else:
        mode = "ไฟล์ที่จะเข้า commit ถัดไป"
        files = commit_candidates()
        mode += f" ({len(files)} ไฟล์)"
        scan_files(files, findings)

    fails = [f for f in findings if f[0] == "FAIL"]
    warns = [f for f in findings if f[0] == "WARN"]
    print(f"ตรวจ: {mode}")
    for level, where, what in fails + warns:
        print(f"  {level}  {where}  {what}")
    print(f"สรุป: FAIL {len(fails)} · WARN {len(warns)}")
    if fails:
        print("หยุด: ห้าม commit/push จนกว่าจะแก้ ดูวิธีแก้ใน scripts/check_secrets.md")
    else:
        print("ผ่าน (ยังตรวจข้อมูลส่วนตัวที่เป็นข้อความธรรมดา เช่น จำนวนหุ้นหรือเลขบัญชี ไม่ได้ ต้องดูเนื้อหาเอง)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
