# 🎬 Interactive IMDb Movie Analytics Dashboard

An interactive data analytics dashboard built using **Python, Streamlit, and Plotly** to explore and analyze movie data from the IMDb dataset.

The dashboard allows users to filter movies by genre, year, rating, and type (movie or series) to discover insights about popularity trends, ratings distribution, and hidden gems.

---

## 🚀 Live Demo

(After deployment you will add your link here)

Example:

https://your-dashboard-name.streamlit.app

---

## 📊 Features

- Interactive movie analytics dashboard
- Dynamic filtering by:
  - Genre
  - Year range
  - Rating
  - Content type (Movie / TV Series)
- Popularity analysis using a custom popularity score
- Rating distribution visualization
- Genre popularity analysis
- Movie search functionality
- Hidden gems discovery (high rating, low votes)
- Movie comparison and recommendations
- Download filtered dataset as CSV

---

## 📁 Project Structure
imdb-movie-analysis
│
├── data
│ ├── raw
│ │ └── imdb_raw.csv
│ │
│ └── processed
│ └── imdb_cleaned.csv
│
├── notebooks
│ └── eda.ipynb
│
├── reports
│ └── figures
│ ├── movies_per_decade.png
│ ├── rating_distribution.png
│ └── votes_vs_rating.png
│
├── src
│ ├── scraper.py
│ ├── preprocess.py
│ ├── analysis.py
│ └── dashboard.py
│
├── requirements.txt
├── main.py
└── README.md

---

## 📈 Data Science Workflow

The project follows a standard data science pipeline:
Data Collection
↓
Data Cleaning & Preprocessing
↓
Exploratory Data Analysis (EDA)
↓
Data Visualization
↓
Feature Engineering
↓
Interactive Dashboard

---

## 🧠 Popularity Score

A custom **Popularity Score** is calculated to rank movies based on impact:
Popularity = Rating × log(Votes)

This metric helps identify movies that are both highly rated and widely watched.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Matplotlib
- Seaborn

---

## ▶️ Running the Project Locally

Clone the repository:
git clone https://github.com/avinash-tayade/imdb-movie-analytics-dashboard

Navigate into the folder:
cd imdb-movie-analytics-dashboard

Install dependencies:
pip install -r requirements.txt

Run the dashboard:
streamlit run src/dashboard.py

---

## 📊 Dashboard Sections

- Overview
- Popularity Analysis
- Genre Analysis
- Movie Explorer
- Recommendations
- Hidden Gems

---

## 📸 Dashboard Preview

(Add screenshots here after deployment)

Example:

## 📌 Future Improvements

- Deploy dashboard to the cloud
- Add genre trend analysis
- Add interactive time-series visualizations
- Integrate real-time movie APIs

---

## 👨‍💻 Author

**Avinash Tayade**

Final Year Computer Engineering Student  
Rajiv Gandhi Institute of Technology, Mumbai

---