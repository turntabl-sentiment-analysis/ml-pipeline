import pandas as pd
import great_expectations as ge

def validate_data(preprocess_dataset_new:pd.DataFrame):

    data = ge.from_pandas(preprocess_dataset_new)
    data_validate = data.expect_table_columns_to_match_ordered_list(
        ['sentiment', 'text']
    )

    if not data_validate['success']:
        raise Exception("Sentiment analysis data")
    else:
        print("Passed")
    return data
