import pandas as pd

def load_analytics():

    df = pd.read_csv(
        "cleaned_complaints.csv"
    )

    total_complaints = len(df)

    total_categories = df["Product"].nunique()

    top_categories = (
        df["Product"]
        .value_counts()
        .head(10)
    )

    return (
        total_complaints,
        total_categories,
        top_categories
    )