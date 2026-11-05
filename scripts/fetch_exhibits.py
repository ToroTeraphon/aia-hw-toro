"""โหลดไฟล์ข่าวผลประกอบการ (Exhibit 99) ที่ fetch_us.py ไม่ได้ดึงมา

fetch_us.py ดึงเฉพาะใบแนบแบบ TEXT.GIF ถ้า 8-K ที่รายงานผลประกอบการ (Item 2.02) ไม่มีไฟล์ข่าวมาด้วย
สคริปต์นี้จะดูรายการไฟล์ในโฟลเดอร์ filing บน sec.gov แล้วโหลด Exhibit 99 มาตั้งชื่อ
8-K_<วันที่>_<accession>_TEXTGIF.htm เพื่อให้ htm_to_text.py และ build_sources.py ใช้ต่อได้เหมือนไฟล์อื่น

ต้องตั้งผู้ติดต่อสำหรับ SEC ผ่านตัวแปรสภาพแวดล้อม SEC_CONTACT ตอนรัน (อย่าเขียนลงไฟล์ใน repo)
ใช้: SEC_CONTACT="ชื่อ อีเมล" python scripts/fetch_exhibits.py <TICKER>
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def get(url, contact):
    req = urllib.request.Request(url, headers={"User-Agent": contact})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def main():
    contact = os.environ.get("SEC_CONTACT")
    if len(sys.argv) != 2 or not contact:
        raise SystemExit(__doc__)
    folder = ROOT / "data" / "raw" / "us" / sys.argv[1].upper()
    facts = json.loads((folder / "companyfacts.json").read_text(encoding="utf-8-sig"))
    cik = int(facts["cik"])
    done = 0
    for f in sorted(folder.glob("8-K_*.htm")):
        m = re.match(r"8-K_(\d{4}-\d{2}-\d{2})_(\d{18})\.htm$", f.name)
        if not m:
            continue  # ข้ามไฟล์ใบแนบที่ดึงมาแล้ว
        date, acc = m.groups()
        target = folder / f"8-K_{date}_{acc}_TEXTGIF.htm"
        text = f.read_text(encoding="utf-8", errors="ignore")
        if target.exists() or "2.02" not in text or "results of operations" not in text.lower():
            continue
        base = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/"
        items = json.loads(get(base + "index.json", contact))["directory"]["item"]
        names = [i["name"] for i in items if re.search(r"(ex|exhibit)[-_]?99|99[-_.]?1\.htm$", i["name"], re.I) and i["name"].endswith(".htm")]
        if not names:
            # บางบริษัทตั้งชื่อไฟล์ข่าวเอง (เช่น xxx-20260630xearningsre.htm) ใช้ไฟล์ .htm ที่ใหญ่ที่สุด
            # ที่ไม่ใช่หน้าหลักของ 8-K (ชื่อลงท้ายด้วยวันที่ 8 หลัก) และไม่ใช่ไฟล์ R<เลข>.htm ของ XBRL
            others = [i for i in items if i["name"].endswith(".htm")
                      and not re.match(r"R\d+\.htm$", i["name"]) and not re.search(r"-\d{8}\.htm$", i["name"])]
            names = [i["name"] for i in sorted(others, key=lambda i: -int(i.get("size") or 0))][:1]
        if not names:
            print(f"{f.name}: ไม่พบไฟล์ Exhibit 99 ในโฟลเดอร์ filing")
            continue
        target.write_bytes(get(base + names[0], contact))
        print(f"{f.name}: โหลด {names[0]} -> {target.name}")
        done += 1
    print(f"โหลดแล้ว {done} ไฟล์ (รัน scripts/htm_to_text.py ต่อ)")


if __name__ == "__main__":
    main()
