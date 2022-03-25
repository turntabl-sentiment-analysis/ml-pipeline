import logging
from typing import Dict, Tuple
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.svm import SVC


def split_data(preprocess_dataset: pd.DataFrame, parameters: Dict) -> Tuple:
    tokenizer = Tokenizer(num_words=2000, split=' ')
    tokenizer.fit_on_texts(preprocess_dataset['text'].values)
    X = tokenizer.texts_to_sequences(preprocess_dataset['text'].values)
    X = pad_sequences(X, 28)
    Y = pd.get_dummies(preprocess_dataset['sentiment']).values
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=parameters["test_size"], random_state=parameters["random_state"])
    return X_train, X_test, y_train, y_test

