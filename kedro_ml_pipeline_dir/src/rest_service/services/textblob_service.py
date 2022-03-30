from rest_service.models.textblob_model import TextBlobOutputRequest, TextBlobOutputResponse
from textblob import TextBlob



def get_textblob_output(sentiment_request: TextBlobOutputRequest):
    text_blob_request = TextBlob(sentiment_request.text)
    response_object = check_sentiment_type_and_get_score(text_blob_request, sentiment_request.sentiment_type)
    polarity_score = response_object["POLARITY"]
    label = sentiment_label(polarity_score)
    print(label)

    return TextBlobOutputResponse(sentiment_response=response_object, sentiment_label=label)


def check_sentiment_type_and_get_score(text, list_of_sentiment_type):
    text_blob_sentiment_response = {}
    for sentiment_type in list_of_sentiment_type:
        if sentiment_type == "POLARITY":
            for sentence in text.sentences:
                score = sentence.sentiment.polarity
                text_blob_sentiment_response["POLARITY"] = score
        else:
            for sentence in text.sentences:
                score = sentence.sentiment.subjectivity
                text_blob_sentiment_response["SUBJECTIVITY"] = score
    return text_blob_sentiment_response


def sentiment_label(score):
    if score > 0:
        return "positive"
    elif score == 0:
        return "neutral"
    else:
        return "negative"
