# Choose a numerical column from the dataset.

# Your task:
import pandas as pd
import numpy as np

df = pd.read_csv("NUMPY&PANDAS/customers-100.csv")
print(df.head())

df["Name_Length"] = df["First Name"].str.len()

# Check how many missing (NaN) values the column contains.
missing = df["Name_Length"].isna().sum()

print(missing)

# Calculate the median of Name_Length using np.median(), ignoring NaN values.
median = np.median(df["Name_Length"].dropna())

print(median)

# Create a new column Name_Length_Cleaned.
median = np.median(df["Name_Length"].dropna())

df["Name_Length_Cleaned"] = df["Name_Length"].fillna(median)

print(df[["Name_Length", "Name_Length_Cleaned"]])

# Replace the missing values in the new column with the median.
df["Name_Length_Cleaned"] = df["Name_Length"].fillna(median)

print(df[["Name_Length", "Name_Length_Cleaned"]])

# Verify that Name_Length_Cleaned has 0 missing values.
print(df["Name_Length_Cleaned"].isna().sum())

# Do not modify the original Name_Length column.
median = np.median(df["Name_Length"].dropna())

df["Name_Length_Cleaned"] = df["Name_Length"].fillna(median)