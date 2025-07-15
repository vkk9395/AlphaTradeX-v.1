import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="AlphaTradex Dashboard", layout="wide")
st.title("📊 AlphaTradex – Indian Market Dashboard 🇮🇳")

st.subheader("📈 Live Indices")

# Define symbols for Indian indices
symbols = {
    "Nifty 50": "%5ENSEI",
    "Sensex": "%5EBSESN",
    "Bank Nifty": "%5ENSEBANK"
}

def get_index_data():
    data = {}
    for name, symbol in symbols.items():
        ticker = yf.Ticker(symbol)
        info = ticker.history(period="1d", interval="1m")
        if not info.empty:
            latest = info.iloc[-1]
            prev_close = info['Close'].iloc[0]
            change = latest["Close"] - prev_close
            pct_change = (change / prev_close) * 100
            data[name] = {
                "LTP": round(latest["Close"], 2),
                "Change": round(change, 2),
                "Change (%)": round(pct_change, 2)
            }
    return data

try:
    index_data = get_index_data()
    df = pd.DataFrame(index_data).T
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"Error fetching index data: {e}")

st.caption("Made with ❤️ by @AlphaTradex")
