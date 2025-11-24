import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

class StockVisualizer:
    def __init__(self):
        plt.style.use('default')
        # Set better default styles
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.titlesize'] = 12
        plt.rcParams['axes.labelsize'] = 11
    
    def create_dashboard(self, combined_data, stock_symbol, save_dir="./results"):
        """Create comprehensive dashboard for a stock"""
        plot_data = combined_data.dropna(subset=['avg_polarity', 'daily_return', 'avg_vader_compound'])
        
        if len(plot_data) < 2:
            print(f"⚠ Insufficient data for {stock_symbol} dashboard")
            return
        
        os.makedirs(save_dir, exist_ok=True)
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle(f'News Sentiment vs Stock Returns: {stock_symbol}', fontsize=16, fontweight='bold')
        
        # 1. Scatter: Polarity vs Returns
        self._plot_scatter(axes[0, 0], plot_data, 'avg_polarity', 'daily_return',
                          'Sentiment Polarity', 'Daily Return (%)',
                          'TextBlob Sentiment vs Returns', 'blue')
        
        # 2. Scatter: VADER vs Returns
        self._plot_scatter(axes[0, 1], plot_data, 'avg_vader_compound', 'daily_return',
                          'VADER Compound Score', 'Daily Return (%)',
                          'VADER Sentiment vs Returns', 'orange')
        
        # 3. Time series
        self._plot_time_series(axes[1, 0], plot_data, stock_symbol)
        
        # 4. Distributions
        self._plot_distributions(axes[1, 1], plot_data, stock_symbol)
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.93)
        
        # Save dashboard
        dashboard_path = os.path.join(save_dir, f"{stock_symbol}_dashboard.png")
        plt.savefig(dashboard_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        
        print(f"✅ Dashboard saved: {dashboard_path}")
        
        # Create individual plots
        self.create_individual_plots(plot_data, stock_symbol, save_dir)
    
    def _plot_scatter(self, ax, data, x_col, y_col, x_label, y_label, title, color):
        """Create scatter plot with trend line"""
        ax.scatter(data[x_col], data[y_col], alpha=0.6, color=color, s=50)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title, fontweight='bold')
        ax.grid(True, alpha=0.3)
        
        # Add trend line
        if len(data) > 1:
            try:
                z = np.polyfit(data[x_col], data[y_col], 1)
                p = np.poly1d(z)
                ax.plot(data[x_col], p(data[x_col]), "r--", alpha=0.8, linewidth=2)
                
                # Add correlation
                corr = data[x_col].corr(data[y_col])
                ax.text(0.05, 0.95, f'r = {corr:.3f}', transform=ax.transAxes,
                       bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
            except:
                pass
    
    def _plot_time_series(self, ax, data, stock_symbol):
        """Create time series plot"""
        ax2 = ax.twinx()
        
        # Plot sentiment
        line1 = ax.plot(data['date'], data['avg_polarity'], 'g-', linewidth=2, label='Sentiment')
        ax.set_ylabel('Sentiment Polarity', color='g')
        ax.tick_params(axis='y', labelcolor='g')
        
        # Plot returns
        line2 = ax2.plot(data['date'], data['daily_return'], 'b-', alpha=0.7, label='Returns')
        ax2.set_ylabel('Daily Return (%)', color='b')
        ax2.tick_params(axis='y', labelcolor='b')
        
        ax.set_xlabel('Date')
        ax.set_title(f'{stock_symbol}: Timeline', fontweight='bold')
        ax.grid(True, alpha=0.3)
        
        # Combine legends
        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax.legend(lines, labels, loc='upper left')
        
        # Rotate dates
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    
    def _plot_distributions(self, ax, data, stock_symbol):
        """Plot distributions of sentiment and returns"""
        # Sentiment distribution
        ax.hist(data['avg_polarity'], bins=15, alpha=0.7, color='green', 
               edgecolor='black', label='Sentiment')
        ax.set_xlabel('Sentiment Polarity')
        ax.set_ylabel('Frequency')
        ax.set_title(f'{stock_symbol}: Distributions', fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def create_individual_plots(self, data, stock_symbol, save_dir):
        """Create individual plot files"""
        plot_dir = os.path.join(save_dir, "individual_plots", stock_symbol)
        os.makedirs(plot_dir, exist_ok=True)
        
        # Scatter: Polarity vs Returns
        plt.figure(figsize=(10, 6))
        self._plot_scatter(plt.gca(), data, 'avg_polarity', 'daily_return',
                          'Sentiment Polarity', 'Daily Return (%)',
                          f'{stock_symbol}: TextBlob Sentiment vs Returns', 'blue')
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f'{stock_symbol}_polarity_vs_returns.png'), 
                   dpi=300, bbox_inches='tight')
        plt.close()
        
        # Scatter: VADER vs Returns
        plt.figure(figsize=(10, 6))
        self._plot_scatter(plt.gca(), data, 'avg_vader_compound', 'daily_return',
                          'VADER Compound Score', 'Daily Return (%)',
                          f'{stock_symbol}: VADER Sentiment vs Returns', 'orange')
        plt.tight_layout()
        plt.savefig(os.path.join(plot_dir, f'{stock_symbol}_vader_vs_returns.png'), 
                   dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Individual plots saved for {stock_symbol}")

if __name__ == "__main__":
    visualizer = StockVisualizer()
    print("StockVisualizer initialized")