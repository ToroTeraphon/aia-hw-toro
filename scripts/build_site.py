"""สร้าง output/index.html จาก output/data.json และ data/sources.json

หน้าเว็บอ่านข้อมูลได้ 2 ทาง:
  1. เปิดผ่านเว็บ (เช่น GitHub Pages): ดึง data.json และ ../data/sources.json ตอนเปิดหน้า
     จึงเห็นหุ้นที่เพิ่มใน data.json ทันทีโดยไม่ต้องรันสคริปต์นี้
  2. เปิดจากไฟล์ในเครื่อง (ดับเบิลคลิก): เบราว์เซอร์ไม่ยอมให้อ่านไฟล์ JSON ข้าง ๆ
     จึงใช้สำเนาที่ฝังไว้ในหน้าเว็บแทน สำเนานี้สร้างโดยสคริปต์นี้ ต้องรันใหม่หลังแก้ข้อมูล
     เพื่อให้สำเนาตรงกับ data.json

สคริปต์นี้ยังตรวจข้อมูลก่อนสร้าง: doc_id ของหลักฐานทุกแถวต้องมีใน sources.json
อย่าแก้ index.html ตรง ๆ เพราะจะถูกเขียนทับ

ใช้: python scripts/build_site.py
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output" / "index.html"


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8-sig"))  # -sig: ทนต่อไฟล์ที่มี BOM


MIN_SCORE_T1 = 4   # T1 ต้องได้คะแนนอย่างน้อยเท่านี้
MIN_DOCS_T1 = 2    # และอ้างเอกสารอย่างน้อยกี่ฉบับ (หลักฐานหลายแถวจากเอกสารฉบับเดียวไม่นับเป็นหลายแหล่ง)
MAX_SCORE_T3 = 2   # คะแนนไม่เกินนี้ = T3


# ประเภทฐานที่ใช้เทียบขนาด Catalyst (ค่าที่ catalyst_size_type ใช้ได้) · หน้าเว็บมีตารางป้ายชื่อชุดเดียวกัน
SIZE_TYPES = ["revenue", "assets", "units_rooms", "units_beds", "units_mw", "units_aircraft",
              "units_sites", "profit", "progress"]


def tier_numbers(s):
    ev = s["evidence"]
    n = lambda sig: sum(e["signal"] == sig for e in ev)
    return s["evidence_score"], len({e["doc_id"] for e in ev}), n("support"), n("challenge")


def derive_tier(s):
    """T1 = ผ่านทั้ง 3 เกณฑ์ (คะแนน, จำนวนเอกสาร, ค้านไม่เกินหนุน) · T3 = คะแนนต่ำ · T2 = ที่เหลือ"""
    score, docs, sup, ch = tier_numbers(s)
    if score <= MAX_SCORE_T3:
        return "T3"
    return "T1" if score >= MIN_SCORE_T1 and docs >= MIN_DOCS_T1 and ch <= sup else "T2"


def tier_reason(s):
    score, docs, sup, ch = tier_numbers(s)
    ok = lambda b: "ผ่าน" if b else "ไม่ผ่าน"
    return (f"คะแนน {score} (เกณฑ์ ≥{MIN_SCORE_T1}: {ok(score >= MIN_SCORE_T1)}) · "
            f"อ้างเอกสาร {docs} ฉบับ (เกณฑ์ ≥{MIN_DOCS_T1}: {ok(docs >= MIN_DOCS_T1)}) · "
            f"หนุน {sup} ค้าน {ch} (ค้านไม่เกินหนุน: {ok(ch <= sup)})")


def main():
    stocks = read("output/data.json")["stocks"]
    wrong = [f"{s['ticker']}: ใน data.json เป็น {s.get('tier')} แต่เกณฑ์ให้ {derive_tier(s)}"
             for s in stocks if s.get("tier") != derive_tier(s)]
    if wrong:
        raise SystemExit("tier ไม่ตรงกับเกณฑ์ (แก้ช่อง tier และ tier_reason ใน data.json):\n  " + "\n  ".join(wrong))
    bad_type = [f"{s['ticker']}: catalyst_size_type = {s.get('catalyst_size_type')!r}" for s in stocks
                if (s.get("catalyst_size_type") is None) != (s.get("catalyst_size_basis") is None)
                or (s.get("catalyst_size_type") is not None and s["catalyst_size_type"] not in SIZE_TYPES)]
    if bad_type:
        raise SystemExit(f"catalyst_size_type ต้องเป็น null พร้อม basis หรือเป็นหนึ่งใน {SIZE_TYPES}:\n  " + "\n  ".join(bad_type))
    used = {e["doc_id"] for s in stocks for e in s["evidence"]}
    # ฝังเฉพาะเอกสารที่หลักฐานอ้างถึง เพื่อให้สำเนาที่ฝังไม่ใหญ่เกินจำเป็น
    sources = {s["doc_id"]: {k: s[k] for k in ("title", "url", "doc_type", "doc_date")}
               for s in read("data/sources.json") if s["doc_id"] in used}
    missing = sorted(used - sources.keys())
    if missing:
        raise SystemExit(f"doc_id ใน data.json ที่ไม่มีใน sources.json: {missing}")

    payload = json.dumps({"stocks": stocks, "sources": sources,
                          "built": date.today().isoformat()}, ensure_ascii=False)
    OUT.write_text(TEMPLATE.replace("__DATA__", payload.replace("</", "<\\/")), "utf-8")
    n_ev = sum(len(s["evidence"]) for s in stocks)
    print(f"เขียน {OUT.relative_to(ROOT)} · หุ้น {len(stocks)} ตัว · หลักฐาน {n_ev} แถว · เอกสาร {len(sources)} ฉบับ")


TEMPLATE = r"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Catalyst Tracker 2027</title>
<style>
:root{--bg:#f7f6f2;--card:#fff;--ink:#1d1d1b;--muted:#6b6a65;--line:#e4e2db;
--sup:#1f7a4d;--sup-bg:#e3f2ea;--ch:#b3402a;--ch-bg:#f8e6e1;--neu:#6b6a65;--neu-bg:#eeede8;--acc:#2f5bd3}
@media (prefers-color-scheme:dark){:root{--bg:#141413;--card:#1e1e1c;--ink:#ecebe6;--muted:#a3a29b;--line:#33322f;
--sup:#5fc28f;--sup-bg:#1d3328;--ch:#ee8a73;--ch-bg:#3a231d;--neu:#a3a29b;--neu-bg:#2a2a27;--acc:#8aa8ff}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 system-ui,-apple-system,"Segoe UI","Noto Sans Thai",sans-serif}
main{max-width:1100px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:26px;margin:0}
.titlebar{display:flex;align-items:center;gap:10px;margin:0 0 4px;position:relative}
.tip{position:relative}
.tip>button{width:26px;height:26px;border-radius:50%;border:1.5px solid var(--acc);background:var(--card);color:var(--acc);font:700 15px/1 Georgia,serif;font-style:italic;cursor:pointer;padding:0}
.tip>button:hover,.tip>button[aria-expanded=true]{background:var(--acc);color:var(--bg)}
.pop{display:none;position:absolute;left:0;top:34px;z-index:10;width:min(460px,calc(100vw - 32px));background:var(--card);border:1px solid var(--line);border-top:3px solid var(--acc);border-radius:10px;padding:12px 16px;box-shadow:0 8px 24px rgba(0,0,0,.18);font-size:14px;line-height:1.55}
.tip:hover .pop,.tip:focus-within .pop,.tip.open .pop{display:block}
.pop h2{font-size:14px;margin:10px 0 4px}.pop h2:first-child{margin-top:0}
.pop p{margin:0 0 6px}.pop ol,.pop ul{margin:0 0 6px;padding-left:20px}
.pop .warn{color:var(--ch)}
@media (max-width:560px){.tip{position:static}.pop{left:0;right:0;width:auto}}
.sub{color:var(--muted);margin:0 0 16px}
.note{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--acc);border-radius:8px;padding:12px 14px;margin:0 0 20px}
.controls{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;margin:0 0 12px}
.group{display:grid;grid-template-columns:110px 1fr;gap:8px;align-items:center;padding:6px 0}
.group+.group{border-top:1px solid var(--line)}
.group .label{font-size:13px;color:var(--muted);font-weight:600}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chips button{border:1px solid var(--line);background:var(--bg);color:var(--ink);border-radius:999px;padding:4px 12px;cursor:pointer;font:inherit;font-size:14px}
.chips button[aria-pressed=true]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.chips button:disabled{opacity:.35;cursor:default}
.count{color:var(--muted);font-size:13px;margin:0 0 10px}
.grp{font-size:15px;margin:18px 0 8px;padding-bottom:4px;border-bottom:2px solid var(--line)}
.grp small{display:block;font-weight:400;font-size:13px;color:var(--muted)}
.empty{color:var(--muted);padding:20px;text-align:center;background:var(--card);border:1px dashed var(--line);border-radius:10px}
@media (max-width:560px){.group{grid-template-columns:1fr;gap:4px}}
.stock{background:var(--card);border:1px solid var(--line);border-radius:10px;margin:0 0 10px;overflow:hidden}
.head{display:grid;grid-template-columns:72px 1fr auto;gap:12px;align-items:center;padding:12px 14px;cursor:pointer;width:100%;border:0;background:none;color:inherit;font:inherit;text-align:left}
.tk{font-weight:700;font-size:17px}
.tk small{display:block;font-weight:400;font-size:12px;color:var(--muted)}
.cat{min-width:0}
.cat b{display:block}
.cat span{color:var(--muted);font-size:13px}
.cat .size{display:flex;flex-wrap:wrap;gap:4px 8px;align-items:baseline;margin-top:6px;padding:4px 10px;background:var(--bg);border-left:3px solid var(--acc);border-radius:6px}
.cat .size .lab{font-size:12px;font-weight:600}
.cat .size .pct{font-size:18px;font-weight:700;color:var(--acc)}
.cat .size .of{color:var(--ink)}
.cat .size.none{border-left-color:var(--line)}
.cat .size .tag{margin:0}
.score{text-align:center}
.dots{letter-spacing:2px;font-size:14px;color:var(--acc)}
.score small{display:block;color:var(--muted);font-size:12px}
.body{display:none;border-top:1px solid var(--line);padding:12px 14px}
.stock.open .body{display:block}
.meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px;margin:0 0 12px}
.meta div{background:var(--bg);border-radius:8px;padding:8px 10px}
.meta dt{font-size:12px;color:var(--muted)}
.meta dd{margin:0}
.ev{list-style:none;margin:0;padding:0}
.ev li{border-top:1px solid var(--line);padding:10px 0}
.ev li:first-child{border-top:0}
.tag{display:inline-block;font-size:12px;border-radius:4px;padding:1px 7px;margin-right:6px;font-weight:600}
.support{color:var(--sup);background:var(--sup-bg)}.challenge{color:var(--ch);background:var(--ch-bg)}.neutral{color:var(--neu);background:var(--neu-bg)}
.src{font-size:13px;color:var(--muted);margin-top:4px}
.src a{color:var(--acc)}
.evnote{font-size:13px;margin-top:4px;color:var(--muted)}
.docs{margin:0 0 12px;font-size:14px}
.docs ul{margin:4px 0 0;padding-left:20px}
.docs a{color:var(--acc)}
.tier{margin-left:4px}
.legend{margin-top:28px;font-size:14px}
.legend table{border-collapse:collapse;width:100%;background:var(--card)}
.legend td{border:1px solid var(--line);padding:6px 10px;vertical-align:top}
footer{margin-top:24px;color:var(--muted);font-size:13px}
@media (max-width:560px){.head{grid-template-columns:56px 1fr;}.score{grid-column:1/-1;text-align:left;display:flex;gap:8px;align-items:center}.score small{display:inline}}
</style>
</head>
<body>
<main>
<div class="titlebar"><h1>Catalyst Tracker 2027</h1>
<div class="tip" id="tip"><button type="button" id="tip-btn" aria-expanded="false" aria-controls="tip-pop" aria-label="ภาพรวมและวิธีใช้เว็บนี้">i</button>
<div class="pop" id="tip-pop" role="region" aria-label="ภาพรวมและวิธีใช้เว็บนี้">
<h2>เว็บนี้ทำอะไร</h2>
<p id="tip-sum"></p>
<p class="warn"><b>คะแนนวัดความแน่นของหลักฐาน ไม่ใช่การทำนายราคา และไม่ใช่คำแนะนำซื้อหรือขาย</b></p>
<h2>เป้าหมาย 3 ขั้น</h2>
<ol>
<li><b>คัดหุ้น:</b> คัดจากหลักฐานและจัดระดับ Watchlist T1–T3 (ผลงานในหน้านี้อยู่ที่ขั้นนี้)</li>
<li><b>Deep Dive รายตัว:</b> เริ่มจาก T1 ถ้าหมดแล้วค่อยทำ T2 ส่วน T3 ยังไม่ทำ</li>
<li><b>เก็บ metric:</b> รายได้ กำไร จำนวนห้อง ฯลฯ ของแต่ละหุ้นว่าดีขึ้นอย่างไรใน 1 ปีข้างหน้า เก็บเองจากเอกสารที่บริษัทยื่น เพราะหุ้นไทยไม่มีเว็บที่รายงานตัวเลขเหล่านี้ให้</li>
</ol>
<h2>วิธีใช้หน้านี้</h2>
<ul>
<li>กรองด้วยปุ่ม Watchlist · ธีม · คะแนน · ขนาด Catalyst แล้วเลือกการเรียงลำดับ</li>
<li>กดที่การ์ดหุ้นเพื่อดูหลักฐานหนุน/ค้านทีละแถว พร้อมลิงก์ไปเอกสารต้นทาง</li>
<li>ตัวเลขที่ไม่มีในเอกสารเว้นว่างไว้ ไม่ได้เดา</li>
</ul>
</div></div></div>
<p class="sub" id="sub">หุ้นไทย + สหรัฐ · ตัวจุดประกายปี 2027 จากเอกสารที่บริษัทยื่นเอง</p>
<div class="note"><b>คะแนนวัดความแน่นของหลักฐาน ไม่ใช่การทำนายราคา และไม่ใช่คำแนะนำซื้อหรือขาย</b><br>
กดที่หุ้นเพื่อดูหลักฐานหนุน/ค้านทีละแถว และลิงก์ไปเอกสารต้นทาง ตัวเลขที่ไม่มีในเอกสารเว้นว่างไว้ ไม่ได้เดา</div>
<div class="controls">
  <div class="group"><span class="label" id="lb-tier">Watchlist</span><div class="chips" id="f-tier" role="group" aria-labelledby="lb-tier"></div></div>
  <div class="group"><span class="label" id="lb-theme">ธีม</span><div class="chips" id="f-theme" role="group" aria-labelledby="lb-theme"></div></div>
  <div class="group"><span class="label" id="lb-score">กรองตามคะแนน</span><div class="chips" id="f-score" role="group" aria-labelledby="lb-score"></div></div>
  <div class="group"><span class="label" id="lb-basis">ขนาด Catalyst เทียบกับ</span><div class="chips" id="f-basis" role="group" aria-labelledby="lb-basis"></div></div>
  <div class="group"><span class="label" id="lb-sort">เรียงลำดับ</span><div class="chips" id="f-sort" role="group" aria-labelledby="lb-sort"></div></div>
</div>
<p class="count" id="count"></p>
<div id="list"></div>
<section class="legend">
<h2>Watchlist (T1–T3)</h2>
<table>
<tr><td>T1 · ติด Watchlist</td><td>ผ่านทั้ง 3 ข้อ: คะแนน ≥4 · อ้างเอกสารอย่างน้อย 2 ฉบับ · จำนวนหลักฐานค้านไม่เกินหลักฐานหนุน</td></tr>
<tr><td>T2 · รอข้อมูล</td><td>คะแนน ≥3 แต่ไม่ผ่านอย่างน้อย 1 ข้อข้างบน</td></tr>
<tr><td>T3 · ยังไม่ติด</td><td>คะแนน ≤2</td></tr>
</table>
<p>T คือระดับของหลักฐาน ไม่ใช่ระดับความน่าลงทุน ใช้เรียงลำดับว่าจะทำ Deep Dive ตัวไหนก่อน: เริ่มจาก T1 ถ้าหมดแล้วค่อยทำ T2 ส่วน T3 ยังไม่ทำ จำนวนหนุน/ค้านนับเป็นแถว ไม่ได้ถ่วงน้ำหนักว่าหลักฐานแถวไหนสำคัญกว่า</p>
<h2>เกณฑ์คะแนน (1–5)</h2>
<table>
<tr><td>5</td><td>ตัวจุดประกายมีผลแล้ว หรือมีสัญญาผูกพันกับลูกค้าแล้ว</td></tr>
<tr><td>4</td><td>กำลังสร้างหรือดำเนินการ มีเงินที่จ่ายจริงหรือผูกพันแล้ว และมีวันที่ชัด</td></tr>
<tr><td>3</td><td>แผนของบริษัทที่มีวันที่ในหรือก่อนปี 2027 และมีตัวเลขรองรับบางส่วน หรือแนวโน้มต่อเนื่องที่มีตัวเลขในงบรองรับ</td></tr>
<tr><td>2</td><td>แผนที่ยังไม่มีหลักฐานแข็ง หรือยังต้องรออนุมัติจากหน่วยงานภายนอก</td></tr>
<tr><td>1</td><td>ไม่พบตัวจุดประกายที่ระบุปี 2027</td></tr>
</table>
<p>หัก 1 คะแนนถ้ามีหลักฐานค้านที่บริษัทเปิดเผยเอง ซึ่งทำให้ตัวจุดประกายอาจไม่เกิดหรือเลื่อนออกไป</p>
<h2>ขนาด Catalyst</h2>
<p>ขนาดของสิ่งที่ตัวจุดประกายจะเพิ่มให้ คิดเป็น % ของฐานเดิมของบริษัท คำนวณจากตัวเลขในเอกสารเท่านั้น แต่ละตัวเทียบกับฐานต่างกันตามธุรกิจ แบ่งเป็น 5 กลุ่มคือ รายได้/ยอดขาย · สินทรัพย์รวม · จำนวนหน่วยที่สร้างรายได้ (ห้อง เตียง MW เครื่องบิน สาขา) · กำไร/EBITDA/ปันผล · ความคืบหน้าโครงการ เทียบขนาดกันได้เฉพาะในกลุ่มเดียวกัน ไม่ควรเทียบข้ามกลุ่ม กลุ่มกำไรและความคืบหน้าวัดสิ่งอื่นที่ไม่ใช่ขนาดของ Catalyst โดยตรง ตัวที่เอกสารไม่มีตัวเลขพอจะเว้นว่าง ตัวเลขนี้ไม่ได้มาจากผลประกอบการย้อนหลัง</p>
<p>ตัวเลขนี้เป็นเพียงตัวบอกขนาดคร่าว ๆ (scale proxy) ไม่ใช่รายได้หรือกำไรที่จะเพิ่มขึ้น เช่น MSFT เทียบรายได้ตามสัญญาที่รอรับรู้ภายใน 12 เดือนกับรายได้ทั้งปีที่ผ่านมา ซึ่งไม่ได้บอกว่ารายได้จะโต 61% และไม่ได้บอกผลต่อกำไรต่อหุ้นหรือกระแสเงินสด</p>
</section>
<footer id="foot"></footer>
</main>
<script id="data" type="application/json">__DATA__</script>
<script>
const EMBEDDED = JSON.parse(document.getElementById('data').textContent);

// หุ้นหนึ่งตัวใน data.json ซ้อนหลักฐานไว้ใน evidence: แปลงเป็นรายการแบนที่ UI ใช้ และนับหนุน/ค้านเอง
function shape(stocks, sources, built) {
  const evidence = [];
  const flat = stocks.map(s => {
    const ev = s.evidence || [];
    ev.forEach(e => evidence.push({ticker: s.ticker, ...e}));
    const n = sig => ev.filter(e => e.signal === sig).length;
    return {...s, theme: s.themes.join('|'),
      catalyst_size_pct: s.catalyst_size_pct ?? '', catalyst_size_basis: s.catalyst_size_basis ?? '',
      catalyst_size_type: s.catalyst_size_type ?? '',
      support_count: n('support'), challenge_count: n('challenge')};
  });
  return {stocks: flat, evidence, sources, built};
}

// เปิดผ่านเว็บ: ดึงไฟล์ล่าสุด · เปิดจากไฟล์ในเครื่อง (fetch ถูกบล็อก) หรือโหลดไม่ได้: ใช้สำเนาที่ฝังไว้
async function loadData() {
  try {
    const get = u => fetch(u, {cache: 'no-cache'}).then(r => { if (!r.ok) throw new Error(r.status); return r.json(); });
    const [d, all] = await Promise.all([get('data.json'), get('../data/sources.json')]);
    const used = new Set(d.stocks.flatMap(s => s.evidence.map(e => e.doc_id)));
    const sources = {};
    all.filter(x => used.has(x.doc_id)).forEach(x => sources[x.doc_id] = {title: x.title, url: x.url, doc_type: x.doc_type, doc_date: x.doc_date});
    return {...shape(d.stocks, sources, ''), live: true};
  } catch (err) {
    return {...shape(EMBEDDED.stocks, EMBEDDED.sources, EMBEDDED.built), live: false};
  }
}

// ปุ่ม i: ชี้หรือโฟกัสแล้วแสดงเอง · กดเพื่อค้างไว้ (มือถือไม่มี hover) · Esc หรือกดที่อื่นเพื่อปิด
const tip = document.getElementById('tip'), tipBtn = document.getElementById('tip-btn');
const setTip = open => { tip.classList.toggle('open', open); tipBtn.setAttribute('aria-expanded', open); };
tipBtn.onclick = () => setTip(!tip.classList.contains('open'));
document.addEventListener('click', e => { if (!tip.contains(e.target)) setTip(false); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') { setTip(false); tipBtn.blur(); } });

let D, byTicker;
loadData().then(d => { D = d; start(); });

const SIG = {support:'หนุน', challenge:'ค้าน', neutral:'กลาง'};
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const order = {support:0, challenge:1, neutral:2};

const ALL = 'ทั้งหมด';
const NONE = 'คำนวณไม่ได้';
const state = {tier: ALL, theme: ALL, score: ALL, type: ALL, sort: 'desc'};
const TIERS = {T1: 'ติด Watchlist', T2: 'รอข้อมูล', T3: 'ยังไม่ติด'};
const tierCount = t => D.stocks.filter(s => s.tier === t).length;

// สร้างปุ่มกลุ่มหนึ่ง: options = [[ค่า, ข้อความ, ปิดใช้ไหม]]
function chips(id, key, options) {
  const box = document.getElementById(id);
  options.forEach(([value, label, disabled]) => {
    const b = document.createElement('button');
    b.textContent = label; b.disabled = !!disabled;
    b.setAttribute('aria-pressed', state[key] === value);
    b.onclick = () => {
      state[key] = value;
      [...box.children].forEach(x => x.setAttribute('aria-pressed', x === b));
      render();
    };
    box.appendChild(b);
  });
}
const scoreCount = n => D.stocks.filter(s => +s.evidence_score === n).length;
// หุ้นหนึ่งตัวอยู่ได้หลายธีม (themes เป็นรายการใน data.json)
const themesOf = s => s.theme.split('|');
const size = s => s.catalyst_size_pct === '' ? null : +s.catalyst_size_pct;
// ประเภทฐานที่ใช้เทียบ (ชุดเดียวกับ SIZE_TYPES ใน build_site.py) · ฐานจริงของแต่ละตัวอยู่ในข้อความ catalyst_size_basis
const TYPES = {
  revenue: 'รายได้ / ยอดขาย', assets: 'สินทรัพย์รวม',
  units_rooms: 'หน่วย: ห้องพัก', units_beds: 'หน่วย: เตียง', units_mw: 'หน่วย: กำลังผลิต (MW)',
  units_aircraft: 'หน่วย: เครื่องบิน / ที่นั่ง', units_sites: 'หน่วย: จำนวนสาขา',
  profit: 'กำไร / EBITDA / ปันผล', progress: 'ความคืบหน้าโครงการ'};
const TYPE_HINT = {
  revenue: 'ช่วงเวลาของฐานต่างกัน (ทั้งปี ไตรมาส ครึ่งปี) ดูฐานของแต่ละตัวก่อนเทียบ',
  profit: 'ไม่ใช่ขนาดของ Catalyst โดยตรง วัดผลต่อกำไรหรือผู้ถือหุ้น เทียบกับกลุ่มอื่นไม่ได้',
  progress: 'ไม่ใช่ขนาดของ Catalyst วัดว่าโครงการคืบหน้าไปแค่ไหน เทียบกับกลุ่มอื่นไม่ได้'};
const typeOf = s => size(s) === null ? NONE : s.catalyst_size_type;
const typeLabel = t => t === NONE ? NONE : TYPES[t] || t;
const typeCount = t => D.stocks.filter(s => typeOf(s) === t).length;

// สร้างปุ่มตัวกรองจากข้อมูล เรียกครั้งเดียวหลังโหลดข้อมูลเสร็จ
function start() {
  byTicker = {};
  D.evidence.forEach(e => (byTicker[e.ticker] ||= []).push(e));
  chips('f-tier', 'tier', [[ALL, ALL], ...Object.entries(TIERS).map(([t, label]) => [t, `${t} · ${label} · ${tierCount(t)} ตัว`, !tierCount(t)])]);
  chips('f-theme', 'theme', [[ALL, ALL], ...[...new Set(D.stocks.flatMap(themesOf))].map(t => [t, t])]);
  chips('f-score', 'score', [[ALL, ALL], ...[5, 4, 3, 2, 1].map(n => [n, `${n} คะแนน · ${scoreCount(n)} ตัว`, !scoreCount(n)])]);
  chips('f-sort', 'sort', [['desc', 'คะแนนมาก → น้อย'], ['asc', 'คะแนนน้อย → มาก'], ['size', 'ขนาด Catalyst มาก → น้อย']]);
  chips('f-basis', 'type', [[ALL, ALL], ...[...Object.keys(TYPES), NONE].map(t => [t, `${typeLabel(t)} · ${typeCount(t)} ตัว`, !typeCount(t)])]);
  document.getElementById('tip-sum').textContent =
    'รวบรวมหุ้นไทยและสหรัฐที่มีตัวจุดประกายปี 2027 พร้อมหลักฐานจากเอกสารที่บริษัทยื่นเอง (SEC EDGAR และ ก.ล.ต. iDisc) ' +
    'กดย้อนไปเอกสารต้นทางได้ทุกแถว แต่ละตัวมีคะแนนความแน่นของหลักฐาน 1–5 เงื่อนไขตัดทิ้ง ขนาด Catalyst เทียบกับบริษัท ' +
    'และระดับ Watchlist (T1 ติด Watchlist · T2 รอข้อมูล · T3 ยังไม่ติด)';
  render();
  document.getElementById('sub').textContent = `หุ้นไทย + สหรัฐ ${D.stocks.length} ตัว · ตัวจุดประกายปี 2027 จากเอกสารที่บริษัทยื่นเอง`;
  document.getElementById('foot').textContent =
    `ข้อมูลจาก output/data.json และ data/sources.json${D.live ? '' : ' (สำเนาที่ฝังไว้ สร้างเมื่อ ' + D.built + ')'} · ` +
    `หุ้น ${D.stocks.length} ตัว · หลักฐาน ${D.evidence.length} แถว · เอกสารที่อ้างถึง ${Object.keys(D.sources).length} ฉบับ`;
}
// แถวขนาด Catalyst ในการ์ด: ตัวเลขเด่น + ฐานที่เทียบ + ป้ายกลุ่ม (กลุ่มกำไรและความคืบหน้าติดป้ายเตือนว่าไม่ใช่ขนาดโดยตรง)
const sizeRow = s => size(s) === null
  ? '<div class="size none"><span class="lab">ขนาด Catalyst</span><span>คำนวณไม่ได้ ดูเหตุผลในรายละเอียด</span></div>'
  : `<div class="size"><span class="lab">ขนาด Catalyst</span><span class="pct">${esc(s.catalyst_size_pct)}%</span>
      <span class="of">${esc(s.catalyst_size_basis)}</span><span class="tag neutral">${esc(typeLabel(s.catalyst_size_type))}</span>
      ${TYPE_HINT[s.catalyst_size_type] && s.catalyst_size_type !== 'revenue' ? '<span class="tag challenge">ไม่ใช่ขนาดโดยตรง</span>' : ''}</div>`;

function evItem(e) {
  const s = D.sources[e.doc_id] || {};
  const link = s.url ? `<a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title || e.doc_id)}</a>` : esc(e.doc_id);
  return `<li><span class="tag ${e.signal}">${SIG[e.signal] || e.signal}</span>${esc(e.finding)}
    <div class="src">${esc(e.evidence_id)} · ${link} · ${esc(e.location)} · เอกสารลงวันที่ ${esc(e.doc_date)} · ดึงข้อมูล ${esc(e.fetched_at)}</div>
    ${e.note ? `<div class="evnote">หมายเหตุ: ${esc(e.note)}</div>` : ''}</li>`;
}

function render() {
  const dir = state.sort === 'asc' ? 1 : -1;
  // เรียงตามขนาด: ตัวที่คำนวณไม่ได้อยู่ท้ายเสมอ
  const bySize = (a, b) => (size(a) === null) - (size(b) === null) || (size(b) ?? 0) - (size(a) ?? 0);
  const rows = D.stocks
    .filter(s => state.tier === ALL || s.tier === state.tier)
    .filter(s => state.theme === ALL || themesOf(s).includes(state.theme))
    .filter(s => state.score === ALL || +s.evidence_score === state.score)
    .filter(s => state.type === ALL || typeOf(s) === state.type)
    .sort((a, b) => (state.sort === 'size' ? bySize(a, b) : dir * (a.evidence_score - b.evidence_score))
      || a.ticker.localeCompare(b.ticker));
  document.getElementById('count').textContent = `แสดง ${rows.length} จาก ${D.stocks.length} ตัว` +
    (state.sort === 'size' ? ' · แยกกลุ่มตามฐานที่ใช้เทียบ เทียบขนาดกันได้เฉพาะในกลุ่มเดียวกัน' : '');
  if (!rows.length) {
    document.getElementById('list').innerHTML = '<div class="empty">ไม่มีหุ้นที่ตรงกับตัวกรองนี้ ลองเลือกธีมหรือคะแนนอื่น</div>';
    return;
  }
  document.getElementById('list').innerHTML = state.sort === 'size' ? grouped(rows) : rows.map(card).join('');
  document.querySelectorAll('.head').forEach(h => h.onclick = () => {
    const a = h.parentElement.classList.toggle('open'); h.setAttribute('aria-expanded', a);
  });
}

// ตอนเรียงตามขนาด: แยกกลุ่มตามฐาน กลุ่มที่มีหลายตัวขึ้นก่อน กลุ่มคำนวณไม่ได้อยู่ท้าย
function grouped(rows) {
  const groups = {};
  rows.forEach(s => (groups[typeOf(s)] ||= []).push(s));
  const keys = Object.keys(groups).sort((a, b) =>
    (a === NONE) - (b === NONE) || groups[b].length - groups[a].length || a.localeCompare(b));
  return keys.map(k => {
    const n = groups[k].length;
    const hint = k === NONE ? 'เอกสารไม่มีตัวเลขพอให้คำนวณ ดูเหตุผลในรายละเอียดของแต่ละตัว'
      : n === 1 ? 'มีตัวเดียวในกลุ่มนี้ จึงไม่มีตัวให้เทียบ' : (TYPE_HINT[k] || 'เทียบขนาดกันได้ในกลุ่มนี้');
    return `<h3 class="grp">${k === NONE ? NONE : 'เทียบกับ ' + esc(typeLabel(k))} · ${n} ตัว<small>${hint}</small></h3>` +
      groups[k].map(card).join('');
  }).join('');
}

function card(s) {
    const n = +s.evidence_score;
    const ev = (byTicker[s.ticker] || []).sort((a, b) => order[a.signal] - order[b.signal]);
    // เอกสารไม่ซ้ำที่หลักฐานของหุ้นนี้อ้างถึง (หลายหลักฐานมักอ้างเอกสารฉบับเดียวกัน)
    const docIds = [...new Set(ev.map(e => e.doc_id))];
    const docLinks = docIds.map(id => {
      const d = D.sources[id] || {};
      const label = esc(d.title || id);
      const a = d.url ? `<a href="${esc(d.url)}" target="_blank" rel="noopener">${label}</a>` : label;
      return `<li>${a} · ${esc(d.doc_type || '')} · ยื่น ${esc(d.doc_date || '')}</li>`;
    }).join('');
    return `<article class="stock" id="s-${esc(s.ticker)}">
      <button class="head" aria-expanded="false">
        <div class="tk">${esc(s.ticker)}<small>${s.market === 'TH' ? 'ไทย' : 'สหรัฐ'} · ${themesOf(s).map(esc).join(' + ')}</small>${s.status.startsWith('ตัวสำรอง') ? '<span class="tag neutral">ตัวสำรอง</span>' : ''}<span class="tag tier ${s.tier === 'T1' ? 'support' : 'neutral'}" title="${esc(TIERS[s.tier])}">${esc(s.tier)}</span></div>
        <div class="cat"><b>${esc(s.catalyst)}</b><span>${esc(s.catalyst_timing)}</span>${sizeRow(s)}</div>
        <div class="score"><div class="dots" aria-label="คะแนน ${n} จาก 5">${'●'.repeat(n)}${'○'.repeat(5 - n)}</div>
          <small>${n}/5 · หนุน ${esc(s.support_count)} · ค้าน ${esc(s.challenge_count)} · จาก ${docIds.length} เอกสาร</small></div>
      </button>
      <div class="body">
        <dl class="meta">
          <div><dt>เงื่อนไขตัดทิ้ง</dt><dd>${esc(s.rejection_condition)}</dd></div>
          <div><dt>Watchlist</dt><dd><b>${esc(s.tier)} · ${esc(TIERS[s.tier])}</b><br>${esc(s.tier_reason)}</dd></div>
          <div><dt>สถานะ</dt><dd>${esc(s.status)}</dd></div>
          <div style="grid-column:1/-1"><dt>เหตุผลของคะแนน</dt><dd>${esc(s.note)}</dd></div>
          <div style="grid-column:1/-1"><dt>ขนาด Catalyst: วิธีคำนวณ</dt><dd>${esc(s.catalyst_size_formula)}<br><small class="evnote">เป็นสัดส่วนต่อฐานเดิม ไม่ใช่กำไรหรือรายได้ที่จะเพิ่มขึ้น เทียบขนาดกันได้เฉพาะในกลุ่มฐานเดียวกัน</small></dd></div>
        </dl>
        <div class="docs"><b>เอกสารต้นทาง (${docIds.length} ฉบับ)</b><ul>${docLinks}</ul></div>
        <ul class="ev">${ev.map(evItem).join('')}</ul>
      </div></article>`;
}
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
