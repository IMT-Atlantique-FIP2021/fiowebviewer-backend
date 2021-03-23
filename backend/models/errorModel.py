from pydantic import BaseModel


class ErrorDetail(BaseModel):
    message: str
    debug: str
