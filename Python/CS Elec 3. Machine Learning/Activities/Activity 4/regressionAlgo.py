# =============================================================================
# # Kyle A. Destura - BSCS 4A
# # Using the data in the "insurance.csv" file
# # Create a linear regression prediction model 
# # using the AGE and BMI column as values for X and Y 
# # where age is the independent variable "x" and BMI as the dependent variable "y". 
# # Using the developed model, predict the BMI of a person with the following age:
# # 
# # 17 years old
# # 18 years old
# # 19 years old
# # 20 years old
# # 65 years old
# # 66 years old
# # 67 years old
# # 68 years old
# # 69 years old
# # 70 years old
# # =============================================================================



import pandas as pd                                          #for loading csv file data to numpy array
import numpy as np                                             #for using data as array
import matplotlib.pyplot as plt                                 #for plotting graph of x,y
from sklearn import linear_model                              #for model we want to predict by
from sklearn.model_selection import train_test_split        #splitting training and testing sets


insurance = pd.read_csv("Python\csv_files\insurance.csv")

# pandas.loc[] returns Series object
# I can use DataFrame.values() as an alternative as it returns NumPy Array object
condition = ((insurance["age"] >= 17) & (insurance["age"] <= 20)) | ((insurance["age"] >= 60) & (insurance["age"] <= 65)) 
x = insurance.loc[ : , "age"]
y = insurance.loc[ : , "bmi"]
x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 39)

# First Regression Algorithm used. Algorithm taken from the Class Powerpoint.
# Very simple regression algorithm
def get_slope_y_intercept(x, y):
    sum_x = sum(x)
    x_mean = np.mean(x)
    sum_y = sum(y)
    y_mean = np.mean(y)
    
    slope = ((sum_x - x_mean) * (sum_y - y_mean)) / ((sum_x - x_mean) * (sum_x - x_mean))
    
    y_intercept = y_mean - (slope * x_mean)

    return slope, y_intercept

def regression_algorithm(x, slope, y_intercept):
    predictor = []
    
    for i in x:
        calculation = slope*(i) + y_intercept
        predictor.append(calculation)
    
    predictor = np.array(predictor)
    
    return predictor
  
slope, y_intercept = get_slope_y_intercept(x_train, y_train)
linear_regression_predictor = regression_algorithm(x_test, slope, y_intercept)

plt.figure(1)
plt.scatter(x_test,
            y_test,
            edgecolor = "b",
            linewidth = 0.5)
plt.plot(x_test,
         linear_regression_predictor, 
         color = "g") # plotting the regression line


plt.xlabel("Age")
plt.ylabel('BMI')
plt.title("Regression Algorithm (1) from (Class Powerpoint)\nNo Splitting")
plt.show()




# 2nd Algorithm from https://towardsdatascience.com/linear-regression-model-899558ba0fc4
# I have studied and used the code from the tutorial because it also provides the
# details on using the predictive model on a dataset.
# 
# Algorithm :
# 1. Loading the Dataset
# 2. Taking the independent and dependent variable
# 3. Splitting to independent(x) and dependent(y) variables using split
# 4. Choosing the Model
# 5. Using Linear Regression Model
# 6. Fitting the training dataset
# 7. Use the created model to predict.

# Using train_test_split()
# @x,@y are array inputs. It can take many input array for splitting.
# @test_size are the splitting of the dataset
# @random_state takes integer 0-42. Idea is similar to seeding in RNGs
# @returns an array with the length of (array length * 2) each for train and test set of the input


# Reshaping array to convert from 1D to 2D array for the model fitting
x_test = x_test.reshape(-1,1) 
x_train = x_train.reshape(-1,1)

# Creating linear regression model.
linear_regression_model = linear_model.LinearRegression()
linear_regression_model.fit(x_train, y_train)

linear_regression_predictor = linear_regression_model.predict(x_test)

plt.figure(2)
#Plotting the graph for test dataset
plt.scatter(x = x_test, 
            y = y_test,
            edgecolor='b',
            linewidth=0.5)

plt.plot(x_test, 
         linear_regression_predictor, 
         color = 'g',
         linewidth = 0.5)

plt.xlabel("Age")
plt.ylabel("BMI")
plt.title("Regression Algorithm (2) from (towardsdatascience.com)\n1/3 Splitting")
plt.show()




# 3rd algorithm from https://www.geeksforgeeks.org/linear-regression-python-implementation/ 
# This has a lot more specific computation compared to the algorithm in the presentation
# This does not use other libraries.
# This does not split the dataset to training and testing

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
  
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
  
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
  
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
  
    return (b_0, b_1)
  
def plot_regression_line(x, y, b):

    plt.scatter(x,
                y,
                edgecolor = "b",
                linewidth = 0.5)
  
    
    y_pred = b[0] + b[1] * x  # predicted response vector
    plt.plot(x, 
              y_pred, 
              color = "g") # plotting the regression line
    plt.title("Regression Algorithm (3) from (geeksforgeeks.com)\nNo Splitting")
    plt.xlabel("Age")
    plt.ylabel('BMI')
    plt.show()
  
b = estimate_coef(x, y)
plot_regression_line(x, y, b)






# I have also learned that in python, when defining function and variables, 
# the names must be in using the all lowercase separated by underscore. https://peps.python.org/pep-0008/
