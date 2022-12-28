""" Main """

from test.mt5.connect import *
from test.indicators.ta import *
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


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


def main():
    login = 65813096
    password = 'maskinanO1'
    server = 'XMGlobal-MT5 2'

    connect_to_mt(login, password, server)

    ohlc_data = pd.DataFrame(mt5.copy_rates_range('EURUSD#',
                                                  mt5.TIMEFRAME_D1,
                                                  datetime(2012, 1, 1),
                                                  datetime(2022, 12, 27)))

    ohlc_data = ohlc_data.assign(OpenPrice=pd.Series(ohlc_data['open'], index=ohlc_data.index))
    ohlc_data = ohlc_data.assign(HighPrice=pd.Series(ohlc_data['high'], index=ohlc_data.index))
    ohlc_data = ohlc_data.assign(LowPrice=pd.Series(ohlc_data['low'], index=ohlc_data.index))
    ohlc_data = ohlc_data.assign(ClosePrice=pd.Series(ohlc_data['close'], index=ohlc_data.index))
    open_price = ohlc_data['OpenPrice']
    high_price = ohlc_data['HighPrice']
    low_price = ohlc_data['LowPrice']
    close_price = ohlc_data['ClosePrice']
    hl2_price = hl2(ohlc_data)

    ema_length = 100
    ema_values = ema(close_price, ema_length)
    ohlc_data = ohlc_data.assign(EMA=pd.Series(ema_values, index=ohlc_data.index))
    ema_values = ohlc_data['EMA']

    tsi_slow = 12
    tsi_fast = 26
    tsi_smooth = 19
    tsi_values, tsi_signal = tsi_mod(hl2_price, tsi_slow, tsi_fast, tsi_smooth)
    ohlc_data = ohlc_data.assign(TSI=pd.Series(tsi_values, index=ohlc_data.index))
    ohlc_data = ohlc_data.assign(TSISignal=pd.Series(tsi_signal, index=ohlc_data.index))
    tsi_values = ohlc_data['TSI']
    tsi_signal = ohlc_data['TSISignal']

    psar_increment = 0.06
    psar_maximum = 0.035
    psar_up, psar_down = psar(high_price, low_price, close_price, psar_increment, psar_maximum)

    fig = plt.figure()

    ax1 = fig.add_subplot(211, ylabel='Price')
    ax1.set_facecolor('xkcd:black')
    close_price.plot(ax=ax1, color='green', lw=0.7, legend=True)
    ema_values.plot(ax=ax1, color='b', lw=0.7, legend=True)
    psar_up.plot(ax=ax1, color='green', lw=0.7, legend=True)
    psar_down.plot(ax=ax1, color='red', lw=0.7, legend=True)

    ax2 = fig.add_subplot(212, ylabel='TSI')
    ax2.set_facecolor('xkcd:black')
    tsi_values.plot(ax=ax2, color='green', lw=0.7, legend=True)
    tsi_signal.plot(ax=ax2, color='red', lw=0.7, legend=True)
    plt.show()


main()
