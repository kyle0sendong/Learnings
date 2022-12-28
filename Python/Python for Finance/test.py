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
    close = ohlc_data['ClosePrice']
    hl2_ = hl2(ohlc_data)
    fig = plt.figure()

    print(close)
    print(hl2_)
    ax1 = fig.add_subplot(211, ylabel='Test')
    hl2_.plot(ax=ax1, color='b', lw=1., legend=True)

    ax2 = fig.add_subplot(212, ylabel='Test')
    close.plot(ax=ax2, color='b', lw=1., legend=True)

    plt.show()


main()
