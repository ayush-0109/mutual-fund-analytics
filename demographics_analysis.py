import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("=" * 50)
print("AGE GROUP DISTRIBUTION")
print("=" * 50)
print(df["age_group"].value_counts())

print("\n" + "=" * 50)
print("GENDER DISTRIBUTION")
print("=" * 50)
print(df["gender"].value_counts())

print("\n" + "=" * 50)
print("TOP 10 STATES")
print("=" * 50)
print(df["state"].value_counts().head(10))

print("\n" + "=" * 50)
print("PAYMENT MODE DISTRIBUTION")
print("=" * 50)
print(df["payment_mode"].value_counts())
