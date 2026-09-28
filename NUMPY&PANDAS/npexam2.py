# 🟦 Q2 — Pandas + NumPy: Conditional Feature Engineering

import numpy as np
import pandas as pd

df = pd.read_csv("NUMPY&PANDAS/customers-100.csv")
print(df)

# Create a new column based on a numerical condition using np.where().

# Create numerical feature
df["Name_Length"] = df["First Name"].str.len()

# Create new column based on condition
df["Name_Category"] = np.where(
    df["Name_Length"] >= 6,
    "Long",
    "Short"
)

df

# Then use Pandas to count how many records fall into each category.

count = df["Name_Category"].value_counts()
print(count)

# Example concept:

# Value >= threshold → "High"
# Value < threshold  → "Low"

# Don't use loops.