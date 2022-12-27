# Converting categorical variable to numeric variable

import pandas as pd
 
# read csv
df = pd.read_csv('Python/csv_files/insurance.csv')
 
# get the dummies and store it in a variable
dummies = pd.get_dummies(df.smoker)

# Concatenate the dummies to original dataframe
merged = pd.concat([df, dummies], axis='columns')
 
# drop the values
# df = merged.drop(['no', 'smoker'], axis='columns')
 
# print the dataframe
print(merged)



# Using DataFrame.replace() method
# df['region'].replace(['southeast', 'southwest',
#                       'northeast', 'northwest'],
#                         [0, 1, 2, 3], inplace=True)

# print(df)
