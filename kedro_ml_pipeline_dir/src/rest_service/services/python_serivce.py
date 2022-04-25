
from tkinter.messagebox import NO
from rest_service.models.python_service_model import PythonModelOutputResponse
from rest_service.models.enums.python_sentiment_label import PythonSentimentType
from rest_service.services.textblob_service import get_textblob_output
from rest_service.services.ttlabs_sentiment_service import predict
from rest_service.models.python_service_model import PythonModelOutputRequest


def get_service_output(pythonrequest:PythonModelOutputRequest):
    textblob_sentiment_type = []
    result = []
    for sentiment_type in pythonrequest.sentiment_type:
        if sentiment_type.TEXTBLOB_POLARITY:
            textblob_sentiment_type.append("POLARITY")
        if sentiment_type.TEXTBLOB_SUBJECTIVITY:
            textblob_sentiment_type.append("SUBJECTIVITY")
        if sentiment_type.TTLABS_POLARITY:
            result.append(predict(PythonModelOutputRequest(text=pythonrequest.text)))
    result.append(get_textblob_output(pythonrequest.text, textblob_sentiment_type))
    return PythonModelOutputResponse(result=result,textblob_sentiment_type=textblob_sentiment_type)



     
     

        
        

