# =============================================================================
# 7. Write a Pandas program to change the data type of given a column or a Series.
# =============================================================================

import pandas as pd

print("\nEXERCISE 7")
pandasSeries2 = pd.Series([1,"Two", 3.2, False])
print(pandasSeries2)

# ‘raise’, then invalid parsing will raise an exception
# ‘coerce’, then invalid parsing will be set as NaN
# ‘ignore’, then invalid parsing will return the input
pandasSeries2 = pd.to_numeric(pandasSeries2, errors="coerce")
print(pandasSeries2)
