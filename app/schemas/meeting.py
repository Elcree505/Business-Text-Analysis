from pydantic import BaseModel
from typing import Optional

class MeetingInput(BaseModel):
    id: Optional[str] = None
    company_name: Optional[str] = None
    title: str
    description: Optional[str] = ""
    datetime: Optional[str] = None
    location: Optional[str] = None
