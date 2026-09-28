# 🟦 Question 1 — NumPy | Advanced

# First, create the dataset yourself:

# import numpy as np

# np.random.seed(10)

# sales = np.column_stack([
#     np.random.randint(1001, 1101, 100),   # Product ID
#     np.random.randint(1, 10, 100),        # Quantity
#     np.random.randint(500, 5000, 100),    # Price
#     np.random.randint(0, 31, 100)         # Discount %
# ])

# The columns are:

# Product_ID | Quantity | Price | Discount
# Task

# Calculate the Final Revenue for every transaction:

# Revenue = Quantity × Price

# Discount Amount = Revenue × Discount / 100

# Final Revenue = Revenue - Discount Amount

# Then:

# Print their Final Revenue
# Do not use a Python for loop




import numpy as np
import pandas as pd


np.random.seed(10)

sale = np.column_stack([
    np.random.randint(1001, 1101, 100),   # Product ID
    np.random.randint(1, 10, 100),        # Quantity
    np.random.randint(500, 5000, 100),    # Price
    np.random.randint(0, 31, 100)         # Discount %
])

print(sale.shape)

print(pd.DataFrame(sale).describe())

df = pd.DataFrame(
    sale,
    columns=["Product_ID", "Quantity", "Price", "Discount"]
)


# Revenue = Quantity × Price
df["Revenue"] = df["Quantity"] * df["Price"]
print(df.head(10))

# Discount Amount = Revenue × Discount / 100
df["Discount_Amount"] = df["Revenue"] * df["Discount"] / 100
print(df.head(10))

# Final Revenue = Revenue - Discount Amount

df["final rev"] = df["Revenue"] - df["Discount_Amount"]
print(df.head(10))


# Show first 10 rows
print(df.head(10))

# Print their row indexes
print(df.head(10).index)