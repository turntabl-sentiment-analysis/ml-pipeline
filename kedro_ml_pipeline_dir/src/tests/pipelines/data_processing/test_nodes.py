import pandas as pd
import imp, sys, os
from conftest import basic_data
from kedro_ml_pipeline_dir.src.kedro_pipeline.pipelines.data_processing.nodes import preprocess_dataset
import pytest


def test_basic_data():
    dataset = pd.DataFrame({"text": [ "@happy" ]   })
    cleaned_data = preprocess_dataset(dataset)
    assert cleaned_data == "happy"
    




