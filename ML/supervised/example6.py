# Step 1 — Import:

# from sklearn.datasets import fetch_california_housing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Step 2 — Load:

housing = fetch_california_housing()
print(housing.target)

# Step 3 — Create DataFrame

housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
print(housing_df)
# Use:

# housing.data

# as the data and:

# housing.feature_names

# as the column names.

# Step 4 — Add target

housing_df['target'] = housing.target
print(housing_df)

y = housing_df['target']
print(len(y))

x = housing_df[["HouseAge","Population","AveOccup"]]
print(len(x))

# Split into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print("x_train:", len(x_train))
print("y_train:", len(y_train))
print("x_test:", len(x_test))
print("y_test:", len(y_test))


model = LinearRegression()
model.fit(x_train, y_train)
print("model fitted")

y_pred = model.predict(x_test)
print(y_pred)

mse = mean_squared_error(y_test,y_pred)
print(mse)
r2 = r2_score(y_test, y_pred)  # Too close --> close 1, Bad--> Close 0
print(r2)


plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, color='red')
plt.xlabel('BMI')
plt.ylabel('Diabetes')
plt.show()