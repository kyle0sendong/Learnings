import numpy as np
import pandas as pd
# axis = 0, cumulative sum in column wise
# axis = 1, cumulative sum in row wise
df = pd.DataFrame([[True, True, False, True, False],
                   [False, False, False, True, True],
                   [True, True, True, True, True]])

df.rename(columns={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}, inplace=True)
arr1 = np.cumsum(df, axis=1) == 1
cumsum = df[arr1]
print(cumsum)

# Transpose
cumsum = cumsum.T
print(cumsum)