import pandas as pd

df = pd.read_csv(
    "Dataset/Credit Card Fraud Risk Analysis.csv"
)

print(df.head())
print(df.shape)
print(df.isnull().sum())

df.drop_duplicates(inplace=True)
print("Duplicates Removed")

df.to_csv(
    "Dataset/cleaned_data.csv",
    index=False
)

print("Cleaned file saved")