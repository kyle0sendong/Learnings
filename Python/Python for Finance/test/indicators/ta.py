""" Exponential Moving Averages """

import pandas as pd
import numpy as np
import statistics as stats


def ema(source, period):
    k = 2 / (period + 1)  # smoothing constant
    ema_p = 0
    ema_values = []
    for source_price in source:
        if ema_p == 0:
            ema_p = source_price
        else:
            ema_p = (source_price - ema_p) * k + ema_p
        ema_values.append(ema_p)
    return ema_values


def sma(source, length):
    history = []
    sma_values = []
    for source_price in source:
        history.append(source_price)
        if len(history) > length:  # remove the oldest price, only average over last 'time_period' prices
            del(history[0])
        sma_values.append(stats.mean(history))
    return sma_values
