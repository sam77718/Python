# 🟦 Question 1 — Filtering + Multiple Conditions

# Using customers-100.csv:

# Find customers who satisfy both conditions:

# Country is India
# Their Email contains the letter "a" (case-insensitive)

# Display only:

# First Name
# Last Name
# Email
# Country

# Also print the number of matching customers.

# Restriction: Pandas only, no loops.

# Write your code and I'll check it.

import pandas as pd

df = pd.read_csv("NUMPY&PANDAS/customers-100.csv")
print(df)

result = df[
    (df["Country"] == "India") &
    (df["Email"].str.contains("a", case=False, na=False))
]

print(result[["First Name", "Last Name", "Email", "Country"]])

print(len(result))