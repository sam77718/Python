import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


car_df = pd.read_csv("ML/supervised/car_prices.csv")
print(car_df)

car_df = car_df.dropna(subset=["sellingprice"])
car_df = car_df.dropna(subset=["year", "mmr"])

print(car_df[["year", "mmr", "sellingprice"]].isnull().sum())


x = car_df[["year",
        "mmr"]]

y = car_df["sellingprice"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
print("x_train",len(x_train))
print("y_train",len(y_train))
print("x_test",len(x_test))
print("y_test",len(y_test))



model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(y_pred)


mse = mean_squared_error(y_test,y_pred)
print(mse)
r2 = r2_score(y_test, y_pred)  # Too close --> close 1, Bad--> Close 0
print(r2)

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# Predictions
y_pred = model.predict(x_test)

# Plot actual data
plt.scatter(x_test["mmr"], y_test)

# Sort values so the line looks correct
sorted_index = x_test["mmr"].argsort()

plt.plot(
    x_test["mmr"].iloc[sorted_index],
    y_pred[sorted_index]
)

plt.xlabel("MMR")
plt.ylabel("Selling Price")
plt.title("Linear Regression - MMR vs Selling Price")

plt.show()