# scripts/

## ขั้นตอนดึงเอกสาร

1. ดึงเอกสารด้วย skill `stock-deepdive-lite:fetch` ลง `data/raw/` (ไม่ commit)
   - หุ้นสหรัฐ: `fetch_us.py <TICKER> --out ./data/raw/us/<TICKER> --contact "ชื่อ อีเมล"` (SEC บังคับให้ระบุผู้ติดต่อ อย่าเขียนอีเมลลงไฟล์ใน repo)
   - หุ้นไทย: `fetch_th.py <SYMBOL> --out ./data/raw/th/<SYMBOL>`
   - แล้วรัน `extract.py` กับโฟลเดอร์นั้น เพื่อแปลงเป็นข้อความและได้ `MANIFEST.md` (ต้องมี `pymupdf` จึงจะอ่าน PDF ได้)
2. รัน `python scripts/build_sources.py` เพื่อสร้าง `data/sources.csv` ใหม่ทั้งไฟล์

## build_sources.py

ไล่ไฟล์ต้นฉบับทุกไฟล์ใน `data/raw/` แล้วบันทึก URL ต้นทาง วันที่ยื่น วันที่ดึง และ sha256

- หุ้นสหรัฐ: URL ชี้ไปที่โฟลเดอร์ของ filing บน SEC EDGAR สร้างจากเลข accession ในชื่อไฟล์ ต้องเพิ่ม CIK ของหุ้นใหม่ในตัวแปร `CIK`
- หุ้นไทย: URL เป็นลิงก์ดาวน์โหลด zip จาก iDisc ซึ่งสคริปต์หาจากหน้ารายการของ iDisc ส่วน sha256 คิดจากไฟล์ที่แตกออกจาก zip แล้ว
- doc_id สร้างจากตัวเอกสารเอง (หุ้นสหรัฐใช้เลข accession หุ้นไทยใช้ประเภท + วันที่ยื่น + ชื่อไฟล์) จึงไม่เปลี่ยนเมื่อดึงเอกสารเพิ่ม หลักฐานใน `output/data.csv` ที่อ้าง doc_id ไว้จึงไม่หลุด
