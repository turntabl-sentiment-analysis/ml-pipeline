from enum import Enum


class SentimentType(str, Enum):
    POLARITY = "POLARITY"
    SUBJECTIVITY = "SUBJECTIVITY"