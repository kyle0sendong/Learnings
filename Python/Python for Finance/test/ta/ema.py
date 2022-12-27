""" Exponential Moving Averages """

import pandas as pd
import numpy as np


def ema(values, period):
    values = np.array(values)
    return pd.ewma(values, span=period)[-1]

