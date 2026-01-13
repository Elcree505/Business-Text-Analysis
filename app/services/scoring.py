def to_score_and_label(rule_score: int):
    # clamp into [-5, 8] then map to [0,1]
    s = max(-5, min(8, rule_score))
    value_score = (s + 5) / 13

    if value_score >= 0.70:
        label = "high"
    elif value_score >= 0.40:
        label = "medium"
    else:
        label = "low"

    return float(value_score), label
