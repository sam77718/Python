# Create:

# np.random.seed(70)

# sales = np.random.randint(1000, 10001, (15, 6))

# Think:

# 15 salespeople × 6 months

# Each row = salesperson
# Each column = month

# Tasks

# Using NumPy only:




# Print their average sales.

import numpy as np

np.random.seed(70)

sales = np.random.randint(1000, 10001, (15, 6))
print(sales)

# Find the total sales of each salesperson.

total_sale_person = np.sum(sales,axis=1)
print("total sales per person : ",total_sale_person)

# Find the average sales of each salesperson.

avg_sale_person = np.mean(sales,axis=1)
print("avg sales per person : ",avg_sale_person)

# Find the salesperson with the highest total sales.

highest_total_sale = np.max(total_sale_person)
print("highest total sale : ",highest_total_sale)

# Find the month with the highest overall sales.

month_sales = np.sum(sales, axis=0)
highest_sale_month_wise = np.argmax(month_sales)
print("Highest sales month index:", highest_sale_month_wise)

# Find salespeople whose average monthly sales > 6000.

month_avg_sal_person = np.mean(sales, axis=1)

print("month wise avg sal of the person : ",np.where(month_avg_sal_person > 6000)[0])

#  Find salespeople who had at least one month below 3000.

month_least_sal_person = np.mean(sales, axis=1)
print("month wise least sal of the person : ",np.where(month_least_sal_person < 3000)[0])

# Find salespeople who had every month above 5000.

salespeople = np.where(np.all(sales > 5000, axis=1))[0]
print("Salespeople:", salespeople)

# Print the indexes of those salespeople.

index =  np.column_stack((np.arange(len(sales)), sales))
print(index)