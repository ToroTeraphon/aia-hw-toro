# output/

ใส่ผลงานของคุณที่นี่

- ภาพหน้าจอ dashboard หรือผลวิเคราะห์ (`.png`, `.jpg`)
- ลิงก์ผลงานที่เปิดดูได้ (เขียนไว้ในไฟล์นี้)
- ไฟล์ผลลัพธ์เล็ก ๆ ที่สร้างเอง เช่น `dashboard.html`

ห้ามใส่: ไฟล์ข้อมูลดิบที่ซื้อมา (เช่น SETSMART), บทวิเคราะห์โบรกเกอร์, ข้อมูลพอร์ตจริง

## ลิงก์ผลงาน

- เว็บออนไลน์: https://toroteraphon.github.io/aia-hw-toro/output/ (GitHub Pages อัปเดตตามทุกครั้งที่ push)
- [index.html](index.html): เว็บ Catalyst Tracker 2027 ดาวน์โหลดแล้วเปิดในเบราว์เซอร์ได้เลย ไม่ต้องมี server
- [stocks.csv](stocks.csv): สรุปรายหุ้น 11 ตัว (ตัวจุดประกาย คะแนน เงื่อนไขตัดทิ้ง สถานะ)
- [data.csv](data.csv): หลักฐานทีละแถว อ้าง doc_id ใน [../data/sources.csv](../data/sources.csv)

`index.html` สร้างจาก CSV ด้วย `python scripts/build_site.py` ห้ามแก้ไฟล์นี้ตรง ๆ
