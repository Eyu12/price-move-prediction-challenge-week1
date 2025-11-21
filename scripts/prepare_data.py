import pandas as pd

def load_and_prepare(file_path):
    """
    Load CSV stock data and prepare it for analysis.
    """
    df = pd.read_csv(file_path)
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df
