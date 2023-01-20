""" Main Backtester"""

from mt5.connect import *
from indicators.ta import *
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

    df = pd.DataFrame(mt5.copy_rates_range('EURUSD#', mt5.TIMEFRAME_D1, datetime(2012, 1, 1),
                                           datetime(2022, 12, 27)))

    hl2_price = hl2(df)

    df.rename(columns={'tick_volume': 'volume'}, inplace=True)
    df['time'] = pd.to_datetime(df.time, unit='s')
    # Smoothed Moving Average (SMA)
    sma40 = sma(df['close'], 40)
    df = df.assign(SMA40=sma40)

    #Relative Moving Average
    rma2 = rma(df['close'], 2)
    rma6 = rma(df['close'], 6)
    df = df.assign(RMA2=rma2)
    df = df.assign(RMA6=rma6)

    # True Strength Index (TSI)
    tsi_slow = 12
    tsi_fast = 26
    tsi_smooth = 19
    tsi_values, tsi_signal = tsi_mod(hl2_price, tsi_slow, tsi_fast, tsi_smooth)
    df = df.assign(TSI=tsi_values)
    df = df.assign(TSISignal=tsi_signal)

    # Parabolic SAR
    psar_increment = 0.06
    psar_maximum = 0.035
    sar_up, sar_down = psar(df['high'], df['low'], df['close'], psar_increment, psar_maximum)
    df = df.assign(PSARUP=sar_up)
    df = df.assign(PSARDOWN=sar_down)

    # Coral
    coral_length = 20
    coral_multiplier = 0.7
    coral_up, coral_down = coral(df['close'], coral_length, coral_multiplier)
    df = df.assign(CORALUP=coral_up)
    df = df.assign(CORALDOWN=coral_down)

    long_condition1 = df.CORALUP is not None
    long_condition2 = df.RMA2 > df.RMA6
    long_condition3 = df.PSARUP is not None
    long_condition4 = df.TSI >= df.TSISignal
    entry1 = long_condition1 & long_condition2 & long_condition3 & long_condition4

    long_condition2 = df.close > df.SMA40
    entry2 = long_condition1 & long_condition2 & long_condition3 & long_condition4
    df['buy'] = (entry1 | entry2).astype(float)
    df['buy_price'] = np.where(df['buy'], df['close'], np.nan)
    df['buy_price'] = df['buy_price'].ffill()   # Forward Fill
    df['sell_price'] = df['open'].shift(-1)
    df.to_csv('data.csv')
    df = pd.read_csv('data.csv')

    # Calculate profit
    df['buy_shifted'] = df['buy'].shift(1)
    open_condition = (df['buy_shifted'] == 0) & (df['buy'] == 1)
    close_condition = (df['buy_shifted'] == 1) & (df['buy'] == 0)
    df['open_trade'] = np.where(open_condition, df['close'], np.nan)
    df['close_trade'] = np.where(close_condition, df['sell_price'], np.nan)

    opened_trades = (df['open_trade'].dropna()).reset_index(drop=True)
    closed_trades = (df['close_trade'].dropna()).reset_index(drop=True)

    profit = ((closed_trades - opened_trades)/opened_trades) * 100
    print(profit)

    # Display Indicators
    fig = plt.figure()

    # Price + EMA + PSAR Plot
    ax1 = fig.add_subplot(311, ylabel='Price')
    ax1.set_facecolor('xkcd:black')
    df.close.plot(ax=ax1, color='green', lw=0.7, legend=True)
    df.SMA40.plot(ax=ax1, color='b', lw=0.7, legend=True)
    df.PSARUP.plot(ax=ax1, color='green', lw=0.7, legend=True)
    df.PSARDOWN.plot(ax=ax1, color='red', lw=0.7, legend=True)

    # TSI Plot
    ax2 = fig.add_subplot(312, ylabel='TSI')
    ax2.set_facecolor('xkcd:black')
    df.TSI.plot(ax=ax2, color='green', lw=0.7, legend=True)
    df.TSISignal.plot(ax=ax2, color='red', lw=0.7, legend=True)

    # Coral Plot
    ax3 = fig.add_subplot(313, ylabel='Coral')
    ax3.set_facecolor('xkcd:black')
    df.CORALUP.plot(ax=ax3, color='green', lw=0.7, legend=True)
    df.CORALDOWN.plot(ax=ax3, color='red', lw=0.7, legend=True)

    plt.show()


main()
