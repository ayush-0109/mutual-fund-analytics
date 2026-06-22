import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

top_funds = df[["scheme_name", "fund_house", "aum_crore"]]

top_funds = top_funds.sort_values(
    by="aum_crore",
    ascending=False
)

print("=" * 50)
print("TOP 10 FUNDS BY AUM")
print("=" * 50)

print(top_funds.head(10))