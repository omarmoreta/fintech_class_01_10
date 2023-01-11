# Beta Comparisons

# This program reads in the daily closing prices of social media stocks—FB, TWTR, SNAP—and the S&P 500 as CSVs and calculates the rolling 30-day beta values of each social media to plot the trends in volatility relative to the market.

# Import libraries and dependencies
import pandas as pd
from pathlib import Path
import matplotlib_inline

# Read the daily closing prices of FB, set the `date` as a datetime index
fb_data = Path("./Resources/Beta_Comparisons/fb_data.csv")
fb_dataframe = pd.read_csv(fb_data, index_col="date", infer_datetime_format=True, parse_dates=True)

# Read the daily closing prices of TWTR, set the `date` as a datetime index
twtr_data = Path("./Resources/Beta_Comparisons/twtr_data.csv")
twtr_dataframe = pd.read_csv(twtr_data, index_col="date", infer_datetime_format=True, parse_dates=True)

# Read the daily closing prices of SNAP, set the `date` as a datetime index
snap_data = Path("./Resources/Beta_Comparisons/snap_data.csv")
snap_dataframe = pd.read_csv(snap_data, index_col="date", infer_datetime_format=True, parse_dates=True)

# Read the daily closing prices of S&P 500, set the `date` as a datetime index
sp500_data = Path("./Resources/Beta_Comparisons/sp500_data.csv")
sp500_dataframe = pd.read_csv(sp500_data, index_col="date", infer_datetime_format=True, parse_dates=True)
sp500_dataframe.head()

# Create a new pivot table where the columns are the closing prices for each ticker
combined_dataframe = pd.concat([fb_dataframe, twtr_dataframe, snap_dataframe, sp500_dataframe], axis="columns", join="inner")

# Sort datetime index in ascending order (past to present)
combined_dataframe.sort_index()

# Set column names to 'FB' 'TWTR', 'SNAP', and 'S&P 500'
combined_dataframe.columns = ["FB", "TWTR", "SNAP", "S&P 500"]

# Display a few rows
combined_dataframe.head()

# Use the `pct_change` function to calculate daily returns of closing prices for each column
daily_returns = combined_dataframe.pct_change()
daily_returns.head()

# Calculate covariance of all daily returns of social media stocks vs. S&P 500
fb_covariance = daily_returns['FB'].cov(daily_returns['S&P 500'])
twtr_covariance = daily_returns['TWTR'].cov(daily_returns['S&P 500'])
snap_covariance = daily_returns['SNAP'].cov(daily_returns['S&P 500'])

print("Covariance")
print(f"FB: {fb_covariance} | TWTR: {twtr_covariance} | SNAP: {snap_covariance}")

# Calculate variance of all daily returns of social media stocks vs. S&P 500
variance = daily_returns['S&P 500'].var()

print("Variance")
print(f"S&P500: {variance}")

# Calculate beta of all daily returns of social media stocks
fb_beta = fb_covariance / variance
twtr_beta = twtr_covariance / variance
snap_beta = snap_covariance / variance

print("Beta")
print(f"FB: {fb_beta} | TWTR: {twtr_beta} | SNAP: {snap_beta}")

# Calculate 30-day rolling covariance of AMZN vs. S&P 500 and plot the data
rolling_fb_covariance = daily_returns['FB'].rolling(window=30).cov(daily_returns['S&P 500'])
rolling_twtr_covariance = daily_returns['TWTR'].rolling(window=30).cov(daily_returns['S&P 500'])
rolling_snap_covariance = daily_returns['SNAP'].rolling(window=30).cov(daily_returns['S&P 500'])

# Calculate 30-day rolling variance of S&P 500
rolling_variance = daily_returns['S&P 500'].rolling(window=30).var()

# Calculate 30-day rolling beta of AMZN and plot the data
rolling_fb_beta = rolling_fb_covariance / rolling_variance
rolling_twtr_beta = rolling_twtr_covariance / rolling_variance
rolling_snap_beta = rolling_snap_covariance / rolling_variance

print("Rolling Beta")
print(f"FB: {rolling_fb_beta} | TWTR: {rolling_twtr_beta} | SNAP: {rolling_snap_beta}")

# Set the figure and plot the different datasets as multiple trends on the same figure
ax = rolling_fb_beta.plot(figsize=(20, 10), title='Rolling 30-Day Beta of Social Media Stocks')
rolling_twtr_beta.plot(ax=ax)
rolling_snap_beta.plot(ax=ax)

# Set the legend of the figure
ax.legend(["FB", "TWTR", "SNAP"])