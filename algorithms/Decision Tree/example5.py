from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

data_df = pd.read_csv("datasets/ai4i2020.csv")
print(data_df.head())
print(data_df.info())
print(data_df.describe())

data = data_df[["Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", "Torque [Nm]", "Machine failure","Tool wear [min]", "TWF", "HDF", "PWF", "OSF", "RNF"]].dropna()
x = data.drop(columns=["Machine failure"])
x.columns = x.columns.str.replace(r"[\[\]<>]", "", regex=True)

print(x.head())
y = data["Machine failure"]
print(y.head())


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print("decision tree")
clf = DecisionTreeClassifier()
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)
print(accuracy_score(y_pred,y_test))


importance = clf.feature_importances_
features = x.columns
plt.figure(figsize=(12,8))
plt.bar(features,importance)
plt.show()

plt.figure(figsize=(12,8))
plot_tree(
    clf,
    feature_names=x.columns,
    class_names=["No Failure", "Failure"],
    filled=True
)
plt.show()

print("RandomForestClassifier : ")
clf = RandomForestClassifier()
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))


importance = clf.feature_importances_
features = x.columns
plt.figure(figsize=(12,8))
plt.bar(features,importance)
plt.show()

print("XGBClassifier")
clf = XGBClassifier()
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

importance = clf.feature_importances_
features = x.columns
plt.figure(figsize=(12,8))
plt.bar(features,importance)
plt.show()



