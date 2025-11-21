import matplotlib.pyplot as plt

def plot_moving_averages(df, ticker):
    plt.figure(figsize=(14,6))
    plt.plot(df['Close'], label='Close Price')
    plt.plot(df['SMA_20'], label='SMA 20')
    plt.plot(df['EMA_20'], label='EMA 20')
    plt.title(f"{ticker} Stock Price with Moving Averages")
    plt.legend()
    plt.show()

def plot_rsi(df, ticker):
    plt.figure(figsize=(14,4))
    plt.plot(df['RSI'], label='RSI')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title(f"{ticker} RSI Indicator")
    plt.legend()
    plt.show()

def plot_macd(df, ticker):
    plt.figure(figsize=(14,4))
    plt.plot(df['MACD'], label='MACD')
    plt.plot(df['MACD_signal'], label='Signal')
    plt.bar(df.index, df['MACD_hist'], label='Histogram', color='grey')
    plt.title(f"{ticker} MACD Indicator")
    plt.legend()
    plt.show()
