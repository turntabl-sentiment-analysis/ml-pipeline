from typing import Dict, List
from kedro_project.src.rest_service.models.ttlabs_sentiment_model import ModelPredictionResponse
from kedro_project.src.rest_service.models.enums.sentiment_label import SentimentLabel
from kedro_project.src.rest_service.models.enums.python_sentiment_label import PythonSentimentType
from kedro_project.src.rest_service.models.enums.sentiment_type import SentimentType
from pydantic import BaseModel


class PythonModelOutputRequest(BaseModel):
    text: str
    sentiment_type: List[str]


class PythonModelOutputResponse(BaseModel):
    sentiment_analysis_response: Dict[str, float]
    TTLABS_POLARITY : str
   

