# 🟦 Question 10 — NumPy | Real-World Data Cleaning

# Create this dataset:

import numpy as np

np.random.seed(100)

data = np.random.randint(100, 1001, 30)
original_data = data.copy()

# Add some invalid values
data[[3, 8, 15, 22]] = -1

print(data)

# Identify all invalid values (-1).

invalid_values = data[data == -1]
print("Invalid values:", invalid_values)

# Count how many invalid values exist.

count = len(invalid_values)
print("count of the invalid values :", count)

# Calculate the average of the valid sales values only.

valid_values = data[data != -1]
print("valid values:", valid_values) 

avg = np.mean(valid_values)
print("avg of the data expect -1: ",avg)

# Replace every -1 with the average
data[data == -1] = avg

print("Updated data:")
print(data)

# Print the original data.

print("Original data:")
print(original_data)

# Print the cleaned data.

cleaned_data = data.copy()
print("Cleaned data:")
print(cleaned_data)