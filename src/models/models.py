from pydantic import BaseModel
from enum import Enum


class SentimentType(str, Enum):
    polarity = "polarity"
    subjectivity = "subjectivity"


class ModelOutputRequest(BaseModel):
    model: str
    text: str


class ModelOutputResponse(BaseModel):
    model: str
    score: int


class TextBlobOutputRequest(BaseModel):
    text: str
    sentiment: SentimentType


class TextBlobOutputResponse(BaseModel):
    sentiment: SentimentType
    text: str
    score: float
