# =============================================================================
# 3. Write a Pandas program to add, subtract, multiple and divide 
# two Pandas Series.
# =============================================================================

import pandas as pd

series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([6, 7, 8, 9, 10])

addTwoSeries = series1 + series2
subtractTwoSeries = series1 - series2
multiplyTwoSeries = series1 * series2
divideTwoSeries = series1/series2

print(addTwoSeries)
print(subtractTwoSeries)
print(multiplyTwoSeries)
print(divideTwoSeries)