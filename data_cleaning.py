import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"

os.makedirs(processed_path, exist_ok=True)

files = [f for f in os.listdir(raw_path) if f.endswith(".csv")]

for file in files:
    file_path = os.path.join(raw_path, file)

    df = pd.read_csv(file_path)

    df = df.drop_duplicates()
    df = df.ffill()

    output_path = os.path.join(processed_path, file)

    df.to_csv(output_path, index=False)

    print(f"Cleaned and saved: {file}")

print("All cleaned files saved successfully!")