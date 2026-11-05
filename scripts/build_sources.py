"""สร้าง data/sources.json จากเอกสารใน data/raw/

ไล่ทุกไฟล์ต้นฉบับ (ไม่นับ .txt ที่แปลงเอง และ MANIFEST.md) แล้วบันทึก
URL ต้นทาง วันที่ยื่น วันที่ดึง และ sha256 ของไฟล์

ใช้: python scripts/build_sources.py
"""
import hashlib
import json
import re
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "sources.json"

SEC_ARCHIVE = "https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/"
SEC_FACTS = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
IDISC_INDEX = {
    "FS": "https://market.sec.or.th/public/idisc/en/Viewmore/fs-full?searchSymbol={sym}",
    "R561": "https://market.sec.or.th/public/idisc/en/Viewmore/fs-r561?searchSymbol={sym}",
}
IDISC_DOWNLOAD = "https://market.sec.or.th/public/idisc/Download?FILEID={fid}"

# FILEID ของ iDisc ที่หาจากหน้ารายการตามชื่อย่อไม่เจอ
# GULF: หน้ารายการของ iDisc ชี้ไปที่บริษัทเดิมก่อนควบรวม ไฟล์ของ GULF DEVELOPMENT
# หา FILEID จากลิงก์บนหน้าหุ้นของ set.or.th (งบ: หน้างบการเงิน · 56-1: หน้าข้อมูลบริษัทภาษาไทย)
# แล้วดาวน์โหลดผ่าน iDisc 56-1 ฉบับนี้มีแต่ภาษาไทย (T)
EXTRA_FILEIDS = {"GULF": ["dat/news/202608/2023FIN060820261731530042E.zip",
                          "dat/f56/2023ONE050320261956340770T.zip"]}

# CIK ของหุ้นสหรัฐ ดูได้จากบรรทัดแรกที่ fetch_us.py พิมพ์ออกมา
CIK = {"C": 831001, "DIS": 1744489, "MCD": 63908, "PEP": 77476, "VZ": 732712, "CRM": 1108524, "UNP": 100885, "DE": 315189, "WELL": 766704, "TMUS": 1283699, "COP": 1163165, "TJX": 109198, "T": 732717, "UBER": 1543151, "BA.US": 12927, "AMAT": 6951, "PANW": 1327567, "TXN": 97476, "LRCX": 707549, "NFLX": 1065280, "CAT": 18230, "GS": 886982, "RTX": 101829, "WFC": 72971, "TMO": 97745, "AMGN": 318154, "CRWD": 1535527, "LIN": 1707925, "AXP": 4962, "GILD": 882095, "MA": 1141391, "ABBV": 1551152, "COST": 909832, "CVX": 93410, "KO": 21344, "CSCO": 858877, "PG": 80424, "MRK": 310158, "UNH": 731766, "BAC": 70858, "HD": 354950, "GE": 40545, "PM": 1413329, "INTC": 50863, "MS": 895421, "NVDA": 1045810, "MSFT": 789019, "NEE": 753308, "MAR": 1048286, "ISRG": 1035267,
       "AVGO": 1730168, "VRT": 1674101, "ANET": 1596532, "CEG": 1868275, "VST": 1692819, "GEV": 1996810, "HLT": 1585689, "SYK": 310764,
       "AMD": 2488, "MU": 723125, "MRVL": 1835632, "DELL": 1571996, "SMCI": 1375365, "ORCL": 1341439,
       "EQIX": 1101239, "DLR": 1297996, "ETN": 1551182, "APH": 820313,
       "CIEN": 936395, "COHR": 820318, "CLS": 1030894, "AMZN": 1018724, "GOOGL": 1652044,
       "DUK": 1326160, "SO": 92122, "D": 715957, "AEP": 4904, "XEL": 72903,
       "SRE": 1032208, "NRG": 1013871, "TLN": 1622536, "ETR": 65984, "PCG": 1004980, "BE": 1664703,
       "FSLR": 1274494, "OKLO": 1849056, "CCJ": 1009001, "LEU": 1065059,
       "BKNG": 1075531, "ABNB": 1559720, "EXPE": 1324424, "RCL": 884887, "CCL": 815097,
       "NCLH": 1513761, "H": 1468174, "DAL": 27904, "UAL": 100517, "LVS": 1300514,
       "WYNN": 1174922, "BSX": 885725, "ABT": 1800, "MDT": 1613103, "EW": 1099800,
       "DXCM": 1093557, "PODD": 1145197, "BDX": 10795, "ZBH": 1136869, "HCA": 860730,
       "UHS": 352915, "LLY": 59478,
       "SPCX": 1181412, "AAPL": 320193, "META": 1326801, "TSLA": 1318605, "BRK.B": 1067983,
       "WMT": 104169, "JPM": 19617, "V": 1403161, "XOM": 2115436, "JNJ": 200406}

SKIP = {".txt", ".md"}
FIELDS = ["doc_id", "ticker", "market", "doc_type", "title", "url",
          "doc_date", "fetched_at", "file_path", "sha256"]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetched_at(path):
    return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")


def us_rows(ticker, folder):
    cik = CIK[ticker]
    for p in sorted(folder.iterdir()):
        if p.suffix.lower() in SKIP or not p.is_file():
            continue
        if p.name == "companyfacts.json":
            yield dict(doc_id=f"{ticker}-companyfacts",
                       doc_type="companyfacts", title=f"{ticker} XBRL company facts",
                       url=SEC_FACTS.format(cik=cik), doc_date="", path=p)
            continue
        # ใบแนบของ 8-K (เช่น ข่าวผลประกอบการ) มีส่วนท้ายชื่อไฟล์ เช่น _TEXTGIF
        m = re.match(r"(.+?)_(\d{4}-\d{2}-\d{2})_(\d{18})(?:_(\w+))?\.htm$", p.name)
        if not m:
            continue
        form, date, acc, part = m.groups()
        suffix = f"-{part}" if part else ""
        label = f" ({part})" if part else ""
        yield dict(doc_id=f"{ticker}-{acc}{suffix}",
                   doc_type=form, title=f"{ticker} {form} filed {date}{label}",
                   url=SEC_ARCHIVE.format(cik=cik, acc=acc), doc_date=date, path=p)


def idisc_fileids(sym):
    """คืน dict ชื่อไฟล์ zip -> FILEID เต็ม จากหน้ารายการของ iDisc"""
    ids = {}
    for url in IDISC_INDEX.values():
        req = urllib.request.Request(url.format(sym=sym),
                                     headers={"User-Agent": "aia-hw-toro/1.0 (homework)"})
        html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "ignore")
        for fid in re.findall(r"FILEID=([^\"'&<>\s]+\.zip)", html):
            ids[Path(fid).stem] = fid
    for fid in EXTRA_FILEIDS.get(sym, []):
        ids[Path(fid).stem] = fid
    return ids


def th_rows(sym, folder):
    ids = idisc_fileids(sym)
    for sub in sorted(folder.iterdir()):
        if not sub.is_dir():
            continue
        kind = "FS" if sub.name.startswith("FS_") else "56-1"
        # ชื่อไฟล์ iDisc ฝังวันที่ยื่นไว้ เช่น 1339FIN13082026... = 13/08/2026
        # รหัสประเภทมีหลายแบบ เช่น FIN, ONE, E1N
        m = re.search(r"(\d{4}[A-Z][A-Z0-9]{2})(\d{2})(\d{2})(\d{4})", sub.name)
        date = f"{m.group(4)}-{m.group(3)}-{m.group(2)}" if m else ""
        fid = next((v for k, v in ids.items() if m and k.startswith(m.group(0))), "")
        url = IDISC_DOWNLOAD.format(fid=fid) if fid else ""
        for p in sorted(sub.iterdir()):
            # .converted. คือไฟล์ที่ convert_legacy_office.ps1 แปลงเอง ไม่ใช่เอกสารต้นทาง
            if p.suffix.lower() in SKIP or ".converted." in p.name:
                continue
            yield dict(doc_id=f"{sym}-{kind}-{date}-{p.stem}",
                       doc_type=kind, title=f"{sym} {kind} filed {date} · {p.name}",
                       url=url, doc_date=date, path=p)


def main():
    rows = []
    for market, fn in (("US", us_rows), ("TH", th_rows)):
        base = RAW / market.lower()
        if not base.exists():
            continue
        for folder in sorted(base.iterdir()):
            if not folder.is_dir():
                continue
            for r in fn(folder.name, folder):
                p = r.pop("path")
                rows.append(dict(
                    ticker=folder.name, market=market,
                    fetched_at=fetched_at(p), file_path=p.relative_to(ROOT).as_posix(),
                    sha256=sha256(p), **r))
    # ลำดับคีย์ตาม FIELDS เพื่อให้ diff อ่านง่าย
    rows = [{k: r[k] for k in FIELDS} for r in rows]
    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    missing = [r["doc_id"] for r in rows if not r["url"]]
    print(f"เขียน {len(rows)} เอกสารลง {OUT.relative_to(ROOT)}")
    if missing:
        print("ไม่มี URL:", ", ".join(missing))


if __name__ == "__main__":
    main()
