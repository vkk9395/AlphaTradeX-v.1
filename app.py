import streamlit as st
import pandas as pd
from upstox_helper import get_live_index_prices

# Set up the page
st.set_page_config(page_title="AlphaTradex Dashboard", layout="wide")
st.title("📊 AlphaTradex – Indian Market Overview 🇮🇳")
st.markdown("Get real-time data of **Nifty 50**, **Bank Nifty**, and **Sensex** using the Upstox API")

st.subheader("📈 Live Indices (via Upstox)")

# Get data from Upstox
try:
    data = get_live_index_prices()

    if "error" in data:
        st.error(f"API Error: {data['error']}")
    else:
        df = pd.DataFrame(data).T
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"App crashed: {e}")

st.markdown("---")
st.caption("Made with ❤️ by @AlphaTradex | Powered by Upstox API")

