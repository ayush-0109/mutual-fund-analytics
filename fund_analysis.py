import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("="*50)
print("TOTAL FUNDS")
print("="*50)
print(len(df))

print("\nTOTAL FUND HOUSES")
print(df["fund_house"].nunique())

print("\nFUND HOUSES:")
print(df["fund_house"].unique())

print("\nCATEGORIES:")
print(df["category"].value_counts())

print("\nRISK CATEGORIES:")
print(df["risk_category"].value_counts())

print("\nUNIQUE AMFI CODES:")
print(df["amfi_code"].nunique())
