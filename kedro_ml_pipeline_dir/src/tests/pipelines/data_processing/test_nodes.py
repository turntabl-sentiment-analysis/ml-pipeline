import pandas as pd
import imp, sys, os
from conftest import basic_data
from kedro_ml_pipeline_dir.src.kedro_pipeline.pipelines.data_processing.nodes import preprocess_dataset
import pytest

@pytest.fixture
def basic_data():
    dataset = pd.DataFrame({
        "text": [
            "@happy"
        ]   
         })
    return dataset

class TestCase:
    def test_preprocess_data(self):
        data = basic_data()
        output = preprocess_dataset(data)
        assert output=={"happy"}


