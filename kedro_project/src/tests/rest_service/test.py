import unittest
import json
from main import app


class get_sentiment_result_test(unittest.TestCase):

    def __init__(self):
        self.app = None

    def setUp(self):
        self.app = app.test_client()

    def test_successful_sentiment_result(self):
        payload = json.dumps({"model": "TextBlob", "text": "I am happy"})
        response = self.app.post("api/v1/sentiment-analysis",
                                 headers={"Content-Type": "application/json"},
                                 data=payload)

        self.assertEquals(200, response.status_code)
