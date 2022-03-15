from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_twitter_sentiment_dataset

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_twitter_sentiment_dataset,
                inputs="twitter_sentiment",
                outputs="processed_twitter_sentiment_dataset",
                name="preprocess_twitter_sentiment_node",
            )
        ]
    )
