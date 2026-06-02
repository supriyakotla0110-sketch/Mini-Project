import pandas as pd

# Load dataset
df = pd.read_csv("rows.csv", low_memory=False)

# Keep only useful columns
df = df[[
    "Consumer complaint narrative",
    "Product",
    "Issue"
]]

# Remove empty complaints
df = df.dropna()

# Save cleaned dataset
df.to_csv(
    "cleaned_complaints.csv",
    index=False
)

print("Cleaned Dataset Shape:")
print(df.shape)

print("\nProducts:")
print(df["Product"].nunique())

print("\nTop 10 Products:")
print(df["Product"].value_counts().head(10))

print("\nCleaned dataset saved as:")
print("cleaned_complaints.csv")