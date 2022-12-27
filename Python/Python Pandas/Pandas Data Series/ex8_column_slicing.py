# =============================================================================
# 8. Write a Pandas program to convert the first column of a DataFrame as a Series.
# =============================================================================

import pandas as pd

# ix[] function is removed. use loc[] or iloc[]
# loc[row, column]
# loc[:"c",] = rows up to index c and all column.
# loc[:"d", :"B"] = row up to d and column up to B
# loc["a":"c", "B":"D"] = row a to c and column B to D
# loc[:, "A"] = all row on column A
# loc["a", :] or loc["a"] = all row a
data1 = {
    "A": [65, 96, 1, 2],
    "B": [66, 97, 1, 2],
    "C": [67, 98, 3, 4],
    "D": [68, 99, 5, 6]
}
print("\nEXERCISE 8")
dataFrame1 = pd.DataFrame(data=data1, index=["a", "b", "c", "d"])
print(dataFrame1)
dataFrame1firstColumn = dataFrame1.loc[:, "A"]
print("\n" + str(dataFrame1firstColumn))
