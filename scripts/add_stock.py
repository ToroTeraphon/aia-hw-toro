"""เพิ่มหุ้น 1 ตัวลง output/data.json จากไฟล์ JSON ที่เขียนไว้ (หุ้น + หลักฐาน)

ไฟล์ที่ส่งเข้ามามีช่องเหมือนหุ้นใน data.json แต่ไม่ต้องใส่ status, tier, tier_reason
สคริปต์จะ
  1. ตรวจว่าช่องครบ, doc_id ของหลักฐานทุกแถวมีใน data/sources.json, evidence_id เรียง E001...
  2. คำนวณ tier และ tier_reason ตามเกณฑ์ใน build_site.py (ไม่ต้องกรอกเอง)
  3. เพิ่มหุ้นต่อท้ายรายการ (ถ้า ticker ซ้ำจะหยุด ใช้ --replace ถ้าตั้งใจแทนที่)

ใช้: python scripts/add_stock.py <ไฟล์.json> [--replace]
แล้วรัน python scripts/build_site.py เพื่อสร้างหน้าเว็บใหม่
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_site  # noqa: E402  (ใช้เกณฑ์ tier ที่เดียวกับที่เว็บใช้ตรวจ)

ROOT = build_site.ROOT
DATA = ROOT / "output" / "data.json"
STOCK_KEYS = ["ticker", "market", "themes", "catalyst", "catalyst_timing", "evidence_score",
              "catalyst_size_pct", "catalyst_size_basis", "catalyst_size_formula",
              "rejection_condition", "status", "tier", "tier_reason", "note", "evidence"]
EVIDENCE_KEYS = ["evidence_id", "finding", "signal", "doc_id", "location", "doc_date", "fetched_at", "note"]


def check(stock, sources):
    errors = []
    need = [k for k in STOCK_KEYS if k not in ("status", "tier", "tier_reason")]
    errors += [f"ขาดช่อง {k}" for k in need if k not in stock]
    if errors:
        return errors
    t = stock["ticker"]
    if stock["market"] not in ("US", "TH"):
        errors.append("market ต้องเป็น US หรือ TH")
    if not isinstance(stock["evidence_score"], int) or not 1 <= stock["evidence_score"] <= 5:
        errors.append("evidence_score ต้องเป็นจำนวนเต็ม 1–5")
    if (stock["catalyst_size_pct"] is None) != (stock["catalyst_size_basis"] is None):
        errors.append("catalyst_size_pct และ catalyst_size_basis ต้องเป็น null พร้อมกัน")
    for i, e in enumerate(stock["evidence"], 1):
        miss = [k for k in EVIDENCE_KEYS if k not in e]
        if miss:
            errors.append(f"{t} หลักฐานแถว {i} ขาดช่อง {miss}")
            continue
        if e["evidence_id"] != f"{t}-E{i:03d}":
            errors.append(f"evidence_id แถว {i} ควรเป็น {t}-E{i:03d} แต่เป็น {e['evidence_id']}")
        if e["signal"] not in ("support", "challenge", "neutral"):
            errors.append(f"{e['evidence_id']}: signal ต้องเป็น support/challenge/neutral")
        if e["doc_id"] not in sources:
            errors.append(f"{e['evidence_id']}: doc_id {e['doc_id']} ไม่มีใน sources.json")
    return errors


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    replace = "--replace" in sys.argv
    if len(args) != 1:
        raise SystemExit(__doc__)
    stock = json.loads(Path(args[0]).read_text(encoding="utf-8-sig"))
    sources = {s["doc_id"] for s in json.loads((ROOT / "data" / "sources.json").read_text(encoding="utf-8-sig"))}
    errors = check(stock, sources)
    if errors:
        raise SystemExit("ข้อมูลหุ้นไม่ผ่าน:\n  " + "\n  ".join(errors))

    stock["status"] = stock.get("status") or "พร้อมศึกษาต่อ"
    stock["tier"] = build_site.derive_tier(stock)
    stock["tier_reason"] = build_site.tier_reason(stock)
    ordered = {k: stock[k] for k in STOCK_KEYS}

    data = json.loads(DATA.read_text(encoding="utf-8-sig"))
    existing = [i for i, s in enumerate(data["stocks"]) if s["ticker"] == stock["ticker"]]
    if existing and not replace:
        raise SystemExit(f"{stock['ticker']} มีอยู่แล้วใน data.json (ใช้ --replace ถ้าตั้งใจแทนที่)")
    if existing:
        data["stocks"][existing[0]] = ordered
    else:
        data["stocks"].append(ordered)
    # ไฟล์เดิมไม่มีบรรทัดว่างท้ายไฟล์ รักษารูปแบบเดิมไว้
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{stock['ticker']}: {stock['tier']} · คะแนน {stock['evidence_score']} · หลักฐาน {len(stock['evidence'])} แถว")
    print(stock["tier_reason"])


if __name__ == "__main__":
    main()
