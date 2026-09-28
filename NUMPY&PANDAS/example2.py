import numpy as np
import pandas as pd

np.random.seed(20)

transactions = np.random.randint(100, 10001, 100)
print(transactions)

# Find transactions that are unusually high using the IQR method.

# Q1 = 25th percentile
Q1 = np.percentile(transactions, 25) 

# Q3 = 75th percentile
Q3 = np.percentile(transactions, 75)    

IQR = Q3 - Q1
print(IQR)

Upper_Limit = Q3 + 1.5 * IQR
print(Upper_Limit)


# Find all transactions greater than the Upper Limit.

high_transactions = transactions[transactions > Upper_Limit]
high_transactions

# rint their row indexes.

df = pd.DataFrame(transactions, columns=["Transactions"])
print(df.head(10))

# Print the number of outliers.

print(f"Number of outliers: {len(high_transactions)}")