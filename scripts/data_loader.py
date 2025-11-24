import pandas as pd
import numpy as np
import os
from datetime import datetime

class DataLoader:
    def __init__(self, data_path=None):
        if data_path is None:
            # Try to find data folder automatically
            self.data_path = self._find_data_folder()
        else:
            self.data_path = data_path
            
        print(f"🔍 Data folder: {os.path.abspath(self.data_path)}")
        
    def _find_data_folder(self):
        """Automatically find the data folder"""
        possible_paths = [
            "./data",
            "../data",
            "data",
            os.path.join(os.path.dirname(__file__), "../data"),
            os.path.join(os.getcwd(), "data")
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                print(f"✅ Found data folder: {os.path.abspath(path)}")
                return path
        
        print("⚠ No data folder found, using ./data")
        return "./data"
    
    def load_stock_data(self, stock_symbol):
        """Load stock data for a specific symbol"""
        file_path = os.path.join(self.data_path, f"{stock_symbol}.csv")
        
        if os.path.exists(file_path):
            try:
                df = pd.read_csv(file_path)
                df.columns = [col.lower() for col in df.columns]
                
                # Find date column
                date_col = self._find_date_column(df)
                if date_col:
                    df = df.rename(columns={date_col: 'date'})
                    df['date'] = pd.to_datetime(df['date'], errors='coerce')
                    df = df.dropna(subset=['date'])
                    # Ensure timezone-naive
                    if df['date'].dt.tz is not None:
                        df['date'] = df['date'].dt.tz_localize(None)
                    df['date'] = df['date'].dt.normalize()
                
                print(f"✅ Loaded {stock_symbol}: {len(df)} records")
                return df
            except Exception as e:
                print(f"❌ Error loading {stock_symbol}: {e}")
                return None
        else:
            print(f"❌ File not found: {file_path}")
            return None
    
    def load_analyst_ratings(self):
        """Load analyst ratings data"""
        file_path = os.path.join(self.data_path, "raw_analyst_ratings.csv")
        
        if os.path.exists(file_path):
            try:
                df = pd.read_csv(file_path)
                df.columns = [col.lower() for col in df.columns]
                
                # Find date column
                date_col = self._find_date_column(df)
                if date_col:
                    df = df.rename(columns={date_col: 'date'})
                    df['date'] = pd.to_datetime(df['date'], errors='coerce')
                    df = df.dropna(subset=['date'])
                    # Ensure timezone-naive
                    if df['date'].dt.tz is not None:
                        df['date'] = df['date'].dt.tz_localize(None)
                    df['date'] = df['date'].dt.normalize()
                
                print(f"✅ Loaded analyst ratings: {len(df)} records")
                return df
            except Exception as e:
                print(f"❌ Error loading analyst ratings: {e}")
                return None
        else:
            print(f"❌ Analyst ratings file not found: {file_path}")
            return None
    
    def _find_date_column(self, df):
        """Find the date column in a dataframe"""
        date_columns = [col for col in df.columns if 'date' in col.lower()]
        return date_columns[0] if date_columns else None
    
    def align_dates(self, news_df, stock_df):
        """Align dates between news and stock data with timezone handling"""
        # Make copies to avoid modifying originals
        news_df = news_df.copy()
        stock_df = stock_df.copy()
        
        print(f"📅 Date alignment started...")
        print(f"   News dates: {news_df['date'].min()} to {news_df['date'].max()} (tz: {'aware' if news_df['date'].dt.tz is not None else 'naive'})")
        print(f"   Stock dates: {stock_df['date'].min()} to {stock_df['date'].max()} (tz: {'aware' if stock_df['date'].dt.tz is not None else 'naive'})")
        
        # Ensure both are timezone-naive for comparison
        if news_df['date'].dt.tz is not None:
            print("   Converting news dates to timezone-naive...")
            news_df['date'] = news_df['date'].dt.tz_localize(None)
        
        if stock_df['date'].dt.tz is not None:
            print("   Converting stock dates to timezone-naive...")
            stock_df['date'] = stock_df['date'].dt.tz_localize(None)
        
        # Normalize dates (remove time component)
        news_df['date'] = news_df['date'].dt.normalize()
        stock_df['date'] = stock_df['date'].dt.normalize()
        
        # Find common date range
        common_start = max(news_df['date'].min(), stock_df['date'].min())
        common_end = min(news_df['date'].max(), stock_df['date'].max())
        
        if common_start > common_end:
            print("❌ No overlapping date range between news and stock data")
            return pd.DataFrame(), pd.DataFrame()
        
        # Filter to common range
        news_aligned = news_df[
            (news_df['date'] >= common_start) & 
            (news_df['date'] <= common_end)
        ].copy()
        
        stock_aligned = stock_df[
            (stock_df['date'] >= common_start) & 
            (stock_df['date'] <= common_end)
        ].copy()
        
        print(f"✅ Date alignment: {common_start} to {common_end}")
        print(f"   News records: {len(news_aligned)}")
        print(f"   Stock records: {len(stock_aligned)}")
        
        return news_aligned, stock_aligned

if __name__ == "__main__":
    loader = DataLoader()
    print("DataLoader initialized")