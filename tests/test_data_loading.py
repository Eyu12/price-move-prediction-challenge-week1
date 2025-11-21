import pandas as pd


def test_data_columns():
    data = pd.DataFrame({
        "column_name": [1, 2, 3],
        "other_column": [4, 5, 6]
    })
    assert "column_name" in data.columns
