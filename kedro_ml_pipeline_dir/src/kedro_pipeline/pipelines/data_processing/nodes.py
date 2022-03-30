import pandas as pd
import numpy as np
import spacy as sp
import re


def preprocess_dataset(data: pd.DataFrame) -> pd.DataFrame:
    data['text'] = data['text'].apply(preprocess_data)
    return data

def preprocess_data(text):
    text = text.lower()
    new_text = re.sub('[^a-zA-z0-9\s]','',text)
    new_text = re.sub('rt',"", new_text)
    return new_text
