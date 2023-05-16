""" Backtesting Trading Strategy using For Loops"""
import pandas as pd
from indicators.ta import *


def backtest():
    year = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
            '2020', '2021', '2022']

    for year_num in range(len(year)):

        df = pd.read_csv('./data/eurusd/H1/' + str(year[year_num]) + '.csv')
        _close = df['close']
        _low = df['low']
        _open = df['open'].shift(1)  # For entry price, shift
        _hl2 = hl2(df)

        tsi_values1, tsi_signal1 = tsi_mod(_close, 12, 26, 19)
        tsi_values2, tsi_signal2 = tsi_mod(_close, 26, 52, 38)
        _sar_up, _sar_down = psar(df, 0.02, 0.2)
        _atr_stoploss = atr(df['high'], _low, _close, 10)

        # Account Info
        account_size = 1000
        trades = 0
        wins = 0

        # Entry & Exit prices
        stoploss = 0
        entry_price = 0
        in_trade = False
        i = 1
        while i < len(_close):

            # Entry conditions
            condition1 = tsi_values1.iloc[i - 1] <= tsi_signal1.iloc[i - 1]
            condition2 = tsi_values1.iloc[i] > tsi_signal1.iloc[i]
            condition3 = tsi_signal2.iloc[i] > 0
            entry = condition1 & condition2 & condition3
            position_size = (account_size * 0.05) * 50

            # Fresh Entry
            if entry & (not in_trade):
                trades += 1
                in_trade = True
                entry_price = _open.iloc[i]
                account_size -= (account_size * 0.05)

                # Set Initial Stoploss
                if _sar_down.iloc[i] is not None:
                    stoploss = _sar_down.iloc[i]
                else:
                    stoploss = entry_price - _atr_stoploss.iloc[i]

            # Opened trade
            if in_trade:

                # To adjust stop loss
                if (_sar_down.iloc[i] is not None) & (_sar_down.iloc[i - 1] is not None):
                    if _sar_down.iloc[i] > _sar_down.iloc[i - 1]:
                        stoploss = _sar_down.iloc[i]

                # If exit trade after stoploss has been hit
                if _low.iloc[i] <= stoploss:
                    in_trade = False  # no more trade open
                    exit_price = stoploss
                    stoploss = 0

                    # Calculate profits
                    profit = (((exit_price - entry_price) / entry_price) * position_size)
                    account_size += profit

                    # Add wins
                    if profit > 0:
                        wins += 1
                        account_size += (account_size * 0.05)

            i += 1

        print(f'\n\nTotal Money: {account_size} at year {str(year[year_num])}')
        print(f'Trades: {trades}')
        print(f'Wins: {wins}')
        print(f'Losses: {trades - wins} ')
        # print(f'Win Rate: {(wins / trades) * 100}% ')


backtest()
