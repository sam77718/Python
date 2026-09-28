# Problem 2 - Age Group vs Survival
# 👉 Question: Did children (age < 18) have a higher survival rate than adults (age ≥ 18)?
# Group A: Children survival status
# Group B: Adults survival status
# H₀: Children and adults had the same survival rate.
# H₁: Children had a higher survival rate.

import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest


data_df = sns.load_dataset('titanic')
print(data_df.head(5))

data_df["age_group"] = np.where(
    data_df["age"] < 18,
    "Child",
    "Adult"
)

count=data_df["age_group"].value_counts()
print("count : ",count)
print(data_df.groupby("age_group")["survived"].mean())

