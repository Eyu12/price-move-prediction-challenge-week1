# 10 Academy: Artificial Intelligence Mastery - Week 1 Challenge

## 🎯 Project Overview
  A comprehensive analysis platform that explores the relationship between financial news sentiment and stock price movements through three progressive tasks covering Git workflows, quantitative analysis, and correlation studies.

## 📋 Task Breakdown
### 🚀 Task 1: Git and GitHub Fundamentals
    Objective: Establish robust development environment and perform exploratory data analysis on financial news data.

### ✅ Minimum Requirements
- Create GitHub repository with proper branching strategy
- Establish task-1 branch with descriptive commits (3+ daily)
- Implement CI/CD workflows with GitHub Actions
- Set up Python development environment

### 📊 Analysis Components
- Descriptive Statistics
   - Textual length analysis (headline characteristics)
   - Publisher activity frequency
   - Temporal publication trends
- Text Analysis & Topic Modeling
  - NLP for keyword extraction and topic identification
  - Event detection (e.g., "FDA approval", "price target")
- Time Series Analysis
  - Publication frequency patterns
  - Market event correlation
  - Optimal trading timing analysis
- Publisher Analysis
  - Contributor impact assessment
  - Content type differentiation
  - Organizational domain analysis

## 📈 Task 2: Quantitative Analysis with PyNance and TA-Lib
   Objective: Implement technical analysis using financial libraries to identify trading signals and patterns.

### ✅ Minimum Requirements
- Merge task-1 into main via Pull Request
- Create task-2 branch for ongoing development
- Implement technical indicator calculations
- Create comprehensive visualizations

### 🔧 Technical Implementation
- Data Preparation
 - Load OHLCV (Open, High, Low, Close, Volume) data into pandas
 - Data cleaning and validation
- TA-Lib Indicators
 - Moving Averages (SMA, EMA)
 - Relative Strength Index (RSI)
 - MACD (Moving Average Convergence Divergence)
 - Bollinger Bands
 - Stochastic Oscillator
- PyNance Financial Metrics
 - Volatility calculations
 - Performance metrics
 - Risk-adjusted returns
- Visualization
 - Interactive price charts with indicators
 - Technical analysis dashboards
 - Pattern recognition visuals

### 📊 Key Performance Indicators
- Proactivity: Self-learning and reference sharing
- Accuracy: Precision of technical indicators
- Completeness: Comprehensive data analysis coverage

## 🔗 Task 3: News Sentiment & Stock Movement Correlation
   Objective: Analyze correlation between news sentiment and stock price movements using advanced NLP and statistical methods.

### ✅ Minimum Requirements
- Merge task-2 into main via Pull Request
- Create task-3 branch for correlation analysis
- Implement sentiment analysis pipeline
- Calculate statistical correlations

### 🧠 Analysis Pipeline
#### Data Preparation
- Date normalization and alignment
- Timestamp standardization
- Dataset merging and validation
#### Sentiment Analysis
- Tools: NLTK, TextBlob
- Methods:
 - Polarity scoring (positive/negative/neutral)
 - Subjectivity analysis
 - VADER sentiment for financial text
#### Stock Movement Analysis
- Daily returns calculation: (Price_t - Price_{t-1}) / Price_{t-1} * 100
- Volatility measurement
- Return distribution analysis
#### Correlation Analysis
- Pearson correlation coefficient
- Statistical significance testing (p-values)
- Lagged correlation analysis
- Multi-day sentiment aggregation

### 📈 Supported Stocks
- AAPL (Apple)
- AMZN (Amazon)
- GOOG (Google)
- META (Meta)
- MSFT (Microsoft)
- NVDA (NVIDIA)

### 📊 Expected Outcomes
#### Task 1 Deliverables
- Repository with proper Git workflow
- EDA reports and insights
- Topic modeling results
- Publisher analysis findings

#### Task 2 Deliverables
- Technical indicator calculations
- Financial metric analysis
- Interactive visualizations
- Trading signal identification

#### Task 3 Deliverables
- Sentiment analysis results
- Correlation coefficients and significance
- Multi-stock comparison
- Actionable investment insights

### 🔍 Analysis Insights
#### Key Research Questions
- Temporal Patterns: When are most financial news articles published?
- Publisher Influence: Which sources drive market movements?
- Technical Signals: Which indicators best predict price changes?
- Sentiment Impact: How does news tone affect stock returns?
- Correlation Strength: Is there statistically significant relationship between news and prices?

#### Methodological Approach
- Quantitative Rigor: Statistical significance testing
- Temporal Alignment: Precise date matching
- Multiple Timeframes: Daily, weekly, and monthly analysis
- Cross-validation: Multiple sentiment analysis methods

### 🤝 Contribution Guidelines
#### Branch Strategy
- main: Production-ready code
- task-1: Exploratory data analysis
- task-2: Technical analysis implementation
- task-3: Correlation analysis development

#### Commit Standards
- Descriptive commit messages
- Minimum 3 commits daily during active development
- Feature-based branching
- Pull request reviews before merging

#### Code Quality
- PEP 8 compliance
- Comprehensive testing
- Documentation strings
- Type hints where applicable

### 📈 Business Applications
#### For Traders
- Sentiment-based trading signals
- Technical indicator alerts
- News impact assessment

#### For Researchers
- Financial NLP methodologies
- Market efficiency studies
- Behavioral finance insights

#### For Developers
- Modular financial analysis codebase
- Reproducible research framework
- Extensible architecture

### 📚 References & Learning Resources
#### Technical Analysis
- TA-Lib documentation
- PyNance tutorials
- Financial time series analysis

#### Natural Language Processing
- NLTK for sentiment analysis
- TextBlob implementation guides
- VADER sentiment for financial text

#### Statistical Methods
- Pearson correlation interpretation
- Time series analysis techniques
- Hypothesis testing in finance