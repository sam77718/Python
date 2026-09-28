# 🟦 Q1 — Pandas + NumPy: Statistical Analysis

# Using customers-100.csv:




# Then use Pandas to identify the 5 rows with the highest values of that feature.

import numpy as np
import pandas as pd

df = pd.read_csv("NUMPY&PANDAS/customers-100.csv")
print(df)


# Create a numerical feature from the dataset and use NumPy to calculate its:
df["Name_Length"] = df["First Name"].str.len()


# mean
mean = np.mean(df["Name_Length"])
print("mean: ",mean)


# median

median = np.median(df["Name_Length"])
print("median: ",median)


# standard deviation

standard_deviation = np.std(df["Name_Length"])
print("median: ",standard_deviation)

# minimum

min = np.min(df["Name_Length"])
print("min: ",min)

# maximum

max = np.max(df["Name_Length"])
print("max: ",max)