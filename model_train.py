import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load your expanded dataset
df = pd.read_csv("tickets.csv")  # must have columns: message, category

X = df["message"]
y = df["category"]

# Build pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

model.fit(X, y)

# Save trained model
joblib.dump(model, "model/ticket_model.pkl")
print("✅ Model trained and saved!")
