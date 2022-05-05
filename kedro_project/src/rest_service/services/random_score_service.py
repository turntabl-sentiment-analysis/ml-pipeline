import random
from rest_service.models.random_score_model import ModelOutputRequest, ModelOutputResponse


def get_model_output(body: ModelOutputRequest):
    model = body.model
    score = random.uniform(0, 100)
    return ModelOutputResponse(model=model, score=score)