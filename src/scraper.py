import pandas as pd
import os


def load_imdb_dataset():

    print("Downloading IMDb datasets...")

    ratings_url = "https://datasets.imdbws.com/title.ratings.tsv.gz"
    basics_url = "https://datasets.imdbws.com/title.basics.tsv.gz"

    ratings = pd.read_csv(ratings_url, sep="\t")
    basics = pd.read_csv(basics_url, sep="\t", low_memory=False)

    # Merge datasets
    df = pd.merge(basics, ratings, on="tconst")

    # Keep only movies
    df = df[df["titleType"].isin(["movie", "tvSeries"])]

    # Select useful columns
    df = df[[
    "primaryTitle",
    "startYear",
    "genres",
    "averageRating",
    "numVotes",
    "titleType"
    ]]

    # Rename columns
    df.columns = ["Title", "Year", "Genres", "Rating", "Votes", "Type"]

    # Remove missing values
    df = df[df["Year"] != "\\N"]
    df = df[df["Rating"].notna()]

    # Convert types
    df["Year"] = df["Year"].astype(int)
    df["Rating"] = df["Rating"].astype(float)

    # Keep top rated movies (votes > 50000)
    df = df[df["Votes"] > 50000]

    os.makedirs("data/raw", exist_ok=True)

    output_path = "data/raw/imdb_raw.csv"
    df.to_csv(output_path, index=False)

    print("Dataset saved to:", output_path)
    print("Total movies:", len(df))


if __name__ == "__main__":
    load_imdb_dataset()