import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("data/processed/imdb_cleaned.csv")

# Feature columns
features = ["Year", "Votes", "Genres", "Type"]

X = df[features]
y = df["Rating"]

# Convert categorical columns
X = pd.get_dummies(X)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)

model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

# Save column order
joblib.dump(X.columns.tolist(), "model_columns.pkl")

print("Model trained and saved successfully!")