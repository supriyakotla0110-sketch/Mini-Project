import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

faq_path = os.path.join(BASE_DIR, "banking_faq.csv")

faq_df = pd.read_csv(faq_path)

FAQS = dict(
    zip(
        faq_df["Question"].str.lower(),
        faq_df["Answer"]
    )
)