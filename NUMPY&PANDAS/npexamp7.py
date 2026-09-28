# 🟦 Q6 — Pandas + NumPy: Grouping & Analysis

# Using the same customers-100.csv:
import pandas as pd
import numpy as np

df = pd.read_csv("NUMPY&PANDAS/customers-100.csv")
print(df.head())

# 1. Group the customers by Country.
grouped = df.groupby("Country")

print(grouped)


# 2. Find the number of customers in each country.
grouped = df.groupby("Country").size()

print(grouped)


# 3. Find the average Customer Score for each country.
avg_score = df.groupby("Country")["Customer Score"].mean()

print(avg_score)

# 4. Find the country with the highest average Customer Score.
highest = avg_score.idxmax()

print(highest)
# Requirements
# Pandas + NumPy
# No loops
# Use groupby()
# Use an aggregation method such as count() / mean()
# Use NumPy somewhere in the analysis

# Try it yourself first. Send me your code, and I'll check it.