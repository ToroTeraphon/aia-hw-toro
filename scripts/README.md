# scripts/

## ขั้นตอนดึงเอกสาร

1. ดึงเอกสารด้วย skill `stock-deepdive-lite:fetch` ลง `data/raw/` (ไม่ commit)
   - หุ้นสหรัฐ: `fetch_us.py <TICKER> --out ./data/raw/us/<TICKER> --contact "ชื่อ อีเมล"` (SEC บังคับให้ระบุผู้ติดต่อ อย่าเขียนอีเมลลงไฟล์ใน repo)
   - หุ้นไทย: `fetch_th.py <SYMBOL> --out ./data/raw/th/<SYMBOL>`
   - แล้วรัน `extract.py` กับโฟลเดอร์นั้น เพื่อแปลงเป็นข้อความและได้ `MANIFEST.md` (ต้องมี `pymupdf` จึงจะอ่าน PDF ได้)
2. ถ้า extract.py แจ้งว่าแปลง .doc/.xls รุ่นเก่าไม่ได้ ให้รัน `powershell -ExecutionPolicy Bypass -File scripts/convert_legacy_office.ps1` แล้วรัน `extract.py` ซ้ำ
3. รัน `python scripts/build_sources.py` เพื่อสร้าง `data/sources.csv` ใหม่ทั้งไฟล์

## convert_legacy_office.ps1

แปลง .doc/.xls เป็น .docx/.xlsx ไฟล์ที่ได้ชื่อ `<ชื่อเดิม>.converted.docx` วางข้างไฟล์ต้นฉบับ ไม่แก้ไฟล์ต้นฉบับ

- บางไฟล์จาก iDisc เป็น .docx/.xlsx อยู่แล้ว แต่ตั้งนามสกุลผิด (ไบต์แรกเป็น `PK`) สคริปต์คัดลอกแล้วเปลี่ยนนามสกุลให้
- ไฟล์รุ่นเก่าจริงเปิดด้วย Word/Excel ในเครื่อง แบบอ่านอย่างเดียวและปิดมาโคร ถ้าค้างเกินเวลาที่ตั้งไว้ (ค่าเริ่มต้น 90 วินาที) จะข้ามและแจ้ง
- ไฟล์ต้องบันทึกเป็น UTF-8 แบบมี BOM ไม่อย่างนั้น Windows PowerShell 5.1 จะอ่านภาษาไทยในสคริปต์ผิดจนรันไม่ได้

## build_sources.py

ไล่ไฟล์ต้นฉบับทุกไฟล์ใน `data/raw/` แล้วบันทึก URL ต้นทาง วันที่ยื่น วันที่ดึง และ sha256

- หุ้นสหรัฐ: URL ชี้ไปที่โฟลเดอร์ของ filing บน SEC EDGAR สร้างจากเลข accession ในชื่อไฟล์ ต้องเพิ่ม CIK ของหุ้นใหม่ในตัวแปร `CIK`
- หุ้นไทย: URL เป็นลิงก์ดาวน์โหลด zip จาก iDisc ซึ่งสคริปต์หาจากหน้ารายการของ iDisc ส่วน sha256 คิดจากไฟล์ที่แตกออกจาก zip แล้ว
- doc_id สร้างจากตัวเอกสารเอง (หุ้นสหรัฐใช้เลข accession หุ้นไทยใช้ประเภท + วันที่ยื่น + ชื่อไฟล์) จึงไม่เปลี่ยนเมื่อดึงเอกสารเพิ่ม หลักฐานใน `output/data.csv` ที่อ้าง doc_id ไว้จึงไม่หลุด
