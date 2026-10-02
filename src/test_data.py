import pandas as pd

df = pd.read_csv("data/fake_reviews.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nLabel distribution:")
print(df["label"].value_counts())

print("\nFirst 5 reviews:")
print(df.head())
