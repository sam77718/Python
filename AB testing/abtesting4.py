import pandas as pd
import numpy as np
import seaborn as sns

data_df = sns.load_dataset("tips")

# Calculate tip percentage
data_df["tip_percentage"] = data_df["tip"] / data_df["total_bill"]

# Calculate average tip percentage
tip_mean = data_df["tip_percentage"].mean()

# 1 = above average, 0 = not above average
data_df["above_mean"] = (
    data_df["tip_percentage"] > tip_mean
).astype(int)

# Group A = Saturday
group_A = data_df[data_df["day"] == "Sat"]["above_mean"]

# Group B = Sunday
group_B = data_df[data_df["day"] == "Sun"]["above_mean"]

# Count successes
count = [group_A.sum(), group_B.sum()]
print("Count:", count)

# Total customers
no = [len(group_A), len(group_B)]
print("Total:", no)

# A/B Test
from statsmodels.stats.proportion import proportions_ztest

stat, p_value = proportions_ztest(count, no)

print("P-value:", p_value)