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
CIK = {
    "TDG": 1260221, "TT": 1466258, "TXT": 217346, "UPS": 1090727, "URI": 1067701, "VLTO": 1967680, "VRSK": 1442145, "WAB": 943452, "WM": 823768, "XYL": 1524472, "ACN": 1467373, "ADBE": 796343, "ADI": 6281, "ADSK": 769397, "AKAM": 1086222,
    "NDSN": 72331, "NOC": 1133421, "NSC": 702165, "ODFL": 878927, "OTIS": 1781335, "PAYX": 723531, "PCAR": 75362, "PH": 76334, "PNR": 77360, "PWR": 1050915, "ROK": 1024478, "ROL": 84839, "RSG": 1060391, "SNA": 91440, "SWK": 93556,
    'HONA':2089271,'HUBB':48898,'HWM':4281,'IEX':832101,'IR':1699150,'ITW':49826,'J':52988,'JBHT':728535,'JCI':833444,'LDOS':1336920,'LHX':202058,'LII':1069202,'LUV':92380,'MAS':62996,'MMM':66740,
    'EFX':33185,'EME':105634,'EMR':32604,'EXPD':746515,'FAST':815556,'FDX':1048911,'FDXF':2082247,'FERG':2011641,'FIX':1035983,'FTV':1659166,'GD':40533,'GNRC':1474735,'GWW':277135,'HII':1501585,'HON':773840,
    'ZTS':1555280,'ADP':8670,'ALLE':1579241,'AME':1037868,'AOS':91142,'AXON':1069183,'BR':1383312,'CARR':1783180,'CHRW':1043277,'CMI':26172,'CPRT':900075,'CSX':277948,'CTAS':723254,'DD':1666700,'DOV':29905,
    'MCK':927653,'MRNA':1682852,'MTD':1037646,'PFE':78003,'REGN':872589,'RMD':943819,'RVTY':31791,'SOLV':1964738,'STE':1757898,'TECH':842023,'VEEV':1393052,'VRTX':875320,'VTRS':1792044,'WAT':1000697,'WST':105770,
    'COR':1140859,'CRL':1100682,'CVS':64803,'DGX':1022079,'DHR':313616,'DVA':927066,'ELV':1156039,'GEHC':1932393,'HSIC':1000228,'HUM':49071,'IDXX':874716,'ILMN':1110803,'INCY':879169,'IQV':1478242,'LH':920148,
    'TROW':1113169,'TRV':86312,'USB':36104,'WRB':11544,'WTW':1140536,'XYZ':1512673,'A':1090872,'ALGN':1097149,'BAX':10456,'BIIB':875045,'BMY':14272,'CAH':721371,'CI':1739940,'CNC':1071739,'COO':711404,
    'MTB':36270,'NDAQ':1120193,'NTRS':73124,'PFG':1126328,'PGR':80661,'PNC':713676,'PRU':1137774,'PYPL':1633917,'RF':1281761,'RJF':720005,'SCHW':316709,'SPGI':64040,'STT':93751,'SYF':1601712,'TFC':92230,
    'GPN':1123360,'HBAN':49196,'HIG':874766,'HOOD':1783879,'IBKR':1381197,'ICE':1571949,'IVZ':914208,'JKHY':779152,'KEY':91576,'KKR':1404912,'L':60086,'MCO':1059556,'MET':1099219,'MRSH':62709,'MSCI':1408198,
    'CB':896159,'CBOE':1374310,'CFG':759944,'CINF':20286,'CME':1156375,'COF':927628,'COIN':1679788,'CPAY':1175454,'EG':1095073,'ERIE':922621,'FDS':1013237,'FIS':1136893,'FISV':798354,'FITB':35527,'GL':320335,
    'ACGL':947484,'AFL':4977,'AIG':5272,'AIZ':1267238,'AJG':354190,'ALL':899051,'AMP':820027,'AON':315293,'APO':1858681,'ARES':1176948,'BEN':38777,'BLK':2012383,'BNY':1390777,'BRO':79282,'BX':1393818,

    'EOG':821189,'EQT':33213,'EXE':895126,'FANG':1539838,'HAL':45012,'KMI':1506307,'MPC':1510295,'OKE':1039684,'OXY':797468,'PSX':1534701,'SLB':87347,'TPL':1811074,'TRGP':1389170,'VLO':1035002,'WMB':107263,
"KMB": 55785, "KR": 56873, "MDLZ": 1103982, "MKC": 63754, "MNST": 865752, "MO": 764180, "SJM": 91419, "STZ": 16918, "SYY": 96021, "TGT": 27419, "TSN": 100493, "APA": 1841666, "BKR": 1701605, "DVN": 1090012, "ADM": 7084, "BF.B": 14693, "BG": 1996862, "CASY": 726958, "CHD": 313927, "CL": 21665, "CLX": 21076, "DG": 29534, "DLTR": 935703, "EL": 1001250, "GIS": 40704, "HRL": 48465, "HSY": 47111, "KDP": 1418135, "KHC": 1637459, "LOW": 60667, "LULU": 1397187, "MGM": 789570, "NKE": 320187, "NVR": 906163, "ORLY": 898173, "PHM": 822416, "RL": 1037038, "ROST": 745732, "SBUX": 829224, "TPR": 1116132, "TSCO": 916365, "ULTA": 1403568, "WSM": 719955, "YUM": 1041061, "BBY": 764478, "CMG": 1058090, "CVNA": 1690820, "DASH": 1792789, "DECK": 910521, "DHI": 882184, "DPZ": 1286681, "DRI": 940944, "EBAY": 1065088, "F": 37996, "GM": 1467858, "GPC": 40987, "GRMN": 1121788, "HAS": 46080, "LEN": 920760, "LMT": 936468, "APP": 1751008, "CHTR": 1091667, "CMCSA": 1166691, "FOXA": 1754301, "LYV": 1335258, "NWSA": 1564708, "OMC": 29989, "RDDT": 1713445, "TKO": 1973266, "TTWO": 946581, "APTV": 1521332, "AZO": 866787, "ECHO": 1415404, "SKYD": 2041610, "C": 831001, "DIS": 1744489, "MCD": 63908, "PEP": 77476, "VZ": 732712, "CRM": 1108524, "UNP": 100885, "DE": 315189, "WELL": 766704, "TMUS": 1283699, "COP": 1163165, "TJX": 109198, "T": 732717, "UBER": 1543151, "BA.US": 12927, "AMAT": 6951, "PANW": 1327567, "TXN": 97476, "LRCX": 707549, "NFLX": 1065280, "CAT": 18230, "GS": 886982, "RTX": 101829, "WFC": 72971, "TMO": 97745, "AMGN": 318154, "CRWD": 1535527, "LIN": 1707925, "AXP": 4962, "GILD": 882095, "MA": 1141391, "ABBV": 1551152, "COST": 909832, "CVX": 93410, "KO": 21344, "CSCO": 858877, "PG": 80424, "MRK": 310158, "UNH": 731766, "BAC": 70858, "HD": 354950, "GE": 40545, "PM": 1413329, "INTC": 50863, "MS": 895421, "NVDA": 1045810, "MSFT": 789019, "NEE": 753308, "MAR": 1048286, "ISRG": 1035267,
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
