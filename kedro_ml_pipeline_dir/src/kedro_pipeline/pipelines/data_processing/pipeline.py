from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_dataset

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_dataset,
                inputs="data",
                outputs="preprocess_dataset",
                name="preprocess_twitter_sentiment_node",
            ),


        ]
    )
