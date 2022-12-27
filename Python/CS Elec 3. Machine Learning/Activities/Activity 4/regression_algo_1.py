'''
Kyle A. Destura - BSCS 4A
Activity #4
Using the data in the 'insurance.csv' file
Create a linear regression prediction model 
using the AGE and BMI column as values for X and Y 
where age is the independent variable 'x' and BMI as the dependent variable 'y'. 
Using the developed model, predict the BMI of a person with the following age:

17 years old
18 years old
19 years old
20 years old
65 years old
66 years old
67 years old
68 years old
69 years old
70 years old
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import random

insurance = pd.read_csv('Python\csv_files\insurance.csv')
x = insurance.loc[:, 'age']
y = insurance.loc[:, 'bmi']
x = np.array(x)
y = np.array(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=random.randrange(0, 42))


def get_y_intercept(slope, x, y):
    return np.mean(y) - (slope*np.mean(x))


def get_slope(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = 0
    denominator = 0

    for index in range(len(x)):
        xi = x[index]
        yi = y[index]
        numerator += (xi-x_mean) * (yi-y_mean)
        denominator += ((xi-x_mean) ** 2)
    
    return numerator/denominator


def get_slope_y_intercept(x, y):
    slope = get_slope(x, y)
    y_intercept = get_y_intercept(slope, x, y)

    return slope, y_intercept


def regression_algorithm(x, slope, y_intercept):
    predictor = []
    for i in x:
        calculation = slope*(i) + y_intercept
        predictor.append(calculation)

    return np.array(predictor)


slope, y_intercept = get_slope_y_intercept(x_train, y_train)
linear_regression_predictor = regression_algorithm(x_test, slope, y_intercept)

plt.figure(1)

plt.scatter(
    x_test,
    y_test,
    edgecolor='b',
    linewidth=0.5)

plt.plot(
    x_test,
    linear_regression_predictor,
    color='g',
    linewidth=0.5)

plt.xlabel('Age')
plt.ylabel('BMI')
plt.title('Regression Algorithm (1) from (Class Powerpoint)')
plt.show()

accuracy = r2_score(y_test, linear_regression_predictor) * 100
print(f'Accuracy of the model created from formula in the PPT {accuracy:.2f}%')

custom_x = np.array([17, 18, 19, 20, 65, 66, 67, 68, 69, 70])
linear_regression_predictor = regression_algorithm(custom_x, slope, y_intercept)
print('\nPredicted BMI')
i = 0

while i < len(custom_x):
    print(f'{custom_x[i]} years old: {linear_regression_predictor[i]:.2f}')
    i += 1
