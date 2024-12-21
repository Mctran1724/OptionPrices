import yfinance as yf
import numpy as np
import pandas as pd

def pull_options(underlying_ticker: str) -> pd.DataFrame:
    """Given the ticker symbol of an underlying asset on yfinance, retrieve a pandas DataFrame with associated option prices"""

    tk = yf.Ticker(underlying_ticker)
    expirations = tk.options

    