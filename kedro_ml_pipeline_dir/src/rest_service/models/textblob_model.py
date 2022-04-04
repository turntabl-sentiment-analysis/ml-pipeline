from rest_service.models.enums.sentiment_label import SentimentLabel
from rest_service.models.enums.sentiment_type import SentimentType
from pydantic import BaseModel
from typing import List, Dict


class TextBlobOutputRequest(BaseModel):
    text: str
    sentiment_type: List[SentimentType]


class TextBlobOutputResponse(BaseModel):
    sentiment_response: Dict[SentimentType, float]
    sentiment_label: SentimentLabel
