import pandas as pd
import pandas as pd
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


titanic_df = pd.read_csv("titanic.csv")

df = titanic_df[["Sex", "Age", "Survived"]].dropna()
le = LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])

x = df[["Sex","Age"]]
y = df["Survived"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print("DecisionTreeClassifier : ")
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
plot_tree(clf,feature_names=x.columns,class_names=['Pass','Fail'],filled=True)
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

