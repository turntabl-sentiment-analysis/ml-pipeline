from enum import Enum


class SentimentType(str, Enum):
    polarity = "POLARITY"
    subjectivity = "SUBJECTIVITY"