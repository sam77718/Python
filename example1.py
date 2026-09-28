import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import accuracy_score

iris = datasets.load_iris() 
df = pd.DataFrame(iris.data, columns=iris.feature_names) 
df['target'] = iris.target 
print(df)

df = df[['sepal length (cm)','sepal width (cm)','target']]
df = df[df['target']!=2]

x = df[['sepal length (cm)','sepal width (cm)']]
y = df['target']



from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

model = SVC(kernel="linear")
model.fit(x_train,y_train)


y_pred = model.predict(x_test)
print("accuracy : ", accuracy_score(y_test,y_pred))

w = model.coef_[0]
b = model.intercept_[0]

print("Weights:", w)
print("Intercept:", b)

# Decision boundary
x_vals = np.linspace(
    x['sepal length (cm)'].min(),
    x['sepal length (cm)'].max(),
    50
)

y_vals = -(w[0] / w[1]) * x_vals - b / w[1]

# Plot
plt.scatter(
    df['sepal length (cm)'],
    df['sepal width (cm)'],
    c=df['target']
)

plt.plot(x_vals, y_vals, 'k-')

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()