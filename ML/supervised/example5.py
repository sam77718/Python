# Load the dataset using load_breast_cancer()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score


# Create a DataFrame from data.data
cancer = load_breast_cancer()
print(cancer.target)

# Add target to the DataFrame
cancer_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
print(cancer_df)

cancer_df['target']=cancer.target
print(cancer_df)

# Use these two features:
# mean radius
# mean texture
x = cancer_df[['mean radius','mean texture']]
print(len(x))

# Use target as y

y = cancer_df['target'] 
print(len(y))

# Split into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print("x_train:", len(x_train))
print("y_train:", len(y_train))
print("x_test:", len(x_test))
print("y_test:", len(y_test))

# Create LogisticRegression()
model = LogisticRegression()
model.fit(x_train,y_train)
print("model fitted")
# Fit the model
# Predict y_pred
y_pred = model.predict(x_test)
print(len(y_pred))

# Calculate accuracy
print('Accuracy : ',accuracy_score(y_test, y_pred))


# Create a scatter plot:
# X-axis → mean radius
# Y-axis → mean texture
# c=y_pred

plt.scatter(x_test['mean radius'],x_test['mean texture'],c=y_pred,cmap='autumn')

plt.xlabel('mean radius')
plt.ylabel('mean texture')
plt.show()