
import streamlit as st
import pandas as pd
from upstox_helper import get_live_index_prices

st.set_page_config(page_title="AlphaTradex Dashboard", layout="wide")
st.title("📊 AlphaTradex – Indian Market Overview 🇮🇳")

st.markdown("Get real-time data of Nifty 50, Bank Nifty, and Sensex using the Upstox API")

st.subheader("📈 Live Indices")

data = get_live_index_prices()

if "error" in data:
    st.error(f"Error fetching data: {data['error']}")
else:
    df = pd.DataFrame(data).T
    st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown("Built with ❤️ by @AlphaTradex")
