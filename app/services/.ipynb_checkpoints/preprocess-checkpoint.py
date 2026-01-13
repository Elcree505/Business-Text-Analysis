import re

def normalize_text(s: str) -> str:
    if not s:
        return ""
    s = s.strip()
    s = re.sub(r"\s+", " ", s)
    return s

def build_full_text(title: str, description: str) -> str:
    title = normalize_text(title)
    description = normalize_text(description or "")
    return f"{title}\n{description}".strip()
    