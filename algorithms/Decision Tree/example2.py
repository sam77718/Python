import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score


df = pd.read_csv("loan_data.csv")

print(df)

df["loan_approved"] = (
    (df["fico"] >= 650) &
    (df["dti"] <= 20) &
    (df["delinq.2yrs"] <= 1) &
    (df["pub.rec"] == 0)
)
df["loan_approved"] = df["loan_approved"].apply(
    lambda x: "Approved" if x else "Rejected"
)
print(df)

print(df["loan_approved"].value_counts())

le = LabelEncoder()
df['purpose'] = le.fit_transform(df['purpose'])
df.head()

x = df[["credit.policy","purpose","delinq.2yrs","pub.rec","not.fully.paid"]]
y = df[["loan_approved"]]


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
print("x_train",len(x_train))
print("y_train",len(y_train))
print("x_test",len(x_test))
print("y_test",len(y_test))

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
