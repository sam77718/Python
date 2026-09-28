import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix)
from sklearn.model_selection import train_test_split


df = pd.read_csv("datasets/customer_purchase_data.csv")
print(df.head(5))
print(df.info())

x = df[["Age","Gender"]]
y = df["PurchaseStatus"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

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

# Decision boundary
w = model.coef_[0]
b = model.intercept_[0]

x_vals = np.linspace(
    x['Age'].min(),
    x['Age'].max(),
    50
)

y_vals = -(w[0] / w[1]) * x_vals - b / w[1]

# Plot
plt.scatter(
    df['Age'],
    df['Gender'],
    c=df['PurchaseStatus']
)

plt.plot(x_vals, y_vals, 'k-')

plt.xlabel('Age')
plt.ylabel('Gender')
plt.show()