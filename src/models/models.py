from pydantic import BaseModel
from enum import Enum
from typing import List, Dict


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
    sentiment_type: List[SentimentType]



class TextBlobOutputResponse(BaseModel):
    sentiment_response: Dict[SentimentType,float]
