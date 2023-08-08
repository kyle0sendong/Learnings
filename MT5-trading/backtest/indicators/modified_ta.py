import MetaTrader5 as mt5
import pandas as pd
from ta.momentum import tsi
from ta.trend import ema_indicator, sma_indicator, psar_up, psar_down
from ta.volatility import average_true_range


def get_timeframe_string(timeframe):
    if timeframe == mt5.TIMEFRAME_M1:
        return 'M1'
    elif timeframe == mt5.TIMEFRAME_M5:
        return 'M5'
    elif timeframe == mt5.TIMEFRAME_M15:
        return 'M15'
    elif timeframe == mt5.TIMEFRAME_M30:
        return 'M30'
    elif timeframe == mt5.TIMEFRAME_H1:
        return 'H1'
    elif timeframe == mt5.TIMEFRAME_H2:
        return 'H2'
    elif timeframe == mt5.TIMEFRAME_H4:
        return 'H4'
    elif timeframe == mt5.TIMEFRAME_D1:
        return 'D1'


def hl2(ohlc):
    i = 0
    hl2_container = []
    while i < len(ohlc['high']):
        high = ohlc['high'][i]
        low = ohlc['low'][i]
        hl2_value = (high+low) / 2
        hl2_container.append(hl2_value)
        i += 1
    return pd.Series(hl2_container)


def nz(x, y=None):
    """
    RETURNS
    Two args version: returns x if it's a valid (not NaN) number, otherwise y
    One arg version: returns x if it's a valid (not NaN) number, otherwise 0
    ARGUMENTS
    x (val) Series of values to process.
    y (float) Value that will be inserted instead of all NaN values in x series.
    """

    if x != x:
        if y is not None:
            return y
        return 0
    return x


def ema(source, period):
    return ema_indicator(source, period)


def sma(source, length):
    return sma_indicator(source, length)


def rma(source, length):
    rma_container = []
    alpha = 1/length
    sum_ = 0
    i = 0
    while i < len(source):
        prev_sum = sum_
        sum_ = alpha*source[i] + (1 - alpha)*nz(prev_sum)
        rma_container.append(sum_)
        i += 1

    return pd.Series(rma_container)


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
    """Parabolic SAR

    Returns Psar Up and Psar Down
    """
    up = psar_up(high, low, close, step, max_step)
    down = psar_down(high, low, close, step, max_step)
    return up, down


def coral(source, sm, cd):
    source_len = len(source)
    i1 = [0] * source_len
    i2 = [0] * source_len
    i3 = [0] * source_len
    i4 = [0] * source_len
    i5 = [0] * source_len
    i6 = [0] * source_len

    di = (sm - 1.0) / 2.0 + 1.0
    c1 = 2 / (di + 1.0)
    c2 = 1 - c1
    c3 = 3.0 * (cd * cd + cd * cd * cd)
    c4 = -3.0 * (2.0 * cd * cd + cd + cd * cd * cd)
    c5 = 3.0 * cd + 1.0 + cd * cd * cd + 3.0 * cd * cd

    bfr = [] * source_len
    bfr_up = [] * source_len
    bfr_down = [] * source_len

    i = 1
    while i < source_len:

        i1[i] = c1 * source[i] + c2 * nz(i1[i-1])
        i2[i] = c1 * i1[i] + c2 * nz(i2[i-1])
        i3[i] = c1 * i2[i] + c2 * nz(i3[i-1])
        i4[i] = c1 * i3[i] + c2 * nz(i4[i-1])
        i5[i] = c1 * i4[i] + c2 * nz(i5[i-1])
        i6[i] = c1 * i5[i] + c2 * nz(i6[i-1])

        bfr.append(-cd * cd * cd * i6[i] + (c3*i5[i]) + (c4*i4[i]) + (c5*i3[i]))

        if bfr[i-1] > nz(bfr[i-2]):
            bfr_up.append(bfr[i-1])
            bfr_down.append(None)
        else:
            bfr_down.append(bfr[i-1])
            bfr_up.append(None)

        i += 1

    bfr_up = pd.Series(bfr_up)
    bfr_down = pd.Series(bfr_down)

    return bfr_up, bfr_down


def atr(high, low, close, length):
    return average_true_range(high, low, close, length)
