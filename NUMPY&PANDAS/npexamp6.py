# 🟦 Q5 — Pandas + NumPy: Date Feature Engineering


import pandas as pd
import numpy as np

df = pd.read_csv("NUMPY&PANDAS/customers-100.csv")
print(df.head())

# Convert Subscription Date into a proper datetime column.
df["Subscription Date"] = pd.to_datetime(df["Subscription Date"])

print(df["Subscription Date"])

# Then create three new columns:

# Subscription Year
# Subscription Month
# Subscription Quarter
# Subscription Year
df["Subscription Year"] = df["Subscription Date"].dt.year

# Subscription Month
df["Subscription Month"] = df["Subscription Date"].dt.month

# Subscription Quarter
df["Subscription Quarter"] = df["Subscription Date"].dt.quarter

print(df[[
    "Subscription Date",
    "Subscription Year",
    "Subscription Month",
    "Subscription Quarter"
]])


# Finally, find which quarter has the highest number of subscriptions.
quarter_counts = df["Subscription Quarter"].value_counts()

print(quarter_counts)


# Use NumPy to find the quarter with the highest number of subscriptions
highest_quarter = quarter_counts.index[np.argmax(quarter_counts.values)]

print("Quarter with highest subscriptions:", highest_quarter)
# Requirements
# Pandas + NumPy
# No loops
# Use Pandas datetime functionality
# Use value_counts() or another Pandas method for counting
# Use NumPy somewhere in the analysis