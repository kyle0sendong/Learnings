"""
3rd algorithm from https://www.geeksforgeeks.org/linear-regression-python-implementation/ 
This has a lot more specific computation compared to the algorithm in the presentation
This does not split the dataset to training and testing
"""

import pandas as pd                                          #for loading csv file data to numpy array
import numpy as np                                             #for using data as array
import matplotlib.pyplot as plt                                 #for plotting graph of x,y

insurance = pd.read_csv('Python/csv_files/insurance.csv')
x = insurance.loc[:, 'age']
y = insurance.loc[:, 'bmi']


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
  
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
  
    # calculating cross-deviation and deviation about x
    ss_xy = np.sum(y*x) - n*m_y*m_x
    ss_xx = np.sum(x*x) - n*m_x*m_x
  
    # calculating regression coefficients
    b_1 = ss_xy/ss_xx
    b_0 = m_y - b_1*m_x
  
    return b_0, b_1


def plot_regression_line(x, y, b):
    
    y_predictor = b[0] + b[1] * x  # predicted response vector
    
    plt.scatter(
        x,
        y,
        edgecolor='b',
        linewidth=0.5)

    plt.plot(
        x,
        y_predictor,
        color='g')
    
    plt.title('Regression Algorithm from (geeksforgeeks.com)')
    plt.xlabel('Age')
    plt.ylabel('BMI')
    plt.show()


b = estimate_coef(x, y)
plot_regression_line(x, y, b)
