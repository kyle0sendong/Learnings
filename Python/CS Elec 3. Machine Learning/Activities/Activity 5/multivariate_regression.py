# =============================================================================
# In Multivariate Regression Algorithm, some of the input variables do not have number values 
# which are not usable in creating the Regression Models. Examples of these are Sex, Address, Color, etc. These are called categorical data.  
# To use these information as part of the historical data, dummy data are created to represent these information using values.  
# For sex, 1 may be used to represent Males, and 0 for females.  
# For colors, number may also be assigned for each.  
# In this way, the information may be used in regression analysis and will make prediction possible.  
# In the previously posted sample data set (insurance.csv), 
# create a Multivariate Regression Analysis model that could 
# predict the possible insurance charge based on age, sex, bmi, number of children, whether smoker or not, and location address as input variables.  
# Create a dummy data for columns with categorical data (sex, smoker, region) in order to make it possible for regression analysis to work.  
# Make sample predictions using random inputs to check for the capability of the model to make predictions.  
# Submit a minimum of 10 screenshots of your sample runs in the link provided.   
# =============================================================================


#to do tomorrow - convert to int first using bin and convert to numerical
#multivariate algorithm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sys
np.set_printoptions(threshold=sys.maxsize)
import seaborn as sns
#get multiple slopes m1 m2 m3 m4 using slope formula 
#after getting slopes of each variable, using mean of x and y and slope, get the y intercept 
#to make a predictor, use the formula y = m1x1 + m2x2 ... mnxn + b

def get_y_intercept(slope, x, y):
    y_intercept = 0
    y_mean = np.mean(y)

    if len(x.shape) > 1:
        mx = 0
        for i in range(len(x)):
            x_mean = np.mean(x[i])
            mx += (slope[i] * x_mean)
            
        y_intercept = y_mean - mx
    else:
        x_mean = np.mean(x)
        y_intercept = y_mean - (slope * x_mean)
        
    return y_intercept

def get_slope(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = 0
    denominator = 0

    for i in range(len(x)):
        numerator += (x[i] - x_mean) * (y[i] - y_mean)
        denominator += ((x[i] - x_mean) ** 2)
    
    slope = numerator/denominator
    return slope

def get_slope_y_intercept(x, y):
    slope = get_slope(x, y)
    y_intercept = get_y_intercept(slope, x, y)
    return slope, y_intercept
    
def multivariate_regression(x, slope, y_intercept):
    predictor = []
    
    for i in range(len(x[0])):
        mx = 0
        for j in range(len(x)):  #m1x1 + m2x2 ... mnxn
            mx += slope * x[j, i]
            
        calculation = mx + y_intercept
        predictor.append(calculation)
        
    predictor = np.array(predictor)
    return predictor

def main(): 
    insurance = pd.DataFrame(pd.read_csv('insurance.csv')).sample(frac=0.3,random_state=69)

    # Converting category variable to numeric variable using DataFrame.replace()
    insurance['sex'].replace(to_replace = ['male', 'female'],
                             value = [0, 1],
                             inplace = True)
    
    insurance['smoker'].replace(to_replace = ['yes', 'no'],
                                value = [0, 1],
                                inplace = True)
    
    insurance['region'].replace(to_replace = ['northeast', 'northwest', 'southeast', 'southwest'],
                                value = [0, 1, 2, 3],
                                inplace = True)

    insurance = insurance.astype({'sex':'int64', 'smoker':'int64', 'region':'int64'})
    x = (np.array(insurance['age']), insurance['sex'], insurance['bmi'], insurance['children'], insurance['smoker'])
    y = insurance.loc[ : , 'charges']
    x = np.array(x)
    y = np.array(y)
    
    m = []
    for i in range (len(x)):
        slope = get_slope(x[i], y)
        m.append(slope)
    
    b = get_y_intercept(m, x, y)
    predictor = multivariate_regression(x, slope, b)
    
    plt.scatter(y,
                predictor,
                edgecolor = 'b',
                linewidth = 0.5)
    
    # plt.plot(y,
    #           predictor, 
    #           color = 'g')

    plt.xlabel('Multivariable')
    plt.ylabel('Charges')
    plt.title('Regression Algorithm')
    plt.show()

    sns.regplot(x=y,y=predictor,ci=None,color ='red');

    
if __name__ == "__main__": 
    main()



# In converting category variable to numeric variable, I can use Pandas.get_dummies(DataFrame.column_name)
# the problem with get_dummies is that it only labels category as 1 and 0 and creates a dummy column
# I used DataFrame['column_name'].replace instead.



# insurance['sex'] = insurance['sex'].astype('category')
# insurance['smoker'] = insurance['smoker'].astype('category')
# insurance['region'] = insurance['region'].astype('category')