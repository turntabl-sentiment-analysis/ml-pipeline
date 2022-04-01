from pydantic import BaseModel
from rest_service.models.enums.sentiment_label import SentimentLabel

from typing import Dict, List


class ModelPredictionRequest(BaseModel):
    text_sentiment: str
    ttlab_sentiment_type: List[SentimentLabel]


class ModelPredictionResponse(BaseModel):
    sentiment_response: Dict[SentimentLabel, float]
