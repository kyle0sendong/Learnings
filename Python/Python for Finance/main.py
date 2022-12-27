""" Main """

from test.mt5.connect import *
from test.indicators.ta import *
from datetime import datetime
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def main():
    login = 65813096
    password = 'maskinanO1'
    server = 'XMGlobal-MT5 2'

    connect_to_mt(login, password, server)

    ohlc_data = pd.DataFrame(mt5.copy_rates_range('EURUSD#',
                                                  mt5.TIMEFRAME_M5,
                                                  datetime(2022, 11, 1),
                                                  datetime(2022, 12, 27)))
    close_data = ohlc_data['close']
    print(close_data)

    ema_values = sma(close_data, 100)
    ohlc_data = ohlc_data.assign(ClosePrice=pd.Series(close_data, index=ohlc_data.index))
    ohlc_data = ohlc_data.assign(EMA=pd.Series(ema_values, index=ohlc_data.index))
    close_price = ohlc_data['ClosePrice']
    ema1 = ohlc_data['EMA']
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax1 = fig.add_subplot(111, ylabel='Price in $')
    close_price.plot(ax=ax1, color='g', lw=2., legend=True)
    ema1.plot(ax=ax1, color='b', lw=2., legend=True)
    plt.savefig('ema.png')
    plt.show()


main()
