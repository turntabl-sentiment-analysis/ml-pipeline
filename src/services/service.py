import random
from src.models.models import ModelOutputRequest, ModelOutputResponse, TextBlobOutputRequest, TextBlobOutputResponse
from textblob import TextBlob


def get_model_output(body: ModelOutputRequest):
    model = body.model
    score = random.uniform(0, 100)
    return ModelOutputResponse(model=model, score=score)


def get_textblob_output(sentiment_request: TextBlobOutputRequest):
    text_blob_request = TextBlob(sentiment_request.text)
    response_object = check_sentiment_type_and_get_score(text_blob_request,sentiment_request.sentiment_type)
    return TextBlobOutputResponse(sentiment_response=response_object)


def check_sentiment_type_and_get_score(text, list_of_sentiment_type):
    text_blob_sentiment_response = {}
    for sentiment_type in list_of_sentiment_type:
        if sentiment_type == "polarity":
            for sentence in text.sentences:
                score = sentence.sentiment.polarity
                text_blob_sentiment_response["polarity"] = score
        else:
            for sentence in text.sentences:
                score = sentence.sentiment.subjectivity
                text_blob_sentiment_response["subjectivity"] = score
    return text_blob_sentiment_response


