"""Project pipelines."""
from typing import Dict


from kedro.pipeline import Pipeline, pipeline
from kedro_pipeline.pipelines import data_processing as dp
from  kedro_pipeline.pipelines import kedro_ml_pipeline as kmp
from  kedro_pipeline.pipelines import data_validation as dvp

def register_pipelines() -> Dict[str, Pipeline]:
    data_processing_pipeline = dp.create_pipeline()
    validate_data_pipeline = dvp.create_pipeline()
    ml_pipeline = kmp.create_pipeline()
    

    return {
        "__default__": data_processing_pipeline + validate_data_pipeline + ml_pipeline ,
        "dp": data_processing_pipeline,
        "dvp": validate_data_pipeline,
        "kmp": ml_pipeline,
    }
