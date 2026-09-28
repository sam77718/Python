import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score





df = pd.read_csv("StudentsPerformance.csv")
print(df.head())
print(df.describe())
print(df.info())

print(df.isnull().sum())

df["avg"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

# Calculate overall mean
mean_avg = df["avg"].mean()
df["pass"] = df["avg"].apply(lambda x: "Pass" if x > mean_avg else "Fail")

df = df[['gender','avg','pass']].dropna()


print(df)
from sklearn.preprocessing import LabelEncoder

# Encode sex xolumn
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
df.head()

x = df.drop("pass",axis=1)
y=df["pass"]

x_train,x_test, y_train,y_test = train_test_split(x,y,test_size=0.2)
print("x_train",len(x_train))
print("y_train",len(y_train))
print("x_test",len(x_test))
print("y_test",len(y_test))

clf = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state = 42)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

importance = clf.feature_importances_
features = x.columns
plt.figure(figsize=(12,8))
plt.bar(features,importance)
plt.show()

plt.figure(figsize=(12,8))
plot_tree(clf,feature_names=x.columns,class_names=['Pass','Fail'],filled=True)
plt.show()