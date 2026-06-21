import pandas as pd
import os

data_path = "data/raw"

files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

for file in files:
    print("\n" + "=" * 50)
    print("FILE:", file)

    df = pd.read_csv(os.path.join(data_path, file))

    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nDATA QUALITY SUMMARY")
print("=" * 50)

for file in files:
    df = pd.read_csv(os.path.join(data_path, file))

    print(f"\n{file}")
    print("Missing Values:")
    print(df.isnull().sum().sum())

    print("Duplicate Rows:")
    print(df.duplicated().sum())