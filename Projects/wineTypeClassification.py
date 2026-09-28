# Project: Wine Type Classification using Multiclass SVM 🍷
# Problem statement

# A winery has collected chemical measurements from different wine samples. Your task is to build an SVM classification model that predicts which wine class a sample belongs to.

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Loads the Wine dataset.

wine = datasets.load_wine()

# Creates X and y.

x = wine.data
y = wine.target

pca = PCA(n_components=2)
x_reduced = pca.fit_transform(x)

# Checks the dataset shape.

print("shape of x : ",x.shape)
print("shape of reduced x : ",x_reduced.shape)

# Splits the data into 70% training and 30% testing.

x_train, x_test, y_train, y_test = train_test_split(x_reduced,y,test_size=0.3,random_state=42, stratify=y)

# Trains an SVM using:

model = SVC(kernel="linear")
model.fit(x_train,y_train)

# Predicts the test data.

y_pred = model.predict(x_test)

# Calculates:

# Accuracy
accuracy_score = accuracy_score(y_pred,y_test)
print("accuracy_score : ",accuracy_score)

# Precision
Precision = precision_score(y_pred,y_test,average="macro")
print("Precision : ",Precision)

# Recall

Recall = recall_score(y_pred,y_test,average="macro")
print("Recall : ",Recall)

# F1-score

F1_score = f1_score(y_pred,y_test,average="macro")
print("f1_score : ",f1_score)

# Confusion matrix


confusion_matrix = confusion_matrix(y_pred,y_test)
print("confusion_matrix : ",confusion_matrix)

# 7. Decision boundary visualization
x_min, x_max = x_reduced[:, 0].min() - 1, x_reduced[:, 0].max() + 1
y_min, y_max = x_reduced[:, 1].min() - 1, x_reduced[:, 1].max() + 1
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 500),
    np.linspace(y_min, y_max, 500)
)

Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.tab10)
plt.scatter(x_reduced[:, 0], x_reduced[:, 1], c=y, edgecolors="k", cmap=plt.cm.tab10, s=40)
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("SVM Decision Boundaries (Digits 0–9, PCA-reduced to 2D)")
plt.colorbar()
plt.show()
