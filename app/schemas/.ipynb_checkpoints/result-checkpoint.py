from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class AnalysisResult(BaseModel):
    value_label: str          # low | medium | high
    value_score: float        # 0~1
    reasons: List[str]
    extracted: Optional[Dict[str, Any]] = None
    summary_zh: Optional[str] = None
