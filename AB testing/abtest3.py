# **Problem 3 - Smokers vs Non-Smokers (Tips Dataset)**
# 👉 Using the **tips dataset** (comes with seaborn).
# Question: Did **non-smokers** leave a higher tip percentage (tip/total\_bill) than **smokers**?

# - Group A: Tip % for non-smokers
# - Group B: Tip % for smokers
# - H₀: Smokers and non-smokers tipped equally.
# - H₁: Non-smokers tipped more than smokers.

# give me only the data base first

import pandas as pd
import numpy as np
import seaborn as sns

data_df = sns.load_dataset("tips")

print(data_df)

import pandas as pd
import numpy as np
import seaborn as sns

data_df = sns.load_dataset("tips")

print(data_df)


data_df["tip_percentage"] = data_df["tip"] / data_df["total_bill"]
print(data_df["tip_percentage"])



tip_mean = data_df["tip_percentage"].mean()

data_df["above_mean"] = (
    data_df["tip_percentage"] > tip_mean
).astype(int)

non_smokers = data_df[data_df["smoker"] == "No"]["above_mean"]
smokers = data_df[data_df["smoker"] == "Yes"]["above_mean"]

count = [non_smokers.sum(), smokers.sum()]
no = [len(non_smokers),len(smokers)]
print(count)
print(no)

from statsmodels.stats.proportion import proportions_ztest
stat, p_value = proportions_ztest(count, no)
print(p_value)
