import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Read the data into a Pandas DataFrame
data = pd.read_csv('US_Unemployment_Oct2012.csv')
# Check the structure of the data
print(data.columns)

# Handle missing values if any
data = data.dropna()
# Visualize stock price data
# Assuming 'SPY' is the column containing stock data
plt.figure(figsize=(12, 6))
plt.plot(data['State'], data['SPY'], label='SPY Stock Price')
plt.title('SPY Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Calculate daily returns
data['Daily_Return'] = data['Close'].pct_change()

# Calculate cumulative returns
data['Cumulative_Return'] = (1 + data['Daily_Return']).cumprod() - 1
# Calculate 50-day moving average
data['50_MA'] = data['Close'].rolling(window=50).mean()
# Analyze correlation
correlation_matrix = data[['SPY', 'IYW', 'VT', 'DBA', 'TLT', 'PDBC', 'IAU']].corr()

# Visualize stock price volatility
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
