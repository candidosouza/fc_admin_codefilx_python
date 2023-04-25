

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True, slots=True)
class CategoryOutput:
    id: str
    name: str
    description: Optional[str]
    is_active: Optional[bool]
    created_at: datetime
