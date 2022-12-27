# =============================================================================
# 6. Write a Pandas program to convert a NumPy array to a Pandas series.
# =============================================================================

import numpy as np
import pandas as pd

print("\nEXERCISE 7")
numpyArray1 = np.array([1,2,3,4,5])
print(numpyArray1)

pandasSeries1 = pd.Series(numpyArray1)
print(pandasSeries1)
