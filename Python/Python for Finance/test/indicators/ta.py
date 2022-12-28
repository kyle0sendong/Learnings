""" Exponential Moving Averages """

import pandas as pd
from ta.trend import *
from ta.momentum import *


def hl2(source):
    i = 0
    hl2_container = []
    while i < len(source['high']):
        high = source['high'][i]
        low = source['low'][i]
        hl2_value = (high+low) / 2
        hl2_container.append(hl2_value)
        i += 1
    return pd.Series(hl2_container)


def ema(source, period):
    return ema_indicator(source, period)


def sma(source, length):
    return sma_indicator(source, length)


def tsi_mod(source, slow=12, fast=26, signal=19):
    """ True Strength Index Modified
    Returns rounded TSI value
    Returns TSI Signal Value
    """

    tsi_value = round(tsi(hl2(source), slow, fast))
    tsi_signal = round(ema(tsi_value, signal))

    i = 0
    while i < len(tsi_value):

        difference = abs(tsi_value[i] - tsi_signal[i])

        if difference <= 7:
            tsi_value[i] = tsi_signal[i]
            tsi_signal[i] = tsi_value[i]
        i += 1

    return tsi_value, tsi_signal
