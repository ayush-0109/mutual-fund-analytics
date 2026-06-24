import streamlit as st
import pandas as pd

st.title("Mutual Fund Analytics Dashboard")

df = pd.read_csv("data/raw/07_scheme_performance.csv")

st.header("Dataset Overview")
st.write(df.head())

st.header("Category Distribution")
st.bar_chart(df["category"].value_counts())

st.header("Risk Category Distribution")
st.bar_chart(df["risk_grade"].value_counts())

st.header("Top 10 Funds by AUM")

top_funds = df.sort_values(
    by="aum_crore",
    ascending=False
).head(10)

st.dataframe(
    top_funds[
        [
            "scheme_name",
            "fund_house",
            "aum_crore"
        ]
    ]
)