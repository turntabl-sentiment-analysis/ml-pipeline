import random

from src.models.models import RequestObject, ResponseObject


def get_model_score(body: RequestObject):
    model = body.model
    text = body.text
    score = random.uniform(0, 100)
    return ResponseObject(model=model, text=text, score=score)
