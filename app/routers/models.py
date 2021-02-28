from pydantic import BaseModel
from typing import List

class Result(BaseModel):
    id: str
    name: str
    tags: List[str]
    submitted_at: str
