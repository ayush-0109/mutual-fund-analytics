import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 50)
print("TOP 10 FUNDS BY SHARPE RATIO")
print("=" * 50)

top_sharpe = df.sort_values(
    by="sharpe_ratio",
    ascending=False
)

print(
    top_sharpe[
        ["scheme_name", "sharpe_ratio", "alpha", "beta"]
    ].head(10)
)

print("\n" + "=" * 50)
print("TOP 10 FUNDS BY ALPHA")
print("=" * 50)

top_alpha = df.sort_values(
    by="alpha",
    ascending=False
)

print(
    top_alpha[
        ["scheme_name", "alpha", "beta"]
    ].head(10)
)