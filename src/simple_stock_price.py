import yfinance as yf
import streamlit as st

TICKER = 'TSLA'

st.write(f"""

         # A Simple Stock Price App :rocket:

         Shown are the stock closing price and volume of {TICKER}!

         """)
ticker_data = yf.Ticker(TICKER)

ticker_dataframe = ticker_data.history(period='1d', start='2016-05-31',
                                       end='2021-05-31')

st.write(f"""

         ### Daily Closing Price For {TICKER}

         """)
st.line_chart(ticker_dataframe.Close)

st.write(f"""

         ### Daily Volume For {TICKER}

         """)

st.line_chart(ticker_dataframe.Volume)
