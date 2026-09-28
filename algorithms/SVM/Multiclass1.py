import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA


digit = datasets.load_digits()
x = digit.data
y = digit.target

# Reduce dimensions to 2D using PCA  # PCA -- Principal component Analysis (64 features --> 2 features)
pca = PCA(n_components=2)
x_reduced = pca.fit_transform(x)

print(x.shape)
print(x_reduced.shape)

x_train, x_test, y_train, y_test = train_test_split(x_reduced,y,test_size=0.3, random_state=42, stratify=y)

clf = SVC(kernel="linear")
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 7. Decision boundary visualization
x_min, x_max = x_reduced[:, 0].min() - 1, x_reduced[:, 0].max() + 1
y_min, y_max = x_reduced[:, 1].min() - 1, x_reduced[:, 1].max() + 1
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 500),
    np.linspace(y_min, y_max, 500)
)

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.tab10)
plt.scatter(x_reduced[:, 0], x_reduced[:, 1], c=y, edgecolors="k", cmap=plt.cm.tab10, s=40)
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("SVM Decision Boundaries (Digits 0–9, PCA-reduced to 2D)")
plt.colorbar()
plt.show()
