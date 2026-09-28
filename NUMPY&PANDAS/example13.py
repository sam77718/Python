# Using the same df:

# Change the DataFrame index to Customer Id.
# Using .loc[], retrieve the customer whose Customer Id is 4d8e5c.
# Display only:
# First Name
# Last Name
# Company
# Country

# Restriction: Use .loc[] for the final selection.

import pandas as pd

df = pd.read_csv('NUMPY&PANDAS/customers-100.csv')

# Change the index to Customer Id
df.set_index("Customer Id", inplace=True)

# Retrieve the customer and display only required columns
result = df.loc[
    "4d8e5c",
    ["First Name", "Last Name", "Company", "Country"]
]

print(result)