import json

import requests


def test_get_sentiment_check_status_code_equals_200():
    body = {"model": "TextBlob", "text": "I am happy"}
    response = requests.post(" http://127.0.0.1:5000/sentiment/sentiment-score", data=json.dumps(body),
                             headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
