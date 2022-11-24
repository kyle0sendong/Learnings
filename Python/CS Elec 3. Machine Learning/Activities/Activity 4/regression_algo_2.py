'''
Regression Algorithm Using Scikit Learn Library
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split    #splitting training and testing sets
from sklearn.metrics import r2_score    #For testing accuracy
import random #For random number generator on seeds

insurance = pd.read_csv('Python\csv_files\insurance.csv')
x = insurance.loc[:,'age']
y = insurance.loc[:,'bmi']
x = np.array(x)
y = np.array(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = random.randrange(0, 42))

# Reshaping array to convert from 1D to 2D array for the model fitting
x_test = x_test.reshape(-1,1)
x_train = x_train.reshape(-1,1)

# Creating linear regression model.
linear_regression_model = linear_model.LinearRegression()
linear_regression_model.fit(x_train, y_train)
linear_regression_predictor = linear_regression_model.predict(x_test)

plt.scatter(
    x = x_test,
    y = y_test,
    edgecolor='b',
    linewidth=0.5)

plt.plot(
    x_test,
    linear_regression_predictor,
    color='g',
    linewidth=2)

plt.xlabel('Age')
plt.ylabel('BMI')
plt.title('Regression Algorithm using Scikit Learn Library')
plt.show()

accuracy = r2_score(y_test, linear_regression_predictor) * 100
print(f' Accuracy of the model created from Scikit-Learn is {accuracy:.2f}%')

custom_x = np.array([17,18,19,20,65,66,67,68,69,70]).reshape(-1,1)
linear_regression_predictor = linear_regression_model.predict(custom_x)
print('\nPredicted BMI')
i = 0
while(i < len(custom_x)):
    print(f'{custom_x[i]} years old: {linear_regression_predictor[i]:.2f}')
    i += 1
