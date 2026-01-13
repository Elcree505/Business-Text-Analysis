HIGH_VALUE = ["法人說明會", "法說會", "業績發表會", "財務展望", "營收", "獲利", "指引", "投資人"]
LOW_VALUE  = ["家庭日", "尾牙", "員工活動", "內部訓練", "聯誼", "慶生"]
EXEC_TITLES = ["董事長", "總經理", "執行長", "財務長", "CFO", "CEO"]

def apply_rules(text: str):
    score = 0
    reasons = []
    extracted = {"meeting_type": None, "has_exec": False, "hits_high": [], "hits_low": []}

    if "法人說明會" in text or "法說會" in text:
        extracted["meeting_type"] = "法人說明會"
        score += 3
        reasons.append("會議類型偏投資人溝通（法人說明會）")

    if "業績發表會" in text:
        extracted["meeting_type"] = "業績發表會"
        score += 2
        reasons.append("會議類型為業績發表（常包含營運重點）")

    for kw in HIGH_VALUE:
        if kw in text:
            score += 1
            extracted["hits_high"].append(kw)

    for kw in LOW_VALUE:
        if kw in text:
            score -= 3
            extracted["hits_low"].append(kw)

    for t in EXEC_TITLES:
        if t in text:
            score += 2
            extracted["has_exec"] = True
            reasons.append(f"提到高階主管出席（{t}）")
            break

    if extracted["hits_high"]:
        reasons.append(f"高價值關鍵字：{', '.join(extracted['hits_high'][:5])}")
    if extracted["hits_low"]:
        reasons.append(f"活動性關鍵字：{', '.join(extracted['hits_low'][:5])}")

    return score, reasons, extracted
