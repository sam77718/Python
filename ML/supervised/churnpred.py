import numbers as np 
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from matplotlib.pylab import plt


churn_df = pd.read_csv("ML/supervised/customer_churn_dataset-testing-master (1).csv")


print(churn_df)
print(churn_df.head())
print(churn_df.columns)
print(churn_df.shape)

x = churn_df[["Age","Tenure",
        "Usage Frequency",
        "Support Calls",
        "Payment Delay",
        "Total Spend",
        "Last Interaction"]]

y = churn_df[["Churn"]]
print(y)

print(len(x),len(y))


x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42)

print("x_train",len(x_train))
print("y_train",len(y_train))
print("x_test",len(x_test))
print("y_test",len(y_test))

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(len(y_pred))

print('Accuracy : ',accuracy_score(y_test, y_pred))

import matplotlib.pyplot as plt
plt.scatter(
    x_test["Age"],
    x_test["Total Spend"],
    c=y_test["Churn"],
    cmap="coolwarm"
)

plt.xlabel("Age")
plt.ylabel("Total Spend")
plt.title("Actual Customer Churn")

plt.show()
