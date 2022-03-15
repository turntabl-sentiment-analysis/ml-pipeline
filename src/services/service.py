import random
from src.models.models import ModelOutputRequest, ModelOutputResponse, TextBlobOutputRequest, TextBlobOutputResponse
from textblob import TextBlob


def get_model_output(body: ModelOutputRequest):
    model = body.model
    score = random.uniform(0, 100)
    return ModelOutputResponse(model=model, score=score)


def get_textblob_output(body: TextBlobOutputRequest):
    blob = TextBlob(body.text)
    score = check_sentiment_type(blob, body)
    return TextBlobOutputResponse(score=score, text=body.text, sentiment=body.sentiment)


def check_sentiment_type(blob, body):
    score = 0
    if body.sentiment == "polarity":
        for sentence in blob.sentences:
            score = sentence.sentiment.polarity
    else:
        for sentence in blob.sentences:
            score = sentence.sentiment.subjectivity
    return score
