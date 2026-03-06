import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def run_analysis():

    df = pd.read_csv("data/processed/imdb_cleaned.csv")

    os.makedirs("reports/figures", exist_ok=True)

    # 1 Rating Distribution
    plt.figure(figsize=(8,5))
    sns.histplot(df["Rating"], bins=20)

    plt.title("Distribution of IMDb Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")

    plt.savefig("reports/figures/rating_distribution.png")
    plt.close()

    # 2 Movies per Decade
    decade_counts = df["Decade"].value_counts().sort_index()

    plt.figure(figsize=(10,5))
    sns.barplot(x=decade_counts.index, y=decade_counts.values)

    plt.title("Movies Released Per Decade")
    plt.xlabel("Decade")
    plt.ylabel("Number of Movies")

    plt.savefig("reports/figures/movies_per_decade.png")
    plt.close()

    # 3 Votes vs Rating
    plt.figure(figsize=(8,5))
    sns.scatterplot(x=df["Votes"], y=df["Rating"])

    plt.title("Votes vs Rating")
    plt.xlabel("Votes")
    plt.ylabel("Rating")

    plt.savefig("reports/figures/votes_vs_rating.png")
    plt.close()

    print("Graphs saved in reports/figures")


if __name__ == "__main__":
    run_analysis()