import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

print("Loading Dataset...")

df = pd.read_csv("rows.csv", low_memory=False)

df = df[[
    "Consumer complaint narrative",
    "Product"
]]

df = df.dropna()

df = df.sample(20000, random_state=42)

X = df["Consumer complaint narrative"]
y = df["Product"]

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "complaint_model.pkl")

# Save vectorizer
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model Saved Successfully!")