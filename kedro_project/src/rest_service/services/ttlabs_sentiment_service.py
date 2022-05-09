from posixpath import split
from xml.sax.handler import property_interning_dict
from rest_service.models.enums.sentiment_label import SentimentLabel
from rest_service.models.ttlabs_sentiment_model import ModelPredictionRequest
from rest_service.models.ttlabs_sentiment_model import ModelPredictionResponse
import numpy as np
import pandas as pd
import tensorflow as tf
import re
import os
from keras.preprocessing.text import Tokenizer

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from kedro_pipeline.pipelines.data_processing.nodes import preprocess_data

data1 = pd.read_csv("C://Users//User//Desktop//MainProject//ml-pipeline//kedro_project//src//rest_service//csv_dataset//Sentiment.csv")
tokenizer = Tokenizer(num_words=2000, split=' ')
tokenizer.fit_on_texts(data1['text'].values)


def my_pipeline(text_sentiment):
    text = text_sentiment.lower()
    new_text = re.sub('[^a-zA-z0-9\s]', '', text)
    new_text = re.sub('rt', '', new_text)
    X = tokenizer.texts_to_sequences(pd.Series(new_text).values)
    X = pad_sequences(X, maxlen=28)
    return X


def predict(sentiment_request: ModelPredictionRequest):
  sentiment_type = ""
  clean_text = my_pipeline(sentiment_request.text)
  loaded_model = tf.keras.models.load_model("C://Users//User//Desktop//MainProject//ml-pipeline//kedro_project//src//rest_service//saved_model//sentiment.h5")
  predictions = loaded_model.predict(clean_text)
  sentiment = int(np.argmax(predictions))
  probability = max(predictions.tolist()[0])
  if sentiment == 0:
    sentiment_type = SentimentLabel.NEGATIVE
  if sentiment == 1:
    sentiment_type = SentimentLabel.NEUTRAL
  if sentiment == 2:
    sentiment_type = SentimentLabel.POSITIVE
  return ModelPredictionResponse(sentiment_type = sentiment_type, score = probability)

