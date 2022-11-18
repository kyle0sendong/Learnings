'''
Kyle A. Destura BSCS 4A
Activity 3. Reading CSV File and Displaying the Data in the Form of Scatter Plot

1. Using Pandas Library, Read the CSV file 'insurance.csv' of Python.  
2. Using MatPlotLib Library, Display the columns 'Age' and 'BMI' as an X & Y pair in a Scatter Plot
3. Using MatPlotLib Library, Display the ratio of Male to Female in the form of Pie Chart
4. Use NumPy to compute for the Mean of the AGE and BMI column and display the results on the screen.

The intention of this activity is to allow the students to be acquainted with the basics of Python Programming 
which will become the primary programming tool for this Machine Learning Class
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

insurance = pd.DataFrame(pd.read_csv('Python\csv_files\insurance.csv'))

plt.figure(1)
age = pd.to_numeric(insurance['age'])
bmi = pd.to_numeric(insurance['bmi'])

plt.scatter(
    x = age, 
    y = bmi,
    facecolor='none',
    edgecolor='r',
    linewidth=0.8)

plt.xlabel('Age')
plt.ylabel('BMI')

agebmiMean = np.mean([age, bmi])
print('\nAge and BMI Mean: ' + str(round(agebmiMean, 2)))

plt.figure(2)
maleCount = insurance['sex'].value_counts()['male']
femaleCount = insurance['sex'].value_counts()['female']

plt.pie(
    x = [maleCount, femaleCount],
    labels = ['male', 'female'],
    autopct = '%0.2f%%',
    startangle = 90,
    explode = [0.05, 0],
    shadow = True,
    colors = ['#87ceeb', 'pink'])

plt.title('Distribution of Sex')
plt.legend()
plt.show()
