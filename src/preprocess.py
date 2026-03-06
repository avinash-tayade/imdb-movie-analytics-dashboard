import pandas as pd
import os
import numpy as np

def preprocess_data():

    input_path = "data/raw/imdb_raw.csv"
    df = pd.read_csv(input_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna()

    # Convert types
    df["Year"] = df["Year"].astype(int)
    df["Rating"] = df["Rating"].astype(float)
    df["Votes"] = df["Votes"].astype(int)
    df["Popularity"] = df["Rating"] * np.log(df["Votes"])

    # Keep movies after 1950 for better analysis
    df = df[df["Year"] >= 1950]

    # Create decade column
    df["Decade"] = (df["Year"] // 10) * 10

    os.makedirs("data/processed", exist_ok=True)

    output_path = "data/processed/imdb_cleaned.csv"
    df.to_csv(output_path, index=False)


    print("Cleaned dataset saved to:", output_path)
    print("Total movies after cleaning:", len(df))


if __name__ == "__main__":
    preprocess_data()

