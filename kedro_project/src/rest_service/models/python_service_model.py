from typing import Dict, List
from rest_service.models.ttlabs_sentiment_model import ModelPredictionResponse
from rest_service.models.enums.sentiment_label import SentimentLabel
from rest_service.models.enums.python_sentiment_label import PythonSentimentType
from rest_service.models.enums.sentiment_type import SentimentType
from pydantic import BaseModel


class PythonModelOutputRequest(BaseModel):
    text: str
    sentiment_type: List[str]


class PythonModelOutputResponse(BaseModel):
    general_response: Dict[str, float]
    TTLABS_POLARITY : str
   

