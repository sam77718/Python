# 🟦 Question 11 — NumPy | Advanced Broadcasting + One-Hot Encoding

# Imagine you are preparing categorical data for a Machine Learning model.

# Create this dataset:

import numpy as np

categories = np.array(["cat", "dog", "bird", "dog", "cat", "fish", "bird", "cat"])
print(categories)

# Find all unique categories
# Expected concept:

unique = np.unique(categories)
print(unique)

# Create the one-hot encoded matrix
# For the original:

one_hot_encodeing = ["cat", "dog", "bird", "dog", "cat", "fish", "bird", "cat"]
one_hot = np.array([
    [1, 0, 0, 0],  # cat
    [0, 1, 0, 0],  # dog
    [0, 0, 1, 0],  # bird
    [0, 1, 0, 0],  # dog
    [1, 0, 0, 0],  # cat
    [0, 0, 0, 1],  # fish
    [0, 0, 1, 0],  # bird
    [1, 0, 0, 0]   # cat
])

print(one_hot)
print(one_hot.shape)


categories_order = np.array(["cat", "dog", "bird", "fish"])

decoded = categories_order[np.argmax(one_hot, axis=1)]

print(decoded)