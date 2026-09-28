# Create this dataset:

# np.random.seed(30)

# sales = np.random.randint(100, 10001, 50)

# Each value represents the sales amount of one transaction.

# Task

# Normalize the sales values using Min-Max Normalization:

# Normalized = (value - minimum) / (maximum - minimum)

# Then:

# Find the minimum sales.
# Find the maximum sales.
# Create a normalized NumPy array.
# Print the first 10 normalized values.
# Verify that the minimum normalized value is 0 and maximum is 1.

import numpy as np
import pandas as pd

np.random.seed(30)

sales = np.random.randint(100, 10001, 50)
print("Sales values:", sales)

df = pd.DataFrame({'column': sales})
normalization = (df["column"] - df["column"].min()) / (df["column"].max() - df["column"].min())
print("Normalized values:", normalization)

min_sales = df["column"].min()
max_sales = df["column"].max()
print("Minimum sales:", min_sales)
print("Maximum sales:", max_sales)

print("First 10 normalized values:", normalization[:10])