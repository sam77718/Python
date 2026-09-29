# Build a Multiclass SVM Classification model to predict
# the customer segment of a customer based on their
# demographic and purchasing behavior.

# Requirements
# Use Python
# Use Pandas for dataset handling
# Use Scikit-learn
# Perform train-test split

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# Budget
# Regular
# Premium

customer = pd.read_csv("datasets/customer_segmentation_data.csv")

print(customer)
print(customer.describe())
print(customer.info())


# Encode Education Level

le = LabelEncoder()


customer["Education Level"] = le.fit_transform(
    customer["Education Level"]
)

customer["Income Level"] = le.fit_transform(
    customer["Income Level"]
)

customer["Policy Type"] = le.fit_transform(
    customer["Policy Type"]
)


# Creates X and y

x = customer[
    [
        "Age",
        "Income Level",
        "Education Level",
        "Policy Type"
    ]
]

y = customer["Segmentation Group"]

# PCA

pca = PCA(n_components=2)

x_reduced = pca.fit_transform(x)


# Train-test split

x_train, x_test, y_train, y_test = train_test_split(
    x_reduced,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)


# Use SVC
# Use an RBF kernel

model = SVC(kernel="rbf")

model.fit(x_train, y_train)


# Prediction

y_pred = model.predict(x_test)


# Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("accuracy :", accuracy)


# Precision

Precision = precision_score(
    y_test,
    y_pred,
    average="macro"
)

print("Precision :", Precision)


# Recall

Recall = recall_score(
    y_test,
    y_pred,
    average="macro"
)

print("Recall :", Recall)


# F1-score

F1_score = f1_score(
    y_test,
    y_pred,
    average="macro"
)

print("F1 Score :", F1_score)


# Confusion matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix :")
print(cm)
# Use the appropriate average parameter for multiclass classification
# Make a prediction for one new customer
# Print the predicted customer segment