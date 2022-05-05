"""
This is a boilerplate pipeline 'data_validation'
generated using Kedro 0.17.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from kedro_pipeline.pipelines.data_validation.nodes import validate_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=validate_data,
                inputs="preprocess_dataset_new",
                outputs="preprocess_data_info",
                name="validate_column_node",
            )
        ]
    )