import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr

class CorrelationCalculator:
    def __init__(self):
        pass
    
    def calculate_daily_returns(self, stock_df):
        """Calculate daily percentage returns"""
        stock_df = stock_df.sort_values('date')
        
        # Find close price column
        close_col = self._find_close_column(stock_df)
        if not close_col:
            raise ValueError("Could not find closing price column")
        
        stock_df['daily_return'] = stock_df[close_col].pct_change() * 100
        stock_df['daily_return'] = stock_df['daily_return'].replace([np.inf, -np.inf], np.nan)
        
        valid_returns = stock_df['daily_return'].dropna()
        print(f"📈 Daily returns calculated: {len(valid_returns)} valid returns")
        
        return stock_df
    
    def calculate_correlations(self, combined_df):
        """Calculate correlations between sentiment and returns"""
        clean_df = combined_df.dropna(subset=['avg_polarity', 'daily_return', 'avg_vader_compound'])
        
        if len(clean_df) < 2:
            return None
        
        results = {
            'pearson_polarity': pearsonr(clean_df['avg_polarity'], clean_df['daily_return']),
            'pearson_vader': pearsonr(clean_df['avg_vader_compound'], clean_df['daily_return']),
            'spearman_polarity': spearmanr(clean_df['avg_polarity'], clean_df['daily_return']),
            'spearman_vader': spearmanr(clean_df['avg_vader_compound'], clean_df['daily_return'])
        }
        
        # Add positive ratio correlation if available
        if 'positive_ratio' in clean_df.columns:
            results['pearson_positive_ratio'] = pearsonr(clean_df['positive_ratio'], clean_df['daily_return'])
        else:
            results['pearson_positive_ratio'] = [np.nan, np.nan]
        
        return {
            'summary': {
                'total_days': len(clean_df),
                'date_range': f"{clean_df['date'].min()} to {clean_df['date'].max()}"
            },
            'correlations': results
        }
    
    def _find_close_column(self, df):
        """Find the closing price column"""
        close_columns = [col for col in df.columns if 'close' in col.lower()]
        return close_columns[0] if close_columns else None
    
    def print_results(self, results, stock_symbol):
        """Print formatted correlation results"""
        if not results:
            print("❌ No correlation results to display")
            return
        
        print("=" * 60)
        print(f"CORRELATION RESULTS: {stock_symbol}")
        print("=" * 60)
        print(f"Analysis Period: {results['summary']['date_range']}")
        print(f"Total Days Analyzed: {results['summary']['total_days']}")
        
        print("\nPEARSON CORRELATIONS:")
        print("-" * 40)
        self._print_correlation_row("Polarity vs Returns", results['correlations']['pearson_polarity'])
        self._print_correlation_row("VADER vs Returns", results['correlations']['pearson_vader'])
        self._print_correlation_row("Positive Ratio vs Returns", results['correlations']['pearson_positive_ratio'])
        
        print("\nSPEARMAN CORRELATIONS:")
        print("-" * 40)
        self._print_correlation_row("Polarity vs Returns", results['correlations']['spearman_polarity'])
        self._print_correlation_row("VADER vs Returns", results['correlations']['spearman_vader'])
        
        print("\nSignificance: *** p<0.001, ** p<0.01, * p<0.05")
        print("=" * 60)
    
    def _print_correlation_row(self, label, correlation_result):
        """Print a single correlation result row"""
        if pd.isna(correlation_result[0]):
            print(f"{label:<30}: Not available")
        else:
            corr, p_val = correlation_result
            significance = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else ""
            print(f"{label:<30}: {corr:7.4f} (p={p_val:.4f}) {significance}")

if __name__ == "__main__":
    calculator = CorrelationCalculator()
    print("CorrelationCalculator initialized")