# Diversification
# This program reads in the CSV datasets of several stocks and calculates a correlation table and heatmap to determine the semiconductor stock that is least correlated to `JNJ` and `HD`.

# Import libraries and dependencies
import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib_inline


# Set file paths
hd_data = Path("./Resources/Correlation/HD.csv")
jnj_data = Path("./Resources/Correlation/JNJ.csv")
intc_data = Path("./Resources/Correlation/INTC.csv")
amd_data = Path("./Resources/Correlation/AMD.csv")
mu_data = Path("./Resources/Correlation/MU.csv")
nvda_data = Path("./Resources/Correlation/NVDA.csv")
tsm_data = Path("./Resources/Correlation/TSM.csv")

# Read the individual CSV datasets
hd = pd.read_csv(hd_data, index_col="date")
jnj = pd.read_csv(jnj_data, index_col="date")
intc = pd.read_csv(intc_data, index_col="date")
amd = pd.read_csv(amd_data, index_col="date")
mu = pd.read_csv(mu_data, index_col="date")
nvda = pd.read_csv(nvda_data, index_col="date")
tsm = pd.read_csv(tsm_data, index_col="date")

intc.head()

# Use the `concat` function to combine the DataFrames by matching indexes (or in this case `date`)
stocks_dataframe = pd.concat([jnj, hd, intc, amd, mu, nvda, tsm], axis="columns", join="inner")
stocks_dataframe.head()

# Use the `pct_change` function to calculate daily returns for each stock
daily_returns = stocks_dataframe.pct_change()
daily_returns

# Use the `corr` function to calculate correlations for each stock pair
correlation = daily_returns.corr()
correlation

# Create a heatmap from the correlation values
sns.heatmap(correlation)

# Create a heatmap from the correlation values and adjust the scale
sns.heatmap(correlation, vmin=-1, vmax=1)