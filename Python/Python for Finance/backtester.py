""" Main """

from test.mt5.connect import *
from test.indicators.ta import *
from datetime import datetime
import pandas as pd
import backtrader as bt
from matplotlib import *
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def main():
    login = 65813096
    password = 'maskinanO1'
    server = 'XMGlobal-MT5 2'

    connect_to_mt(login, password, server)

    ohlc_data = pd.DataFrame(mt5.copy_rates_range('EURUSD#',
                                                  mt5.TIMEFRAME_H1,
                                                  datetime(2022, 1, 1),
                                                  datetime(2022, 12, 27)))

    del ohlc_data['spread']
    del ohlc_data['real_volume']

    ohlc_data.rename(columns={'time': 'timestamp', 'tick_volume': 'volume'}, inplace=True)
    ohlc_data['timestamp'] = pd.to_datetime(ohlc_data['timestamp'], unit='s')
    ohlc_data.set_index('timestamp', inplace=True)

    cerebro = bt.Cerebro()
    feed = bt.feeds.PandasData(dataname=ohlc_data)
    cerebro.adddata(feed)
    cerebro.run()
    cerebro.plot()

main()
