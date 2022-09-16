import numpy as np
import pandas as pd

# =============================================================================
# 6. Write a Pandas program to convert a NumPy array to a Pandas series.
# =============================================================================
print("\nEXERCISE 7")
numpyArray1 = np.array([1,2,3,4,5])
print(numpyArray1)

pandasSeries1 = pd.Series(numpyArray1)
print(pandasSeries1)


# =============================================================================
# 7. Write a Pandas program to change the data type of given a column or a Series.
# =============================================================================
print("\nEXERCISE 7")
pandasSeries2 = pd.Series([1,"Two", 3.2, False])
print(pandasSeries2)

#‘raise’, then invalid parsing will raise an exception
#‘coerce’, then invalid parsing will be set as NaN
#‘ignore’, then invalid parsing will return the input
pandasSeries2 = pd.to_numeric(pandasSeries2, errors="coerce")
print(pandasSeries2)


# =============================================================================
# 8. Write a Pandas program to convert the first column of a DataFrame as a Series.
# =============================================================================
#ix[] function is removed. use loc[] or iloc[]
#loc[row, column]
#conditions for loc[] 
# loc[:"c",] = rows up to index c and all column.
# loc[:"d", :"B"] = row up to d and column up to B
# loc["a":"c", "B":"D"] = row a to c and column B to D
# loc[:, "A"] = all row on column A
# loc["a", :] or loc["a"] = all row a
data1 = {
    "A" : [65, 96, 1, 2],
    "B" : [66, 97, 1, 2],
    "C" : [67, 98, 3, 4],
    "D" : [68, 99, 5, 6]
}
print("\nEXERCISE 8")
dataFrame1 = pd.DataFrame(data=data1, index=["a", "b", "c", "d"])
print(dataFrame1)
dataFrame1firstColumn = dataFrame1.loc[:, "A"]
print("\n" + str(dataFrame1firstColumn))


# =============================================================================
# 9. Write a Pandas program to convert a given Series to an array.
# =============================================================================

print("\nEXERCISE 9")
pandasSeries3 = pd.Series([1, "Two", 3, False])
numpyArray2 = np.array(pandasSeries3)
print(numpyArray2)
print(type(numpyArray2))

#pandasSeries3.values.tolist() converting pandas series to list
#pandasSeries3.to_list() convert pandas series to list
#numpyArray2.tolist() convert numpy array to list
test1 = pandasSeries3.values.tolist()
print(type(test1))
test2 = pandasSeries3.to_list()
print(type(test2))
test3 = numpyArray2.tolist()
print(type(test3))
























