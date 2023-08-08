'''
Multi-variate Regression using Scikit Learn Library
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import seaborn as sns
import random
rngesus = random.randrange(0, 42)  #number seed for the random number generator used in splitting of dataset

def using_sklearn():

    insurance = pd.DataFrame(pd.read_csv('Python\csv_files\insurance.csv'))
    x = insurance.loc[ : , : 'region']
    y = insurance.loc[ : , 'charges']
    
    # Preprocessing - converting to categorical data to numeric type using pandas.get_dummies
    dummy1 = pd.get_dummies(insurance['sex'])
    dummy2 = pd.get_dummies(insurance['smoker'])
    dummy3 = pd.get_dummies(insurance['region'])
    x = pd.concat([x, dummy1], axis='columns')
    x = pd.concat([x, dummy2], axis='columns')
    x = pd.concat([x, dummy3], axis='columns')
    x = x.drop(['sex', 'smoker', 'region'], axis='columns')
    # ====

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=rngesus)

    linreg = LinearRegression()
    linreg.fit(x_test, y_test)
    predictor = linreg.predict(x_test)
    
    plt.figure(2)
    plt.title('Using Scikit-learn')
    plt.xlabel('Actual');
    plt.ylabel('Predicted');
    plt.scatter(y_test,
                predictor, 
                edgecolor = '#8C6512',
                linewidth = 0.5)
    plt.show()
    
    sns.regplot(x = y_test, 
                y = predictor,
                ci = 90,
                color = '#8C6512',
                marker = 'd')
    
    accuracy = r2_score(y_test, predictor) * 100
    print(f' Accuracy of the model created from Scikit-Learn is {accuracy:.2f}%')

using_sklearn()
