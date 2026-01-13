from services.preprocess import build_full_text
from services.rules import apply_rules
from services.scoring import to_score_and_label

def analyze(title: str, description: str):
    text = build_full_text(title, description)
    r_score, reasons, extracted = apply_rules(text)
    value_score, value_label = to_score_and_label(r_score)

    summary_zh = f"{value_label.upper()}：{title[:30]}"

    return {
        "value_label": value_label,
        "value_score": value_score,
        "reasons": reasons[:6],
        "extracted": extracted,
        "summary_zh": summary_zh
    }
