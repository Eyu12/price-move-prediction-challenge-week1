def test_data_columns():
    import pandas as pd
    data = pd.read_csv("../data/raw_analyst_ratings.csv")
    assert "headline" in data.columns
    assert "date" in data.columns
