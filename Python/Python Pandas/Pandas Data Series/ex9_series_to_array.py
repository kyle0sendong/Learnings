# =============================================================================
# 9. Write a Pandas program to convert a given Series to an array.
# =============================================================================

import numpy as np
import pandas as pd

print("\nEXERCISE 9")
pandasSeries3 = pd.Series([1, "Two", 3, False])
numpyArray2 = np.array(pandasSeries3)
print(numpyArray2)
print(type(numpyArray2))

# pandasSeries3.values.tolist() converting pandas series to list
# pandasSeries3.to_list() convert pandas series to list
# numpyArray2.tolist() convert numpy array to list
test1 = pandasSeries3.values.tolist()
print(type(test1))
test2 = pandasSeries3.to_list()
print(type(test2))
test3 = numpyArray2.tolist()
print(type(test3))
