import logging
from typing import Dict, Tuple
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from sklearn.svm import SVC



def split_data(preprocess_dataset: pd.DataFrame, parameters: Dict) -> Tuple:
    tokenizer = Tokenizer(num_words=2000, split=' ')
    tokenizer.fit_on_texts(preprocess_dataset['text'].values)
    X = tokenizer.texts_to_sequences(preprocess_dataset['text'].values)
    X = pad_sequences(X, 28)
    Y = pd.get_dummies(preprocess_dataset['sentiment']).values
    X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size=parameters["test_size"], random_state=parameters["random_state"])
    return X_train, X_test, y_train, y_test


def train_model(preprocess_dataset:pd.DataFrame) -> Sequential:
    model = Sequential()
    tokenizer = Tokenizer(num_words=2000, split=' ')
    tokenizer.fit_on_texts(preprocess_dataset['text'].values)
    X = tokenizer.texts_to_sequences(preprocess_dataset['text'].values)
    X = pad_sequences(X, 28)
    model.add(Embedding(2000, 128, input_length=X.shape[1]))
    model.add(SpatialDropout1D(0.4))
    model.add(LSTM(196, dropout=0.3, recurrent_dropout=0.2, return_sequences=True))
    model.add(LSTM(128, recurrent_dropout=0.2))
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    Y = pd.get_dummies(preprocess_dataset['sentiment']).values
    X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size=0.2)
    model.fit(X_train, y_train, epochs=10, batch_size=512, validation_data=(X_test, y_test))
    return model



