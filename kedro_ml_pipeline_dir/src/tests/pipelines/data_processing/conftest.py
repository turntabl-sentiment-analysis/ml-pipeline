import pandas as pd
import  pytest

@pytest.fixture(scope='module')
def basic_data():
    dataset = pd.DataFrame({
        "text": [
            "@happy"
        ]   
         })
    return dataset