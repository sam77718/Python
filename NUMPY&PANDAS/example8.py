# Create this dataset:

import numpy as np

np.random.seed(80)
sales = np.random.randint(1000, 10001, (6, 4))
print(sales)

# Task
# You need to perform a business sales adjustment.
# 1. Increase sales in every quarter by 10%
# Create a new array:
# adjusted_sales
# Do not modify the original sales array.

updated_sales = np.array((sales*0.1)+ sales)
print("updated sales : ",updated_sales)

# Apply a different growth rate to each quarter

# Growth rates are:

growth = np.array([0.05, 0.10, 0.15, 0.20])
growth_rate = updated_sales * growth
print("growth rate : ",growth_rate)

# Find the difference between original and adjusted sales

# Create:

difference = growth_rate - sales
print("difference : ",difference)


# Replace all sales below ₹3,000 with ₹3,000
# Create another array without changing the original:

corrected_sales = sales.copy()

corrected_sales[corrected_sales < 3000] = 3000

print(corrected_sales)