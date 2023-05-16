""" Save Data to local storage """

from mt5.connect import *
from datetime import datetime
import pandas as pd
from pathlib import Path


def save_data_yearly(account_info, start_year, end_year, ticker_name, timeframe):

    connect_to_mt(account_info[0], account_info[1], account_info[2])

    for i in range(end_year-start_year):
        year = start_year + i - 1
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        df = pd.DataFrame(mt5.copy_rates_range(ticker_name, timeframe, start_date, end_date))

        directory = Path('./data/' + ticker_name + '/yearly/' + str(timeframe))

        if not directory.exists():
            directory.mkdir(parents=True)
        else:
            df.to_csv('./data/' + ticker_name + '/yearly/' + str(timeframe) + '/' + str(year) + '.csv')


def save_data_monthly(start_year, end_year, start_month, end_month, ticker_name, timeframe):
    directory = Path('./ticker_name/monthly/' + str(timeframe))

    if not directory.exists():
        directory.mkdir(parents=True)


def save_data_daily(start_year, end_year, start_month, end_month, start_day, end_day, ticker_name, timeframe):
    directory = Path('./ticker_name/daily/' + str(timeframe))

    if not directory.exists():
        directory.mkdir(parents=True)


def main():
    login = 65813096
    password = 'maskinanO1'
    server = 'XMGlobal-MT5 2'
    account_info = [login, password, server]

    ticker_name = 'EURJPY#'
    ticker_timeframe = mt5.TIMEFRAME_H1

    save_data_yearly(account_info, 2021, 2023, ticker_name, ticker_timeframe)


main()
