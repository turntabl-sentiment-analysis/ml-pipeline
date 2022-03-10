from pydantic import BaseModel


class ModelOutputRequest(BaseModel):
    model: str
    text: str


class ModelOutputResponse(BaseModel):
    model: str
    score: int
