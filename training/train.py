import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

df = pd.read_csv("training/data/sample_emails.csv")
X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), max_df=0.9)),
    ("clf", LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)
print("Test score:", pipeline.score(X_test, y_test))

os.makedirs("app/models", exist_ok=True)
joblib.dump(pipeline, "app/models/model.joblib")
print("Model saved to app/models/model.joblib")

