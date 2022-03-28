from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data, train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["preprocess_dataset", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),

            node(
                func=train_model,
                inputs=["X_train", "y_train", "preprocess_dataset", "parameters"],
                outputs=None,
                name="model_node",
            ),

        ]
    )