# =============================================================================
# 4. Write a Pandas program to compare the elements of the two Pandas Series. 
# =============================================================================

import pandas as pd

series1 = pd.Series([9, 8, 7, 6, 5])
series2 = pd.Series([5, 6, 7, 8, 9])

print("series1 > series2")
print(series1 > series2)

print("\nseries1 < series2")
print(series1 < series2)

print("\nseries1 == series2")
print(series1 == series2)

print("\nseries1 <= series2")
print(series1 <= series2)

print("\nseries1 >= series2")
print(series1 >= series2)
