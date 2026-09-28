# 📦 Imports you need

import pandas as pd
from sklearn.datasets import load_diabetes

# Use the Diabetes dataset:

diabetes = load_diabetes()
print(diabetes.target)
# 🎯 Task
# Create a DataFrame called diabetes_df using diabetes.data.
diabetes_df = pd.DataFrame(diabetes.data)
print(diabetes_df)

# Use diabetes.feature_names as the column names.
diabetes_df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print(diabetes_df)

# Add the target column to the DataFrame.
diabetes_df["target"] = diabetes.target
print(diabetes_df)

# Display the first 5 rows.
print(diabetes_df.head(5))
