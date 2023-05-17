""" Save Data to local storage """

from mt5.connect import *
from datetime import datetime
import pandas as pd
from pathlib import Path
import calendar


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


def is_directory_exist(path):
    directory = Path(path)

    if not directory.exists():
        directory.mkdir(parents=True)

    if directory.exists():  # Double check
        return True


def save_data(account_info, ticker_name, timeframe,
              start_year, end_year,
              start_month=0, end_month=0,
              monthly=False, daily=False):
    connect_to_mt(account_info[0], account_info[1], account_info[2])

    for year in range(start_year, end_year+1):

        timeframe_string = get_timeframe_string(timeframe)

        # Record Yearly
        if (not monthly) & (not daily):

            path = './data/' + ticker_name + '/' + timeframe_string + '/yearly'

            if is_directory_exist(path):
                start_date = datetime(year, 1, 1)
                end_date = datetime(year, 12, 31)
                df = pd.DataFrame(mt5.copy_rates_range(ticker_name, timeframe, start_date, end_date))

                if len(df) > 5:  # Save only if df contains data
                    df.to_csv('./data/'
                              + ticker_name
                              + '/'
                              + timeframe_string
                              + '/yearly/'
                              + str(year)
                              + '.csv')

        # Record monthly
        if monthly:

            path = './data/' + ticker_name + '/' + timeframe_string + '/monthly/' + str(year)

            if is_directory_exist(path):
                for j in range(1, 13):
                    num_days = calendar.monthrange(year, j)[1]  # Take number of days each month
                    start_date = datetime(year, j, 1)
                    end_date = datetime(year, j, num_days)

                    df = pd.DataFrame(mt5.copy_rates_range(ticker_name, timeframe, start_date, end_date))

                    if len(df) > 5:  # Save only if df contains data
                        df.to_csv('./data/'
                                  + ticker_name
                                  + '/'
                                  + timeframe_string
                                  + '/monthly/'
                                  + str(year)
                                  + '/'
                                  + str(j)
                                  + '.csv')

        # Record daily
        if daily:
            if start_month > 0:

                for month in range(start_month, end_month + 1):

                    path = './data/' + ticker_name + '/' + timeframe_string + '/daily/' + str(year) + '/' + str(month) + '/'

                    if is_directory_exist(path):
                        num_days = calendar.monthrange(year, month)[1]  # Take number of days each month

                        for day in range(1, num_days):
                            start_date = datetime(year, month, day)
                            end_date = datetime(year, month, day+1)
                            df = pd.DataFrame(mt5.copy_rates_range(ticker_name, timeframe, start_date, end_date))

                            if len(df) > 5:   # Save only if df contains data
                                df.to_csv('./data/'
                                          + ticker_name
                                          + '/'
                                          + timeframe_string
                                          + '/daily/'
                                          + str(year)
                                          + '/'
                                          + str(month)
                                          + '/'
                                          + str(day)
                                          + '.csv')


def main():
    login = 65813096
    password = 'maskinanO1'
    server = 'XMGlobal-MT5 2'
    account_info = [login, password, server]

    ticker_name = 'EURJPY#'
    ticker_timeframe = mt5.TIMEFRAME_M1

    save_data(account_info, ticker_name, ticker_timeframe,
              start_year=2023, end_year=2023,
              start_month=2, end_month=5,
              daily=True)


main()
