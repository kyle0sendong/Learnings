""" Main """

from test.mt5.connect import *
from test.indicators.ta import *
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def main():
    login = 65813096
    password = 'maskinanO1'
    server = 'XMGlobal-MT5 2'

    connect_to_mt(login, password, server)

    ohlc_data = pd.DataFrame(mt5.copy_rates_range('EURUSD#',
                                                  mt5.TIMEFRAME_D1,
                                                  datetime(2012, 1, 1),
                                                  datetime(2022, 12, 27)))

    ohlc_data = ohlc_data.assign(ClosePrice=pd.Series(ohlc_data['close'], index=ohlc_data.index))
    close_price = ohlc_data['ClosePrice']

    ema_values = ema(close_price, 100)
    ohlc_data = ohlc_data.assign(EMA=pd.Series(ema_values, index=ohlc_data.index))
    ema_values = ohlc_data['EMA']

    tsi_slow = 12
    tsi_fast = 26
    tsi_smooth = 19
    tsi_values, tsi_signal = tsi_mod(ohlc_data, tsi_slow, tsi_fast, tsi_smooth)
    ohlc_data = ohlc_data.assign(TSI=pd.Series(tsi_values, index=ohlc_data.index))
    ohlc_data = ohlc_data.assign(TSISignal=pd.Series(tsi_signal, index=ohlc_data.index))
    tsi_values = ohlc_data['TSI']
    tsi_signal = ohlc_data['TSISignal']

    fig = plt.figure()

    ax1 = fig.add_subplot(211, ylabel='Price')
    close_price.plot(ax=ax1, color='yellow', lw=0.5, legend=True)
    ema_values.plot(ax=ax1, color='b', lw=0.5, legend=True)

    ax2 = fig.add_subplot(212, ylabel='TSI')
    tsi_values.plot(ax=ax2, color='green', lw=0.5, legend=True)
    tsi_signal.plot(ax=ax2, color='red', lw=0.5, legend=True)
    plt.show()


main()
