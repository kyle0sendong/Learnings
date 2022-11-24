'''
In Multivariate Regression Algorithm, some of the input variables do not have number values 
which are not usable in creating the Regression Models. Examples of these are Sex, Address, Color, etc. These are called categorical data.  
To use these information as part of the historical data, dummy data are created to represent these information using values.  
For sex, 1 may be used to represent Males, and 0 for females.  
For colors, number may also be assigned for each.  
In this way, the information may be used in regression analysis and will make prediction possible.  
In the previously posted sample data set (insurance.csv), 
create a Multivariate Regression Analysis model that could 
predict the possible insurance charge based on age, sex, bmi, number of children, whether smoker or not, and location address as input variables.  
Create a dummy data for columns with categorical data (sex, smoker, region) in order to make it possible for regression analysis to work.  
Make sample predictions using random inputs to check for the capability of the model to make predictions.  
Submit a minimum of 10 screenshots of your sample runs in the link provided.   
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import seaborn as sns
import random
#number seed for the random number generator used in splitting of dataset
rngesus = random.randrange(0, 42) 

# get_y_intercept(slope, x, y)) computes for the y - intercept of x and y
def get_y_intercept(slope, x, y):
    y_intercept = 0
    y_mean = np.mean(y)
    mx = 0
    
    for i in range(len(x.columns)):
        x_mean = np.mean(x.iloc[:, i])
        mx += (slope[i] * x_mean)

    y_intercept =  y_mean - mx
    return y_intercept

# get_slope() computes the slope of x and y
def get_slope(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = 0
    denominator = 0
    
    for i in range(len(x)):
        x_temp = x.iloc[i]
        y_temp = y.iloc[i]
        numerator += (x_temp - x_mean) * (y_temp - y_mean)
        denominator += (x_temp - x_mean) ** 2
    
    slope = numerator/denominator
    if slope < 0:
        slope = 0
    return slope


# multivariate_regression() Uses formula = y = (m1x1 + m2x2 ... mNxN) + b
# Uses for loop for iterating every element in every column.
# @x - DataFrame, 
# @slope - slope of every independent variable, 
# @y_intercept taken from formula y = mx + b
# @returns the Multivariate Linear Regression model. 
def multivariate_regression(x, slope, y_intercept):
    predictor = []

    for i in range(len(x)): 
        mx = 0
        for j in range(len(x.columns)):  #m1x1 + m2x2 ... mnxn
            x_temp = x.iloc[i, j]
            mx += slope[j] * x_temp
            
        calculation = mx + y_intercept
        predictor.append(calculation)
        
    predictor = np.array(predictor)
    return predictor

# main() contains necessary code for running the algorithm presented from the class powerpoint
def main(): 
    insurance = pd.DataFrame(pd.read_csv('Python\csv_files\insurance.csv'))
    x = insurance.loc[ : , :'region']
    y = insurance.loc[ : , 'charges']
    
    #Preprocessing - converting to categorical data to numeric type using pandas.get_dummies.
    dummy1 = pd.get_dummies(insurance['sex'])
    dummy2 = pd.get_dummies(insurance['smoker'])
    dummy3 = pd.get_dummies(insurance['region'])
    x = pd.concat([x, dummy1], axis='columns')
    x = pd.concat([x, dummy2], axis='columns')
    x = pd.concat([x, dummy3], axis='columns')
    x = x.drop(['sex', 'smoker', 'region'], axis='columns') #drop the categorical variable
    
    # Splitting of dataset into training and testing dataset
    x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.3, random_state=rngesus)   
    
    # Computing for the slope of every column. Used in getting the y_intercept and the linear regression model
    slope = []
    for i in range (len(x.columns)):
        x_temp = x_train.iloc[:, i]
        m = get_slope(x_temp, y_train)
        slope.append(m)
    
    y_intercept = get_y_intercept(slope, x_train, y_train)
    predictor = multivariate_regression(x_test, slope, y_intercept) #Multivariate Linear Regression predictor
    
    #Display the created predictor model
    plt.xlabel('Multivariable')
    plt.ylabel('Charges')
    plt.title('Regression Algorithm from ppt')
    plt.scatter(x = y_test,
                y = predictor,
                edgecolor = 'b',
                linewidth = 0.5)
    plt.show()
    
    sns.regplot(x=y_test,
                y=predictor,
                ci=90,
                color ='#086655',
                marker = 'd',
                label = 'asd');

    accuracy = r2_score(y_test, predictor) * 100
    print(f' Accuracy of the model created from the PPT Algorithm is {accuracy:.2f}%')

main()
