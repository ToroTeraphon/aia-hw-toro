"""พิมพ์รายการหุ้นที่ข้อมูลไม่ครบจากของจริง แล้วเทียบกับ incomplete.md ว่ามีตัวไหนตกหล่น

ไม่แก้ไฟล์ใดเลย อ่านอย่างเดียว ตรวจ 2 อย่างที่เครื่องรู้เองได้
  1. หุ้นที่ catalyst_size_pct เป็น null (อ่านจาก output/data.json)
  2. ไฟล์ที่ extract.py แปลงเป็นข้อความไม่ได้ (อ่านจาก data/raw/<ตลาด>/<ตัว>/MANIFEST.md
     หัวข้อ "ไฟล์ที่แปลงเป็นข้อความไม่ได้") ถ้าโฟลเดอร์ data/raw ไม่มีในเครื่อง จะบอกและข้าม
สิ่งที่เครื่องตรวจให้ไม่ได้ คือเอกสารที่ดาวน์โหลดไม่ได้ และคะแนนที่ไม่มั่นใจ ต้องจดมือใน incomplete.md

แล้วเทียบว่ามีแถวของ ticker นั้นในตาราง incomplete.md พร้อมประเภทที่ตรงกันหรือยัง ตัวที่ไม่มีจะขึ้น !! และสคริปต์คืนรหัส 1

ใช้: python scripts/list_incomplete.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "output" / "data.json"
RAW = ROOT / "data" / "raw"
DOC = ROOT / "incomplete.md"
HEADING = "## ไฟล์ที่แปลงเป็นข้อความไม่ได้"


def unreadable_files(manifest):
    """ชื่อไฟล์ใต้หัวข้อ 'ไฟล์ที่แปลงเป็นข้อความไม่ได้' ใน MANIFEST.md (บรรทัดที่ขึ้นต้นด้วย - `...`)"""
    text = manifest.read_text(encoding="utf-8-sig")
    if HEADING not in text:
        return []
    section = text.split(HEADING, 1)[1].split("\n## ", 1)[0]
    return re.findall(r"^- `([^`]+)`", section, flags=re.M)


def mentioned(ticker, label, doc_text):
    """มีแถวในตารางของ incomplete.md ที่คอลัมน์แรกเป็น ticker และคอลัมน์ "ประเภท" เป็น label หรือไม่"""
    pattern = rf"^\|\s*{re.escape(ticker)}\s*\|\s*{re.escape(label)}\s*\|"
    return re.search(pattern, doc_text, flags=re.M) is not None


def main():
    stocks = json.loads(DATA.read_text(encoding="utf-8-sig"))["stocks"]
    doc_text = DOC.read_text(encoding="utf-8") if DOC.exists() else ""
    if not doc_text:
        print("หมายเหตุ: ไม่พบ incomplete.md จึงถือว่าทุกตัวตกหล่น\n")
    missing = []

    no_size = [s for s in stocks if s["catalyst_size_pct"] is None]
    print(f"1) ไม่มีขนาด Catalyst: {len(no_size)} ตัว")
    for s in no_size:
        ok = mentioned(s["ticker"], "ไม่มีขนาด Catalyst", doc_text)
        print(f"   {'  ' if ok else '!!'} {s['ticker']:<7}{s['market']}  {s['catalyst_size_formula'][:70]}")
        if not ok:
            missing.append((s["ticker"], "ไม่มีขนาด Catalyst"))

    print()
    if not RAW.exists():
        print("2) ไฟล์ที่แปลงไม่ได้: ข้าม (ไม่มี data/raw ในเครื่องนี้ ซึ่งไม่ถูกเก็บใน git)")
    else:
        rows = []
        for s in stocks:
            m = RAW / s["market"].lower() / s["ticker"] / "MANIFEST.md"
            if not m.exists():
                continue
            listed = unreadable_files(m)
            # MANIFEST ยังแสดงไฟล์ต้นฉบับแม้แปลงสำเร็จแล้ว ไฟล์ที่แปลงแล้วจะมี <ชื่อ>.converted.* ข้างกัน
            left = [f for f in listed
                    if not any((m.parent / f).parent.glob(Path(f).stem + ".converted.*"))]
            if left:
                rows.append((s["ticker"], left, len(listed)))
        print(f"2) ยังแปลงเป็นข้อความไม่ได้ (ไม่มีไฟล์ .converted): {len(rows)} ตัว")
        for t, left, total in rows:
            ok = mentioned(t, "แปลงไฟล์ไม่ได้", doc_text)
            print(f"   {'  ' if ok else '!!'} {t:<7}{len(left)}/{total} ไฟล์ เช่น {left[0]}")
            if not ok:
                missing.append((t, "แปลงไฟล์ไม่ได้"))

    print()
    if missing:
        print(f"ตกหล่นจาก incomplete.md ({len(missing)} รายการ ที่ขึ้น !! ข้างบน):")
        for t, why in missing:
            print(f"   {t}: {why}")
        return 1
    print("ทุกตัวที่เครื่องตรวจเจอ มีอยู่ใน incomplete.md แล้ว")
    print("(เครื่องตรวจไม่ได้: เอกสารที่ดาวน์โหลดไม่ได้ และคะแนนที่ไม่มั่นใจ ต้องดูใน incomplete.md เอง)")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
