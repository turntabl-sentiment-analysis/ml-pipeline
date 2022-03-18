import logging
from typing import Dict, Tuple
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


def split_data(twitter_sentiment: pd.DataFrame, parameters: Dict) -> Tuple:
    X = twitter_sentiment[parameters['features']]
    y = twitter_sentiment['sentiment_type']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test