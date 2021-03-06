
from multiprocessing.connection import answer_challenge
from tkinter.messagebox import NO
from kedro_project.src.rest_service.models.textblob_model import TextBlobOutputRequest
from kedro_project.src.rest_service.models.ttlabs_sentiment_model import ModelPredictionRequest
from kedro_project.src.rest_service.models.python_service_model import PythonModelOutputResponse
from kedro_project.src.rest_service.models.enums.python_sentiment_label import PythonSentimentType
from kedro_project.src.rest_service.services.textblob_service import get_textblob_output
from kedro_project.src.rest_service.services.ttlabs_sentiment_service import predict
from kedro_project.src.rest_service.models.python_service_model import PythonModelOutputRequest


def get_service_output(pythonrequest:PythonModelOutputRequest):
    textblob_sentiment_type = []
    ttlabs_response = {}
    ttlabs_polarity= " "
    for sentiment_type in pythonrequest.sentiment_type:
        if sentiment_type == "TEXTBLOB_POLARITY":
            textblob_sentiment_type.append("TEXTBLOB_POLARITY")
        if sentiment_type == "TEXTBLOB_SUBJECTIVITY":
            textblob_sentiment_type.append("TEXTBLOB_SUBJECTIVITY")
        if sentiment_type == "TTLABS_POLARITY":
            ttlabs_data={'text':pythonrequest.text}
            ttlabs_request= ModelPredictionRequest(**ttlabs_data)
            ttlabs_result = predict(ttlabs_request)
            ttlabs_polarity = ttlabs_result.sentiment_type
            ttlabs_response= {"TTLABS_POLARITY":ttlabs_result.score}
        
    textblob_data = {"text":pythonrequest.text,"sentiment_type": textblob_sentiment_type}
    textblob_response = get_textblob_output(TextBlobOutputRequest(**textblob_data))
    textblob_response = textblob_response.sentiment_response
    if textblob_response and ttlabs_response:
        sentiment_analysis_response = {**textblob_response,**ttlabs_response}

    elif textblob_response:
       sentiment_analysis_response = textblob_response

    else:
       sentiment_analysis_response = ttlabs_response
  
    return PythonModelOutputResponse(sentiment_analysis_response = sentiment_analysis_response,TTLABS_POLARITY=ttlabs_polarity)
        
        

