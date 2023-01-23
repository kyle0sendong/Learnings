""" Main Backtester"""

from mt5.connect import *
from indicators.ta import *
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def main():
    year = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
            '2020', '2021', '2022']

    for num in range(len(year)):
        df = pd.read_csv('./data/eurusd/H1/'+str(year[num])+'.csv')

        # Technical Indicators
        hl2_price = hl2(df)
        sma40_length = 400

        rma2_length = 2
        rma6_length = 6

        tsi_slow = 12
        tsi_fast = 26
        tsi_smooth = 19

        sar_increment = 0.05
        sar_maximum = 0.02

        coral_length = 21
        coral_multiplier = 0.8

        atr_length = 5

        sma40 = rma(df['close'], sma40_length)
        rma2 = rma(df['close'], rma2_length)
        rma6 = rma(df['close'], rma6_length)
        tsi_values, tsi_signal = tsi_mod(hl2_price, tsi_slow, tsi_fast, tsi_smooth)
        sar_up, sar_down = psar(df['high'], df['low'], df['close'], sar_increment, sar_maximum)
        coral_up, coral_down = coral(df['close'], coral_length, coral_multiplier)
        atr5 = atr(df['high'], df['low'], df['close'], atr_length)

        # Long Entry Conditions
        long_condition1 = (coral_up is not None) | ((coral_up is None) & (sar_up is not None))
        long_condition2 = rma2 > rma6
        long_condition3 = sar_up is not None
        long_condition4 = tsi_values > tsi_signal
        long_condition5 = df['close'] >= sma40
        entry1 = long_condition1 & long_condition2 & long_condition3 & long_condition4

        # Long Entry Conditions
        long_condition2 = df.close > sma40
        entry2 = long_condition1 & long_condition2 & long_condition3 & long_condition4

        # Buy entries
        buy = entry1.astype(float)
        buy_shifted = buy.shift(1)

        # Find Opening and Closing Trades
        open_condition = (buy_shifted == 0) & (buy == 1)
        close_condition = (buy_shifted == 1) & (buy == 0)
        df['open_trade'] = np.where(open_condition, df['close'], np.nan)
        df['close_trade'] = np.where(close_condition, df['close'], np.nan)

        # Drop NaN values then reset index. In this way, only the opening and closing indices are stored. Saves memory
        open_trades = (df['open_trade'].dropna()).reset_index(drop=True)
        close_trades = (df['close_trade'].dropna()).reset_index(drop=True)

        # Used for calculating position size
        df['low_entry'] = np.where(open_trades is not None, df['low'], np.nan)
        df['atr5_entry'] = np.where(open_trades is not None, atr5, np.nan)
        low_entry = (df['low_entry'].dropna()).reset_index(drop=True)
        atr5_entry = (df['atr5_entry'].dropna()).reset_index(drop=True)

        # To calculate how much loss or profit has been made in each trade.
        profits = ((close_trades - open_trades)/open_trades) * 100
        profits = profits.fillna(0)

        # Risk management
        initial_size = 1000.0
        account_size = initial_size
        risk_per_trade = 0.02

        # Trading Data
        maximum_profit = 1000
        win = 0
        num_trades = len(profits)
        savings = 0.0

        # Using loop for counting profit/losses
        for i in range(len(open_trades)):

            stop_loss_position = low_entry[i] - (atr5_entry[i] * 2)
            stop_loss_percentage = (open_trades[i]-stop_loss_position) / open_trades[i]
            position_size = (account_size*risk_per_trade) / abs(stop_loss_percentage*10)

            if position_size > (account_size / 4):
                position_size = account_size / 4

            account_size = account_size + (position_size*profits[i])

            if profits[i] > 0:
                win = win + 1
                temp_savings = (position_size * profits[i]) * 0.2  # save 10% of every win
                savings += temp_savings
                account_size -= temp_savings

            if account_size > maximum_profit:
                maximum_profit = account_size

        print(f'{year[num]}')
        print(f'Account Size: ${account_size:.2f}')
        print(f'Total Savings: ${savings}')
        print(f'potential profit: ${maximum_profit:.2f}')
        print(f'win rate: {win/num_trades * 100}%')
        print(f'number of trades: {num_trades}')
        print(f'Total Profit : {(account_size + savings) - initial_size}\n\n')

    """
    Todo: 
        1. Stop loss problem and position sizing
        2. Optimize trading strategy
    """

    # # Display Indicators
    # fig = plt.figure()
    #
    # # Price + EMA + PSAR Plot
    # ax1 = fig.add_subplot(311, ylabel='Price')
    # ax1.set_facecolor('xkcd:black')
    # df.close.plot(ax=ax1, color='green', lw=0.7, legend=True)
    # sma40.plot(ax=ax1, color='b', lw=0.7, legend=True)
    # sar_up.plot(ax=ax1, color='green', lw=0.7, legend=True)
    # sar_down.plot(ax=ax1, color='red', lw=0.7, legend=True)
    #
    # # TSI Plot
    # ax2 = fig.add_subplot(312, ylabel='TSI')
    # ax2.set_facecolor('xkcd:black')
    # tsi_values.plot(ax=ax2, color='green', lw=0.7, legend=True)
    # tsi_signal.plot(ax=ax2, color='red', lw=0.7, legend=True)
    #
    # # Coral Plot
    # ax3 = fig.add_subplot(313, ylabel='Coral')
    # ax3.set_facecolor('xkcd:black')
    # coral_up.plot(ax=ax3, color='green', lw=0.7, legend=True)
    # coral_down.plot(ax=ax3, color='red', lw=0.7, legend=True)
    #
    # plt.show()


main()
