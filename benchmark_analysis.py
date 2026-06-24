import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("=" * 50)
print("BENCHMARK INDICES")
print("=" * 50)

print(df["index_name"].value_counts())

print("\n" + "=" * 50)
print("AVERAGE INDEX VALUE")
print("=" * 50)

print(df.groupby("index_name")["close_value"].mean())