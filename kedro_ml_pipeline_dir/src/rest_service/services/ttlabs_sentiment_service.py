from posixpath import split
from xml.sax.handler import property_interning_dict
from rest_service.models.ttlabs_sentiment_model import ModelPredictionRequest
from rest_service.models.ttlabs_sentiment_model import ModelPredictionResponse
import numpy as np
import  pandas as pd
import tensorflow as tf
import re
import os
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from kedro_pipeline.pipelines.data_processing.nodes import preprocess_data


data1 = pd.read_csv("C:\\Users\\User\\Desktop\\MainProject\\ml-pipeline\\kedro_ml_pipeline_dir\\data\\01_raw\\Sentiment.csv")
tokenizer = Tokenizer(num_words=2000, split=' ')
tokenizer.fit_on_texts(data1['text'].values)

def my_pipeline(text_sentiment):
  text = text_sentiment.lower()
  new_text = re.sub('[^a-zA-z0-9\s]','',text)
  new_text = re.sub('rt','',new_text)
  X = tokenizer.texts_to_sequences(pd.Series(new_text).values)
  X = pad_sequences(X,maxlen=28)
  return X


def predict(sentiment_request: ModelPredictionRequest):
  response = {}
  clean_text = my_pipeline(sentiment_request.text_sentiment)
  loaded_model = tf.keras.models.load_model("C:\\Users\\User\\Desktop\\MainProject\\ml-pipeline\\kedro_ml_pipeline_dir\\src\\rest_service\\services\\sentiment.h5")
  predictions = loaded_model.predict(clean_text)
  pred = predictions.tolist()[0]
  for value in sentiment_request.ttlab_sentiment_type:
    if value == "POSITIVE":
      response["POSITIVE"] = pred[2]
    elif value == "NEUTRAL":
      response["NEUTRAL"] = pred[1]
    else:
      response["NEGATIVE"] = pred[0]
  return ModelPredictionResponse(sentiment_response = response)