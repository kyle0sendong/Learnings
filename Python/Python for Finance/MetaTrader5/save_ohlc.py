"""Saving oh OHLC data to csv"""

from connect import *
from datetime import datetime
import pandas as pd


def main():
    login = 65813096
    password = 'maskinanO1'
    server = 'XMGlobal-MT5 2'

    connect_to_mt(login, password, server)

    ohlc_data = pd.DataFrame(mt5.copy_rates_range('EURUSD#',
                                                  mt5.TIMEFRAME_M5,
                                                  datetime(2022, 6, 1),
                                                  datetime(2022, 12, 1)))
    print(ohlc_data)


main()
