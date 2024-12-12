import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!
""")

# Define the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2024-5-31')
st.write("""
### Closing Price Chart
""")
# Display closing price chart
st.line_chart(tickerDF.Close)

st.write("""
### Volume Chart
""")
# Display volume chart
st.line_chart(tickerDF.Volume)
