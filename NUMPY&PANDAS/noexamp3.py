# 🟦 Q3 — Pandas + NumPy: Group Analysis

# Using customers-100.csv:

import numpy as np
import pandas as pd

df = pd.read_csv("NUMPY&PANDAS/customers-100.csv")
print(df)

# Create a Name_Length column from First Name.
df["Name_Length"] = df["First Name"].str.len()
print(df[["First Name", "Name_Length"]])

# Group the data by Country.
print(df.groupby("Country").size())

# Find the average Name_Length for each country.

avg = df.groupby("Country")["Name_Length"].mean()

print(avg)

# Find the country with the highest average name length.

highest = avg.idxmax()

print(highest)
# Requirements:

# Use Pandas + NumPy.
# No loops.
# Use groupby().
# Use NumPy for the average calculation.

# Write your code. I'll check it and then give you Q4.