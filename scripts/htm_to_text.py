"""แปลงไฟล์ .htm ของ SEC EDGAR เป็นข้อความ เพราะ extract.py ไม่แปลง .htm ให้

เขียน <ชื่อเดิม>.txt ไว้ข้างไฟล์ .htm ใน data/raw/ (ไม่ commit)
ตัดแท็ก HTML, script/style และส่วนหัว XBRL (ix:header) ออก แล้วเก็บการขึ้นบรรทัดตามย่อหน้าและแถวตาราง

ใช้: python scripts/htm_to_text.py data/raw/us/<TICKER>
"""
import html
import re
import sys
from pathlib import Path


def to_text(raw):
    t = re.sub(r"(?is)<(script|style|ix:header).*?</\1>", " ", raw)
    t = re.sub(r"(?i)<(br|/p|/div|/tr|/li|/h\d)[^>]*>", "\n", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = "\n".join(re.sub(r"[ \t]+", " ", line).strip() for line in t.splitlines())
    return re.sub(r"\n{2,}", "\n", t)


def main():
    for folder in map(Path, sys.argv[1:]):
        for p in sorted(folder.glob("*.htm")):
            out = p.with_suffix(".txt")
            out.write_text(to_text(p.read_text("utf-8", "ignore")), "utf-8")
            print(f"{out.stat().st_size:>9}  {out}")


if __name__ == "__main__":
    main()
