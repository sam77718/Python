# A/B Testing

# Problem 1 - Class vs Survival

# 👉 Question: Did 1st class passengers have a higher survival rate than 3rd class passengers on the Titanic?

# Group A: Survival of 1st class passengers

# Group B: Survival of 3rd class passengers

# Null Hypothesis (H₀): Both classes had the same survival rate.

# Alternate Hypothesis (H₁): 1st class passengers had a higher survival rate.

import pandas as pd
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest


data_df = sns.load_dataset('titanic')
print(data_df.head(5))
print(data_df.describe())
print(data_df.info())

#  Question: Did 1st class passengers have a higher survival rate than 3rd class passengers on the Titanic?

# first_class_survived = data_df[data_df["class"]=="First"]["survived"].mean()
# third_class_survived =data_df[data_df["class"]=="Third"]["survived"].mean()
# print("first class survived mean :",first_class_survived,'\n' "third class survived mean :",third_class_survived )

group_A = data_df[data_df["class"] == "First"]["survived"]
print("group A",group_A)

group_B = data_df[data_df["class"] == "Third"]["survived"]
print("group B",group_B)

count = [group_A.sum(), group_B.sum()]
print("count: ",count)

no = [len(group_A),len(group_B)]
print(no)


stat, p_value = proportions_ztest(count, no)

print(count)
print(stat)  # Almost Zero

if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis : No Significant difference b/w male and female tips wrt mean")