"""สร้าง output/index.html จาก output/stocks.csv, output/data.csv และ data/sources.csv

ฝังข้อมูลลงในหน้าเว็บเป็น JSON เพื่อให้เปิดไฟล์ได้ตรง ๆ โดยไม่ต้องมี server
(เบราว์เซอร์ส่วนใหญ่ไม่ยอมให้หน้าที่เปิดจาก file:// อ่านไฟล์ CSV ข้าง ๆ)
แก้ข้อมูลที่ CSV แล้วรันสคริปต์นี้ใหม่ทุกครั้ง อย่าแก้ index.html ตรง ๆ

ใช้: python scripts/build_site.py
"""
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output" / "index.html"


def read(path):
    with open(ROOT / path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    stocks = read("output/stocks.csv")
    evidence = read("output/data.csv")
    used = {e["doc_id"] for e in evidence}
    sources = {s["doc_id"]: {k: s[k] for k in ("title", "url", "doc_type", "doc_date")}
               for s in read("data/sources.csv") if s["doc_id"] in used}
    missing = sorted(used - sources.keys())
    if missing:
        raise SystemExit(f"doc_id ใน data.csv ที่ไม่มีใน sources.csv: {missing}")

    payload = json.dumps({"stocks": stocks, "evidence": evidence, "sources": sources,
                          "built": date.today().isoformat()}, ensure_ascii=False)
    OUT.write_text(TEMPLATE.replace("__DATA__", payload.replace("</", "<\\/")), "utf-8")
    print(f"เขียน {OUT.relative_to(ROOT)} · หุ้น {len(stocks)} ตัว · หลักฐาน {len(evidence)} แถว · เอกสาร {len(sources)} ฉบับ")


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
h1{font-size:26px;margin:0 0 4px}
.sub{color:var(--muted);margin:0 0 16px}
.note{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--acc);border-radius:8px;padding:12px 14px;margin:0 0 20px}
.controls{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 12px}
.controls button{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:6px 12px;cursor:pointer;font:inherit}
.controls button[aria-pressed=true]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.stock{background:var(--card);border:1px solid var(--line);border-radius:10px;margin:0 0 10px;overflow:hidden}
.head{display:grid;grid-template-columns:72px 1fr auto;gap:12px;align-items:center;padding:12px 14px;cursor:pointer;width:100%;border:0;background:none;color:inherit;font:inherit;text-align:left}
.tk{font-weight:700;font-size:17px}
.tk small{display:block;font-weight:400;font-size:12px;color:var(--muted)}
.cat{min-width:0}
.cat b{display:block}
.cat span{color:var(--muted);font-size:13px}
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
.legend{margin-top:28px;font-size:14px}
.legend table{border-collapse:collapse;width:100%;background:var(--card)}
.legend td{border:1px solid var(--line);padding:6px 10px;vertical-align:top}
footer{margin-top:24px;color:var(--muted);font-size:13px}
@media (max-width:560px){.head{grid-template-columns:56px 1fr;}.score{grid-column:1/-1;text-align:left;display:flex;gap:8px;align-items:center}.score small{display:inline}}
</style>
</head>
<body>
<main>
<h1>Catalyst Tracker 2027</h1>
<p class="sub">หุ้นไทย + สหรัฐ 10 ตัว · ตัวจุดประกายปี 2027 จากเอกสารที่บริษัทยื่นเอง</p>
<div class="note"><b>คะแนนวัดความแน่นของหลักฐาน ไม่ใช่การทำนายราคา และไม่ใช่คำแนะนำซื้อหรือขาย</b><br>
กดที่หุ้นเพื่อดูหลักฐานหนุน/ค้านทีละแถว และลิงก์ไปเอกสารต้นทาง ตัวเลขที่ไม่มีในเอกสารเว้นว่างไว้ ไม่ได้เดา</div>
<div class="controls" id="filters"></div>
<div id="list"></div>
<section class="legend">
<h2>เกณฑ์คะแนน (1–5)</h2>
<table>
<tr><td>5</td><td>ตัวจุดประกายมีผลแล้ว หรือมีสัญญาผูกพันกับลูกค้าแล้ว</td></tr>
<tr><td>4</td><td>กำลังสร้างหรือดำเนินการ มีเงินที่จ่ายจริงหรือผูกพันแล้ว และมีวันที่ชัด</td></tr>
<tr><td>3</td><td>แผนของบริษัทที่มีวันที่ในหรือก่อนปี 2027 และมีตัวเลขรองรับบางส่วน</td></tr>
<tr><td>2</td><td>แผนที่ยังไม่มีหลักฐานแข็ง หรือยังต้องรออนุมัติจากหน่วยงานภายนอก</td></tr>
<tr><td>1</td><td>ไม่พบตัวจุดประกายที่ระบุปี 2027</td></tr>
</table>
<p>หัก 1 คะแนนถ้ามีหลักฐานค้านที่บริษัทเปิดเผยเอง ซึ่งทำให้ตัวจุดประกายอาจไม่เกิดหรือเลื่อนออกไป</p>
</section>
<footer id="foot"></footer>
</main>
<script id="data" type="application/json">__DATA__</script>
<script>
const D = JSON.parse(document.getElementById('data').textContent);
const SIG = {support:'หนุน', challenge:'ค้าน', neutral:'กลาง'};
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const byTicker = {};
D.evidence.forEach(e => (byTicker[e.ticker] ||= []).push(e));
const order = {support:0, challenge:1, neutral:2};

const themes = ['ทั้งหมด', ...new Set(D.stocks.map(s => s.theme))];
let theme = 'ทั้งหมด';
const filters = document.getElementById('filters');
themes.forEach(t => {
  const b = document.createElement('button');
  b.textContent = t; b.setAttribute('aria-pressed', t === theme);
  b.onclick = () => { theme = t; [...filters.children].forEach(x => x.setAttribute('aria-pressed', x === b)); render(); };
  filters.appendChild(b);
});

function evItem(e) {
  const s = D.sources[e.doc_id] || {};
  const link = s.url ? `<a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title || e.doc_id)}</a>` : esc(e.doc_id);
  return `<li><span class="tag ${e.signal}">${SIG[e.signal] || e.signal}</span>${esc(e.finding)}
    <div class="src">${esc(e.evidence_id)} · ${link} · ${esc(e.location)} · เอกสารลงวันที่ ${esc(e.doc_date)} · ดึงข้อมูล ${esc(e.fetched_at)}</div>
    ${e.note ? `<div class="evnote">หมายเหตุ: ${esc(e.note)}</div>` : ''}</li>`;
}

function render() {
  const rows = D.stocks.filter(s => theme === 'ทั้งหมด' || s.theme === theme)
    .sort((a, b) => b.evidence_score - a.evidence_score || a.ticker.localeCompare(b.ticker));
  document.getElementById('list').innerHTML = rows.map(s => {
    const n = +s.evidence_score;
    const ev = (byTicker[s.ticker] || []).sort((a, b) => order[a.signal] - order[b.signal]);
    return `<article class="stock" id="s-${esc(s.ticker)}">
      <button class="head" aria-expanded="false">
        <div class="tk">${esc(s.ticker)}<small>${s.market === 'TH' ? 'ไทย' : 'สหรัฐ'} · ${esc(s.theme)}</small></div>
        <div class="cat"><b>${esc(s.catalyst)}</b><span>${esc(s.catalyst_timing)}</span></div>
        <div class="score"><div class="dots" aria-label="คะแนน ${n} จาก 5">${'●'.repeat(n)}${'○'.repeat(5 - n)}</div>
          <small>${n}/5 · หนุน ${esc(s.support_count)} · ค้าน ${esc(s.challenge_count)}</small></div>
      </button>
      <div class="body">
        <dl class="meta">
          <div><dt>เงื่อนไขตัดทิ้ง</dt><dd>${esc(s.rejection_condition)}</dd></div>
          <div><dt>สถานะ</dt><dd>${esc(s.status)}</dd></div>
          <div style="grid-column:1/-1"><dt>เหตุผลของคะแนน</dt><dd>${esc(s.note)}</dd></div>
        </dl>
        <ul class="ev">${ev.map(evItem).join('')}</ul>
      </div></article>`;
  }).join('');
  document.querySelectorAll('.head').forEach(h => h.onclick = () => {
    const a = h.parentElement.classList.toggle('open'); h.setAttribute('aria-expanded', a);
  });
}
render();
document.getElementById('foot').textContent =
  `สร้างจาก output/stocks.csv, output/data.csv และ data/sources.csv เมื่อ ${D.built} · หลักฐาน ${D.evidence.length} แถว จากเอกสาร ${Object.keys(D.sources).length} ฉบับ`;
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
