import pandas as pd
from nodes import  preprocess_twitter_sentiment_dataset

def test_preprocess_twitter_sentiment_dataset():
    basic_data = pd.DataFrame({
        "clean_text" : [
            "I am happy",
            "I am sad"
        ],
        "category":[
            1,
            -1
        ]
    })
    output =  preprocess_twitter_sentiment_dataset(basic_data)
    assert output.equals(pd.DataFrame({
        "sentiment_text" : [
            "I am happy",
            "I am sad"
        ],
        "sentiment_type":[
            1,
            -1
        ]
    }))
