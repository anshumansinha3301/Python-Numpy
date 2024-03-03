import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

stocks_info = {'AAPL': 150, 'TATA': 100, 'SSNLF': 326}

stock_data = {symbol: yf.download(symbol, start='2020-01-01', end='2022-01-01') for symbol in stocks_info.keys()}

# Extract closing prices from the stock data for each stock
closing_prices = {symbol: data['Close'] for symbol, data in stock_data.items()}

# Calculate daily returns using NumPy for each stock
daily_returns = {symbol: np.log(prices / prices.shift(1)) for symbol, prices in closing_prices.items()}

# Calculate cumulative returns using NumPy for each stock
cumulative_returns = {symbol: np.exp(np.cumsum(returns)) - 1 for symbol, returns in daily_returns.items()}

# Plotting the stock prices and cumulative returns for each stock
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

for symbol, prices in closing_prices.items():
    ax1.plot(prices, label=f'{symbol} ({stocks_info[symbol]} Rs)')

ax1.set_title('Stock Prices Over Time')
ax1.set_ylabel('Stock Price')
ax1.legend()

for symbol, returns in cumulative_returns.items():
    ax2.plot(returns, label=f'{symbol} ({stocks_info[symbol]} Rs)')

ax2.set_title('Cumulative Returns Over Time')
ax2.set_ylabel('Cumulative Returns')
ax2.axhline(y=0, color='r', linestyle='--', label='Zero Returns')
ax2.legend()

plt.tight_layout()
plt.show()
