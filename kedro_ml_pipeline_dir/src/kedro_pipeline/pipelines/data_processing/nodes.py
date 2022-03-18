import pandas as pd
import numpy as np

def preprocess_twitter_sentiment_dataset(twitter_sentiment: pd.DataFrame) -> pd.DataFrame:
    twitter_sentiment.rename(columns={"clean_text": "sentiment_text", "category": "sentiment_type"}, inplace=True)
    twitter_sentiment["sentiment_text"].replace('', np.nan, inplace=True)
    twitter_sentiment["sentiment_type"].replace('', np.nan, inplace=True)
    twitter_sentiment.dropna(axis=0, how='any', inplace=True)
    return twitter_sentiment
