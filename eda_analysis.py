import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 50)
print("CATEGORY DISTRIBUTION")
print("=" * 50)
print(df["category"].value_counts())

print("\n" + "=" * 50)
print("RISK CATEGORY DISTRIBUTION")
print("=" * 50)
print(df["risk_category"].value_counts())

print("\n" + "=" * 50)
print("FUND HOUSE DISTRIBUTION")
print("=" * 50)
print(df["fund_house"].value_counts())