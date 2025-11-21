def test_data_columns():
    import pandas as pd
    data = pd.read_csv("data/news.csv")
    assert "headline" in data.columns
    assert "date" in data.columns
