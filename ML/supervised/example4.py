import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

iris = load_iris()
print(iris.target)

iris_df = pd.DataFrame(iris.data,columns=iris.feature_names)
print(iris_df)

iris_df["target"] = iris.target
print(iris_df)

x = iris_df[['sepal length (cm)','sepal width (cm)']]
y = iris_df['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print("x_train:", len(x_train))
print("y_train:", len(y_train))
print("x_test:", len(x_test))
print("y_test:", len(y_test))

model = LogisticRegression()
model.fit(x_train,y_train)
print("model fitted")

y_pred = model.predict(x_test)
# print(y_pred)

print('Accuracy : ',accuracy_score(y_test, y_pred))

plt.scatter(x_test['sepal length (cm)'],x_test['sepal width (cm)'],c=y_pred,cmap='autumn')

plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()