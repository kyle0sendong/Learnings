import numpy as np


def nz(x, y=None):
    """
    RETURNS
    Two args version: returns x if it's a valid (not NaN) number, otherwise y
    One arg version: returns x if it's a valid (not NaN) number, otherwise 0
    ARGUMENTS
    x (val) Series of values to process.
    y (float) Value that will be inserted instead of all NaN values in x series.
    """
    if isinstance(x, np.generic):

        return x.fillna(y or 0)
    if x != x:
        if y is not None:
            return y
        return 0
    return x
