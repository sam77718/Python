# Different concept now.

# Using the original customers-100.csv, find all customers whose Last Name starts with "B" OR ends with "son".

import pandas as pd

df = pd.read_csv('NUMPY&PANDAS/customers-100.csv')

# Display:

# Customer Id
# First Name
# Last Name
# Email

result = df[['Customer Id','First Name','Last Name','Email']]
print(result)

# Also print the total number of matching customers.
print("Total matching customers:", len(result))

# Requirements
# Use Pandas string methods (.str...)
# Handle possible missing last names safely.
# Do not use loops.
# Don't use regular expressions unless you actually need them.

df["Subscription Date"] = pd.to_datetime(df["Subscription Date"])
print(df["Subscription Date"].dtype)

df = df.sort_values("Subscription Date", ascending=False)
print("--->",df)

updated =  df[['Customer Id','First Name','Last Name','Subscription Date']]
print(updated)


df["Email Provider"] = df["Email"].str.split("@").str[1]
print(df[['Email Provider','Email']])

print(df["Email Provider"].value_counts())