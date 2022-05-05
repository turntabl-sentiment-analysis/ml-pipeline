from db import db_connection
from rest_service.models.enums.sentiment_type import SentimentType
from rest_service.models.textblob_model import TextBlobOutputRequest, TextBlobOutputResponse
from textblob import TextBlob




def get_textblob_output(sentiment_request: TextBlobOutputRequest):
    text_blob_request = TextBlob(sentiment_request.text)  
    list_sentiment_types= [] 
    for sentiment in sentiment_request.sentiment_type:    
        record = db_connection(sentiment)    
        list_sentiment_types.append(record[0][3])
    response_object = check_sentiment_type_and_get_score(text_blob_request, list_sentiment_types)
    return TextBlobOutputResponse(sentiment_response=response_object)


def check_sentiment_type_and_get_score(text, list_of_sentiment_type):
    text_blob_sentiment_response = {}
    for item in list_of_sentiment_type:
        if item == 'SUBJECTIVITY':
            for sentence in text.sentences:
                score = sentence.sentiment.subjectivity
                text_blob_sentiment_response['SUBJECTIVITY'] = score
        else:
            for sentence in text.sentences:
                score = sentence.sentiment.polarity
                text_blob_sentiment_response['POLARITY'] = score
    return text_blob_sentiment_response


def sentiment_label(score):
    if score > 0:
        return "POSITIVE"
    elif score == 0:
        return "NEUTRAL"
    else:
        return "NEGATIVE"