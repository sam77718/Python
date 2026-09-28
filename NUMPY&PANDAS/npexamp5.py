# Using customers-100.csv:

# Create a Name_Length column from First Name.

import pandas as pd
import numpy as np

# Then create a Customer Score using:
df = pd.read_csv("NUMPY&PANDAS/customers-100.csv")
print(df.head())

# Customer Score = Name_Length × 10

df["Name_Length"] = df["First Name"].str.len()
print(df[["First Name", "Name_Length"]])
df["Customer Score"] = df["Name_Length"]*10
print(df["Customer Score"])

# Tasks:

# Create the Customer Score column.
print(df[["First Name", "Name_Length","Customer Score"]])

# Rank all customers based on Customer Score, from highest to lowest.
df["Rank"] = df["Customer Score"].rank(
    ascending=False,
    method="min"
)


# Display the top 10 customers with:
# Customer Id
# First Name
# Last Name
# Name_Length
# Customer Score
top_10 = df.sort_values("Customer Score", ascending=False).head(10)

print(top_10[[
    "Customer Id",
    "First Name",
    "Last Name",
    "Name_Length",
    "Customer Score"
]])

# Find the customer with the lowest score.
lowest = df.sort_values("Customer Score", ascending=False).tail(1)
print(lowest[[
    "Customer Id",
    "First Name",
    "Last Name",
    "Name_Length",
    "Customer Score"
]])

