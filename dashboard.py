import streamlit as st
import pandas as pd
import psycopg2
import os

st.set_page_config(page_title="Crypto Market Dashboard", layout="wide")

st.write("🔥 DASHBOARD IS RUNNING")

# Database connection
def get_data():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            database=os.getenv("DB_NAME", "crypto_db"),
            user=os.getenv("DB_USER", "admin"),
            password=os.getenv("DB_PASSWORD", "admin123"),
            port=os.getenv("DB_PORT", 5432),
        )
        query = "SELECT * FROM crypto_market_current ORDER BY market_cap DESC"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()

# 🔥 IMPORTANT: get data BEFORE using it
df = get_data()

st.title("🚀 Crypto Market Dashboard")

# Show raw data temporarily for debugging
st.write(df.head())

# ---- KPIs ----
if not df.empty:
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Coins", len(df))
    col2.metric("Total Market Cap (Top Coins)", f"${df['market_cap'].sum():,.0f}")
    col3.metric("Average 24h Change", f"{df['price_change_24h'].mean():.2f}%")

    st.divider()

    # ---- Top Gainers ----
    st.subheader("🔥 Top 10 Gainers (24h)")
    top_gainers = df.sort_values("price_change_24h", ascending=False).head(10)
    st.dataframe(top_gainers[["coin_name", "symbol", "price", "price_change_24h"]])

    # ---- Market Cap Chart ----
    st.subheader("📊 Top 10 Coins by Market Cap")
    top_marketcap = df.head(10)
    st.bar_chart(top_marketcap.set_index("coin_name")["market_cap"])

    # ---- Price Change Chart ----
    st.subheader("📈 Price Change Distribution")
    st.bar_chart(df.set_index("coin_name")["price_change_24h"].head(20))
else:
    st.warning("No data available yet.")
