import pandas as pd
import os
from data_loader import DataLoader
from sentiment_analyzer import SentimentAnalyzer
from correlation_calculator import CorrelationCalculator
from visualization import StockVisualizer

def analyze_stock(stock_symbol, ratings_df):
    """Complete analysis for a single stock"""
    print(f"\n{'='*60}")
    print(f"📈 ANALYZING: {stock_symbol}")
    print(f"{'='*60}")
    
    # Initialize components
    loader = DataLoader()
    sentiment_analyzer = SentimentAnalyzer()
    correlation_calculator = CorrelationCalculator()
    visualizer = StockVisualizer()
    
    try:
        # 1. Load stock data
        stock_df = loader.load_stock_data(stock_symbol)
        if stock_df is None:
            return None
        
        # 2. Filter ratings for this stock
        if 'stock' in ratings_df.columns:
            stock_ratings = ratings_df[ratings_df['stock'].str.upper() == stock_symbol.upper()].copy()
            if len(stock_ratings) == 0:
                print(f"⚠ No specific ratings for {stock_symbol}, using all ratings")
                stock_ratings = ratings_df.copy()
        else:
            stock_ratings = ratings_df.copy()
        
        print(f"📰 Using {len(stock_ratings)} ratings for analysis")
        
        # 3. Align dates
        news_aligned, stock_aligned = loader.align_dates(stock_ratings, stock_df)
        if len(news_aligned) == 0 or len(stock_aligned) == 0:
            print("❌ No overlapping dates")
            return None
        
        # 4. Calculate returns
        stock_with_returns = correlation_calculator.calculate_daily_returns(stock_aligned)
        
        # 5. Sentiment analysis
        news_with_sentiment = sentiment_analyzer.analyze_dataframe(news_aligned)
        daily_sentiment = sentiment_analyzer.aggregate_daily_sentiment(news_with_sentiment)
        
        # 6. Combine data
        combined_data = pd.merge(daily_sentiment, stock_with_returns, on='date', how='inner')
        if len(combined_data) < 5:
            print(f"⚠ Insufficient combined data: {len(combined_data)} days")
            return None
        
        # 7. Calculate correlations
        results = correlation_calculator.calculate_correlations(combined_data)
        if results:
            correlation_calculator.print_results(results, stock_symbol)
        
        # 8. Create visualizations
        visualizer.create_dashboard(combined_data, stock_symbol)
        
        # 9. Save results
        results_dir = "./results"
        os.makedirs(results_dir, exist_ok=True)
        combined_data.to_csv(os.path.join(results_dir, f"{stock_symbol}_results.csv"), index=False)
        print(f"💾 Results saved: {stock_symbol}_results.csv")
        
        return {
            'combined_data': combined_data,
            'correlation_results': results
        }
        
    except Exception as e:
        print(f"❌ Error analyzing {stock_symbol}: {e}")
        return None

def main():
    """Main analysis pipeline"""
    print("🚀 Starting Correlation Analysis: News Sentiment vs Stock Movements")
    print("=" * 70)
    
    # Initialize data loader
    loader = DataLoader()
    
    # Load analyst ratings
    ratings_df = loader.load_analyst_ratings()
    if ratings_df is None:
        print("❌ Failed to load analyst ratings")
        return
    
    # Stocks to analyze
    stocks = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA']
    
    all_results = {}
    
    # Analyze each stock
    for stock in stocks:
        result = analyze_stock(stock, ratings_df)
        if result:
            all_results[stock] = result
    
    # Summary
    print(f"\n🎉 ANALYSIS COMPLETED!")
    print(f"✅ Successful: {len(all_results)} stocks")
    print(f"📊 Results saved in './results/' folder")
    
    return all_results

if __name__ == "__main__":
    results = main()