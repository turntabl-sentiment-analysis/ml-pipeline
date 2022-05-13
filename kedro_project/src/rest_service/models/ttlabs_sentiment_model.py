from pydantic import BaseModel
from kedro_project.src.rest_service.models.enums.sentiment_label import SentimentLabel

from typing import Dict, List


class ModelPredictionRequest(BaseModel):
    text: str

class ModelPredictionResponse(BaseModel):
    sentiment_type :  str
    score : float
  