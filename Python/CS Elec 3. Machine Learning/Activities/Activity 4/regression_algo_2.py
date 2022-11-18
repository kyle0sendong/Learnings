'''
https://towardsdatascience.com/linear-regression-model-899558ba0fc4

Algorithm :
1. Loading the Dataset
2. Taking the independent and dependent variable
3. Splitting to independent(x) and dependent(y) variables using split
4. Choosing the Model
5. Using Linear Regression Model
6. Fitting the training dataset
7. Use the created model to predict.s
'''
import pandas as pd                                          #for loading csv file data to numpy array
import numpy as np                                             #for using data as array
import matplotlib.pyplot as plt                                 #for plotting graph of x,y
from sklearn import linear_model                              #for model we want to predict by
from sklearn.model_selection import train_test_split        #splitting training and testing sets
from sklearn.metrics import r2_score
import random

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
plt.title('Regression Algorithm from (towardsdatascience.com)')
plt.show()

accuracy = r2_score(y_test, linear_regression_predictor) * 100
print(f' Accuracy of the model created from Scikit-Learn is {accuracy:.2f}%')
