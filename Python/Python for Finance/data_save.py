""" Save Data to local storage """

from mt5.connect import *
from datetime import datetime
import pandas as pd


def main():
    login = 65813096
    password = 'maskinanO1'
    server = 'XMGlobal-MT5 2'

    connect_to_mt(login, password, server)
    ticker_name = 'BTCUSD#'
    ticker_timeframe = mt5.TIMEFRAME_H1

    start_date = [datetime(2014, 1, 1), datetime(2015, 1, 1), datetime(2016, 1, 1), datetime(2017, 1, 1), datetime(2018, 1, 1),
                  datetime(2019, 1, 1), datetime(2020, 1, 1), datetime(2021, 1, 1), datetime(2022, 1, 1)]
    
    end_date = [datetime(2014, 12, 31),
                datetime(2015, 12, 31), datetime(2016, 12, 31), datetime(2017, 12, 31), datetime(2018, 12, 31), 
                datetime(2019, 12, 31), datetime(2020, 12, 31), datetime(2021, 12, 31), datetime(2022, 12, 31)]
    year = ['2014', '2015', '2016', '2017', '2018', '2019',
            '2020', '2021', '2022']
    # start_date = [datetime(2007, 1, 1), datetime(2008, 1, 1), datetime(2009, 1, 1), datetime(2010, 1, 1),
    #               datetime(2011, 1, 1), datetime(2012, 1, 1), datetime(2013, 1, 1), datetime(2014, 1, 1),
    #               datetime(2015, 1, 1), datetime(2016, 1, 1), datetime(2017, 1, 1), datetime(2018, 1, 1),
    #               datetime(2019, 1, 1), datetime(2020, 1, 1), datetime(2021, 1, 1), datetime(2022, 1, 1)]
    #
    # end_date = [datetime(2007, 12, 31), datetime(2008, 12, 31), datetime(2009, 12, 31), datetime(2010, 12, 31),
    #             datetime(2011, 12, 31), datetime(2012, 12, 31), datetime(2013, 12, 31), datetime(2014, 12, 31),
    #             datetime(2015, 12, 31), datetime(2016, 12, 31), datetime(2017, 12, 31), datetime(2018, 12, 31),
    #             datetime(2019, 12, 31), datetime(2020, 12, 31), datetime(2021, 12, 31), datetime(2022, 12, 31)]
    # year = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
    #         '2020', '2021', '2022']

    for i in range(len(year)):
        df = pd.DataFrame(mt5.copy_rates_range(ticker_name, ticker_timeframe, start_date[i], end_date[i]))
        df.to_csv('./data/btcusd/H1/'+str(year[i])+'.csv')


main()
