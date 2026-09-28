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


data = load_breast_cancer()
print(data.target)

df = pd.DataFrame(data.data, columns=data.feature_names)
print(df)

df['target']=data.target
print(df)

x = df.drop(columns=["target"])
print("X",x)
y = df["target"]
print("Y",y)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print("Decision tree")
clf = DecisionTreeClassifier()
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))


importance = clf.feature_importances_
features = x.columns
plt.figure(figsize=(12,8))
plt.bar(features,importance)
plt.show()

plt.figure(figsize=(12,8))
plot_tree(clf,feature_names=x.columns,class_names=['True','False'],filled=True)
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



