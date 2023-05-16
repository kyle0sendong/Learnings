""" Save Data to local storage """

from mt5.connect import *
from datetime import datetime
import pandas as pd
from pathlib import Path


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
    elif timeframe == mt5.TIMEFRAME_H4:
        return 'H4'
    elif timeframe == mt5.TIMEFRAME_D1:
        return 'D1'


def save_data_yearly(account_info, start_year, end_year, ticker_name, timeframe):

    connect_to_mt(account_info[0], account_info[1], account_info[2])

    for i in range((end_year-start_year) + 1):
        year = start_year + i
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        df = pd.DataFrame(mt5.copy_rates_range(ticker_name, timeframe, start_date, end_date))
        timeframe_string = get_timeframe_string(timeframe)
        directory = Path('./data/' + ticker_name + '/yearly/' + timeframe_string)

        if not directory.exists():
            directory.mkdir(parents=True)
        else:
            df.to_csv('./data/' + ticker_name + '/yearly/' + timeframe_string + '/' + str(year) + '.csv')


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
