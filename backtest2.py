""" Main Backtester"""

import numpy as np
from indicators.ta import *

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def backtest():

    year = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
            '2020', '2021', '2022']

    total_profit = 0

    for num in range(len(year)):
        best_rma_length = 0
        best_tsi_slow = 0
        best_tsi_fast = 0
        best_tsi_smooth = 0
        best_account_size = 0
        total_trades = 0
        total_win = 0

        df = pd.read_csv('./data/eurusd/H1/' + str(year[num]) + '.csv')
        close_price = df['close']
        # Test Technical Indicators
        hl2_price = hl2(df)

        for i in range(12, 60):

            total_money_used = 0

            slow = i
            fast = round(i*2.1)
            smooth = round(i*1.6)
            tsi_values, tsi_signal = tsi_mod(hl2_price, slow, fast, smooth)
            long_condition = tsi_values > tsi_signal

            for rma_length in range(1, 6):

                total_account_size = 0

                rma2 = rma(hl2_price, rma_length)
                rma6 = rma(hl2_price, rma_length*3)

                entry = long_condition & (rma2 > rma6)

                # Buy entries
                buy = entry.astype(float)
                buy_shifted = buy.shift(1)

                # Find Opening and Closing Trades
                open_condition = (buy_shifted == 0) & (buy == 1)
                close_condition = (buy_shifted == 1) & (buy == 0)
                df['open_trade'] = np.where(open_condition, close_price, np.nan)
                df['close_trade'] = np.where(close_condition, close_price, np.nan)

                # Drop NaN values then reset index. In this way, only the opening and closing indices are stored.
                open_trades = (df['open_trade'].dropna()).reset_index(drop=True)
                close_trades = (df['close_trade'].dropna()).reset_index(drop=True)

                # To calculate how much loss or profit has been made in each trade.
                profits = ((close_trades - open_trades) / open_trades) * 100
                profits = profits.fillna(0)

                # Risk management
                initial_size = 1000.0
                total_money_used += initial_size
                account_size = initial_size

                trades = 0
                wins = 0

                # Using loop for counting profit/losses
                for j in range(len(open_trades)):

                    trades += 1
                    position_size = (account_size * 0.02) * 100
                    account_size = account_size + ((position_size / 100) * profits[j])

                    if profits[j] > 0:
                        wins += 1

                total_account_size += account_size

                if (total_account_size > best_account_size) & (trades >= 50):
                    best_account_size = total_account_size
                    best_rma_length = rma_length
                    best_tsi_slow = slow
                    best_tsi_fast = fast
                    best_tsi_smooth = smooth
                    total_trades = trades
                    total_win = wins

        total_profit += (best_account_size - 1000)
        print(f'\n\nBest Total Money: {best_account_size} at year {str(year[num])}')
        print(f'Best TSI Value: slow: {best_tsi_slow} fast: {best_tsi_fast} smooth: {best_tsi_smooth} ')
        print(f'Best RMA Value: {best_rma_length}')
        print(f'Trades: {total_trades}')
        print(f'Wins: {total_win}')
        print(f'Losses: {total_trades - total_win} ')
        print(f'Win Rate: {(total_win/total_trades)*100}% ')

    print(f'Total Profit: {total_profit} over the years')


backtest()
