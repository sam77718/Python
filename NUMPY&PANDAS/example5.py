# Create this dataset:

# import numpy as np

# np.random.seed(50)

# sales = np.random.randint(1000, 10001, (12, 4))

# Think of it as:

# 12 months × 4 quarters/regions

# Each row represents a month and each column represents a region.

# Task

# Using NumPy only:

# Print the indexes (row, column) of those above-average sales values.
# Helpful functions

# You may need:

# np.sum()
# np.mean()
# np.argmax()
# np.where()


import numpy as np

np.random.seed(50)

sales = np.random.randint(1000, 10001, (12, 4))
print("Sales",sales)

# Calculate the total sales for each month.
total_sales_month = np.sum(sales,axis=1)
print("total sales per month : ",total_sales_month)

# Calculate the total sales for each region.
total_sales_region = np.sum(sales,axis=0)
print("total sales per region : ",total_sales_region)

# Find the month with the highest total sales.

highest_sal_month = max(total_sales_month)
print("highest sal per month",highest_sal_month)

# Find the region with the highest total sales.

highest_sal_region = max(total_sales_region)
print("highest sal per region",highest_sal_region)


# Find the overall average sales.

overall_avg = np.mean(sales)
print("overall avg : ",overall_avg)

# Find all individual sales values that are greater than the overall average.

highest_sales = sales[sales > overall_avg]
print(highest_sales)

# Print the indexes (row, column) of those above-average sales values.
rows, columns = np.where(sales > overall_avg)

print("Rows:", rows)
print("Columns:", columns)