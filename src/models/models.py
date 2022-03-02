from pydantic import BaseModel


class RequestObject(BaseModel):
    model: str
    text: str


class ResponseObject(BaseModel):
    model: str
    score: int
