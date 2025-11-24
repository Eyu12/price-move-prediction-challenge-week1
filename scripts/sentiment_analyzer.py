import pandas as pd
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of a text using multiple methods"""
        if pd.isna(text) or text == "":
            return {'polarity': 0, 'subjectivity': 0, 'vader_compound': 0}
        
        # TextBlob analysis
        blob = TextBlob(str(text))
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # VADER analysis
        vader_scores = self.sia.polarity_scores(str(text))
        
        return {
            'polarity': polarity,
            'subjectivity': subjectivity,
            'vader_compound': vader_scores['compound'],
            'vader_positive': vader_scores['pos'],
            'vader_negative': vader_scores['neg'],
            'vader_neutral': vader_scores['neu']
        }
    
    def analyze_dataframe(self, df, text_column='headline'):
        """Perform sentiment analysis on a dataframe"""
        print("🔍 Performing sentiment analysis...")
        
        # Apply sentiment analysis
        sentiment_results = df[text_column].apply(self.analyze_sentiment)
        
        # Add sentiment columns to dataframe
        df['sentiment_polarity'] = sentiment_results.apply(lambda x: x['polarity'])
        df['sentiment_subjectivity'] = sentiment_results.apply(lambda x: x['subjectivity'])
        df['vader_compound'] = sentiment_results.apply(lambda x: x['vader_compound'])
        
        # Classify sentiment
        df['sentiment_label'] = df['sentiment_polarity'].apply(
            lambda x: 'positive' if x > 0.5 else 'negative' if x < 0.5 else 'neutral'
        )
        
        print("✅ Sentiment analysis completed")
        print(f"Sentiment distribution:\n{df['sentiment_label'].value_counts()}")
        
        return df
    
    def aggregate_daily_sentiment(self, df):
        """Aggregate sentiment scores by date"""
        daily_sentiment = df.groupby('date').agg({
            'sentiment_polarity': ['mean', 'std', 'count'],
            'vader_compound': ['mean', 'std'],
            'sentiment_label': lambda x: (x == 'positive').sum() / len(x) if len(x) > 0 else 0
        }).round(4)
        
        # Flatten column names
        daily_sentiment.columns = [
            'avg_polarity', 'std_polarity', 'article_count',
            'avg_vader_compound', 'std_vader_compound',
            'positive_ratio'
        ]
        
        daily_sentiment = daily_sentiment.reset_index()
        print(f"📊 Aggregated sentiment for {len(daily_sentiment)} days")
        
        return daily_sentiment

if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    print("SentimentAnalyzer initialized")