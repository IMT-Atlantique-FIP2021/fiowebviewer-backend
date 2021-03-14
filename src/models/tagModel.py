from typing import Optional, List

from pydantic import BaseModel, Field


class Tag(BaseModel):
    class Config:
        allow_population_by_field_name = True

    tag_id: Optional[str] = Field(alias="id")
    name: str
