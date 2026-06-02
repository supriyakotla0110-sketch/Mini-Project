import pandas as pd

df = pd.read_csv("rows.csv", low_memory=False)

print("Total Rows:", len(df))

print("\nMissing Narratives:")
print(df["Consumer complaint narrative"].isna().sum())

print("\nNon-Missing Narratives:")
print(df["Consumer complaint narrative"].notna().sum())

print("\nSample Complaint:")

sample = df["Consumer complaint narrative"].dropna().iloc[0]

print(sample[:1000])