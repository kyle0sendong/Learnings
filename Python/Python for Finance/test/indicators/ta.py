""" Exponential Moving Averages """

import pandas as pd
from ta.trend import *
from ta.momentum import *


def ema(source, period):
    return ema_indicator(source, period)


def sma(source, length):
    return sma_indicator(source, length)


def tsi_mod(source, slow=12, fast=26, signal=19):
    """ True Strength Index Modified
    Returns rounded TSI value
    Returns TSI Signal Value
    """

    tsi_value = round(tsi(source, slow, fast))
    tsi_signal = round(ema(tsi_value, signal))

    i = 0
    while i < len(tsi_value):

        difference = abs(tsi_value[i] - tsi_signal[i])

        if difference <= 7:
            tsi_value[i] = tsi_signal[i]
            tsi_signal[i] = tsi_value[i]
        i += 1

    return tsi_value, tsi_signal


def psar(high, low, close, step, max_step):
    up = psar_up(high, low, close, step, max_step)
    down = psar_down(high, low, close, step, max_step)
    return up, down
