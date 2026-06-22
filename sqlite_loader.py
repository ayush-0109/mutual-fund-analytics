import pandas as pd
import sqlite3
import os

conn = sqlite3.connect("mutual_funds.db")

data_path = "data/raw"

files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

for file in files:
    df = pd.read_csv(os.path.join(data_path, file))

    table_name = file.replace(".csv", "")

    df.to_sql(table_name, conn, if_exists="replace", index=False)

    print(f"Loaded {file} -> {table_name}")

conn.close()

print("\nAll files loaded into SQLite database successfully!")