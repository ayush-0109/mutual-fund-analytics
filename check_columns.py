import pandas as pd

df1 = pd.read_csv("data/raw/08_investor_transactions.csv")
print("INVESTOR TRANSACTIONS COLUMNS:")
print(df1.columns.tolist())

print()

df2 = pd.read_csv("data/raw/10_benchmark_indices.csv")
print("BENCHMARK COLUMNS:")
print(df2.columns.tolist())