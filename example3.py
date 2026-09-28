import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder



df = pd.read_csv("datasets/train.csv")
print(df.head())
print(df.describe())
print(df.info())

columns = ["Gender", "Married", "Dependents", "Education",
           "Employment_Status", "Credit_History", "Property_Area",
           "Loan_Status"]

le = LabelEncoder()

for col in columns:
    df[col] = le.fit_transform(df[col])

print(df.head())

x = df[["Gender", "Married", "Dependents", "Education",
        "Employment_Status", "Credit_History", "Property_Area"]]
print(x)

# Target
y = df[["Loan_Status"]]
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

clf = DecisionTreeClassifier()
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

importance = clf.feature_importances_
features = x.columns
plt.figure(figsize=(12,8))
plt.bar(features,importance)
plt.show()


clf = RandomForestClassifier()
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

importance = clf.feature_importances_
features = x.columns
plt.figure(figsize=(12,8))
plt.bar(features,importance)
plt.show()




x = df[["Credit_History","Married"]]
y = df[["Loan_Status"]]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)


model = SVC(kernel="linear")
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

# 1. Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 2. Precision
precision = precision_score(y_test, y_pred)
print("Precision:", precision)

# 3. Recall
recall = recall_score(y_test, y_pred)
print("Recall:", recall)

# 4. F1-score
f1 = f1_score(y_test, y_pred)
print("F1-score:", f1)

# 5. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# 6. Feature Importance / SVM coefficients
feature_importance = pd.DataFrame({
    "Feature": x.columns,
    "Coefficient": model.coef_[0],
    "Importance": np.abs(model.coef_[0])
})

print("Feature Importance:")
print(feature_importance)

# Hyperplane
w = model.coef_[0]
b = model.intercept_[0]

x_vals = np.linspace(-0.2, 1.2, 100)

y_vals = -(w[0] * x_vals + b) / w[1]

# Plot
plt.figure(figsize=(8, 6))

plt.scatter(
    df["Credit_History"],
    df["Married"],
    c=df["Loan_Status"]
)

plt.plot(
    x_vals,
    y_vals,
    "k-",
    linewidth=2,
    label="Hyperplane"
)

plt.xlabel("Credit_History")
plt.ylabel("Married")
plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)
plt.legend()
plt.grid()
plt.show()