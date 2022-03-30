from enum import Enum


class SentimentLabel(str,Enum):
    negative = "NEGATIVE"
    positive = "POSITIVE"
    neutral = "NEUTRAL"