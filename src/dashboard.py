import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page setup
st.set_page_config(page_title="Interactive IMDb Movie Analytics and Popularity Insights Dashboard", layout="wide")

st.title("🎬 Interactive IMDb Movie Analytics and Popularity Insights Dashboard")

# Load dataset with caching
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/imdb_cleaned.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

genres = sorted(set(g for sub in df["Genres"].str.split(",") for g in sub))

genre_filter = st.sidebar.selectbox(
    "Genre",
    ["All"] + genres
)

type_filter = st.sidebar.selectbox(
    "Content Type",
    ["All", "movie", "tvSeries"]
)

year_range = st.sidebar.slider(
    "Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2000, 2023)
)

rating_filter = st.sidebar.slider(
    "Minimum Rating",
    float(df["Rating"].min()),
    float(df["Rating"].max()),
    7.0
)

# Apply filters
filtered = df.copy()

if genre_filter != "All":
    filtered = filtered[filtered["Genres"].str.contains(genre_filter)]

if type_filter != "All":
    filtered = filtered[filtered["Type"] == type_filter]

filtered = filtered[
    (filtered["Year"] >= year_range[0]) &
    (filtered["Year"] <= year_range[1]) &
    (filtered["Rating"] >= rating_filter)
]

# Download filtered dataset
st.sidebar.download_button(
    label="Download Filtered Data",
    data=filtered.to_csv(index=False),
    file_name="filtered_movies.csv",
    mime="text/csv"
)

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Overview",
    "Popularity Analysis",
    "Genre Analysis",
    "Movie Explorer",
    "Recommendations",
    "Hidden Gems"
])

# -------------------------
# TAB 1: Overview
# -------------------------
with tab1:

    st.subheader("📊 Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Titles", len(filtered))
    col2.metric("Average Rating", round(filtered["Rating"].mean(), 2))
    col3.metric("Average Votes", int(filtered["Votes"].mean()))
    col4.metric("Best Rating", filtered["Rating"].max())

    st.subheader("⭐ Rating Distribution")

    fig = px.histogram(
        filtered,
        x="Rating",
        nbins=20,
        color_discrete_sequence=["#ff4b4b"]
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# TAB 2: Popularity Analysis
# -------------------------
with tab2:

    st.subheader("🔥 Popularity vs Rating")

    fig2 = px.scatter(
        filtered,
        x="Votes",
        y="Rating",
        hover_data=["Title"],
        color="Rating"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🏆 Most Popular Titles")

    top_pop = filtered.sort_values(
        by="Popularity",
        ascending=False
    ).head(10)

    st.dataframe(
        top_pop[["Title", "Year", "Rating", "Votes", "Popularity"]],
        use_container_width=True
    )

# -------------------------
# TAB 3: Genre Analysis
# -------------------------
with tab3:

    st.subheader("🎭 Top Genres")

    genre_counts = (
        filtered["Genres"]
        .str.split(",")
        .explode()
        .value_counts()
        .head(10)
    )

    fig3 = px.bar(
        x=genre_counts.index,
        y=genre_counts.values,
        labels={"x": "Genre", "y": "Number of Titles"},
        color=genre_counts.values
    )

    st.plotly_chart(fig3, use_container_width=True)

# -------------------------
# TAB 4: Movie Explorer
# -------------------------
with tab4:

    st.subheader("🔍 Search Movie or Series")

    search = st.text_input("Enter title")

    if search:

        result = df[df["Title"].str.contains(search, case=False)]

        if not result.empty:

            st.dataframe(
                result[["Title", "Year", "Rating", "Votes", "Popularity"]],
                use_container_width=True
            )

        else:
            st.warning("No titles found.")

# -------------------------
# TAB 5: Recommendations
# -------------------------
with tab5:

    st.subheader("🎯 Better Than Your Favorite")

    fav = st.text_input("Enter your favorite movie")

    if fav:

        pref = df[df["Title"].str.contains(fav, case=False)]

        if not pref.empty:

            genre = pref.iloc[0]["Genres"].split(",")[0]
            rating = pref.iloc[0]["Rating"]

            better = df[
                (df["Genres"].str.contains(genre)) &
                (df["Rating"] > rating)
            ].sort_values(by="Rating", ascending=False).head(10)

            st.write(f"Better titles in **{genre}** genre")

            st.dataframe(
                better[["Title", "Year", "Rating", "Votes"]],
                use_container_width=True
            )

        else:
            st.warning("Movie not found.")

# -------------------------
# TAB 6: Hidden Gems
# -------------------------
with tab6:

    st.subheader("💎 Hidden Gems")

    gems = filtered[
        (filtered["Rating"] > 8) &
        (filtered["Votes"] < filtered["Votes"].median())
    ].sort_values(by="Rating", ascending=False).head(10)

    st.dataframe(
        gems[["Title", "Year", "Rating", "Votes"]],
        use_container_width=True
    )