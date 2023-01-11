# Instructor Demo: Simple Moving Averages

# This program reads in the CSV datasets of Netflix (NFLX) and plots the 20, 50, and 100 Simple Moving Averages (SMA) using the `rolling` function, `window` parameter, and `mean` function.

# Import libraries and dependencies
import pandas as pd
from pathlib import Path
import matplotlib_inline

# Set file path
nflx_data = Path("./Resources/Rolling_Statistics/nflx.csv")

# Read the CSV into a DataFrame and set the 'date' column as a datetime index
nflx_dataframe = pd.read_csv(nflx_data, index_col="date", infer_datetime_format=True, parse_dates=True)
nflx_dataframe.sort_index(inplace=True)
# Display a few records
nflx_dataframe.head()

# Plot DataFrame
nflx_dataframe.plot()

# Calculate 20-day Simple Moving Average for NFLX Closing Prices
nflx_sma_20 = nflx_dataframe.rolling(window=20).mean()
nflx_sma_20.plot()

# Calculate 50-day Simple Moving Average for NFLX Closing Prices
nflx_sma_50 = nflx_dataframe.rolling(window=50).mean()
nflx_sma_50.plot()

# Calculate 100-day Simple Moving Average for NFLX Closing Prices
nflx_sma_100 = nflx_dataframe.rolling(window=100).mean()
nflx_sma_100.plot()

# Set figure of the daily closing prices of NFLX
ax = nflx_dataframe.plot(figsize=(25,10))

# Overlay SMA20, SMA50, and SMA100 on the same figure
nflx_sma_20.plot(ax=ax)
nflx_sma_50.plot(ax=ax)
nflx_sma_100.plot(ax=ax)

# Set the legend of the figure
ax.legend(["Original", "SMA20", "SMA50", "SMA100"]);

# Set figure of the daily closing prices of NFLX
ax = nflx_dataframe.plot(figsize=(25,10))

# Overlay STD20, STD50, and STD100 on the same figure
nflx_dataframe.rolling(window=20).std().plot(ax=ax)
nflx_dataframe.rolling(window=50).std().plot(ax=ax)
nflx_dataframe.rolling(window=100).std().plot(ax=ax)

# Set the legend of the figure
ax.legend(["Original", "STD20", "STD50", "STD100"]);