from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Observation:
    date: date
    observation: str
    color: str
    baby: bool
    peak_indication: Optional[str] = None
    frequency: Optional[str] = None
    code: Optional[str] = None
    comment: Optional[str] = None
