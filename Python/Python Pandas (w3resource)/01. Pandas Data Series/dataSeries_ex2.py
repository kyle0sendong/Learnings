# =============================================================================
# 2. Write a Pandas program to convert a Panda module Series to Python list 
# and it's type.
# =============================================================================

import pandas as pd

series = pd.Series([1,2,3,4,5,6,7])

seriesToList = series.tolist()

print(seriesToList)
print(type(seriesToList))