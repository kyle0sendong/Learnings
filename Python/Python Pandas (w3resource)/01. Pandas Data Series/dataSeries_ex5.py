# =============================================================================
# 5. Write a Pandas program to convert a dictionary to a Pandas series.
# =============================================================================

import pandas as pd

myDict = {
    "A" : 65,
    "B" : 66,
    "C" : 67,
    "D" : 68,
    "E" : 69
}

series = pd.Series(myDict)

print(series)