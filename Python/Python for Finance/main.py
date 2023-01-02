""" Main """

from test.mt5.connect import *
from test.indicators.ta import *
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

    open_price = df['open']
    high_price = df['high']
    low_price = df['low']
    close_price = df['close']
    hl2_price = hl2(df)

    df.rename(columns={'time': 'timestamp', 'tick_volume': 'volume'}, inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # Smoothed Moving Average (SMA)
    sma40 = sma(close_price, 40)
    df = df.assign(SMA40=sma40)

    #Relative Moving Average
    rma2 = rma(close_price, 2)
    rma6 = rma(close_price, 6)
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
    sar_up, sar_down = psar(high_price, low_price, close_price, psar_increment, psar_maximum)
    df = df.assign(PSARUP=sar_up)
    df = df.assign(PSARDOWN=sar_down)

    # Coral
    coral_length = 20
    coral_multiplier = 0.7
    coral_up, coral_down = coral(close_price, coral_length, coral_multiplier)
    df = df.assign(CORALUP=coral_up)
    df = df.assign(CORALDOWN=coral_down)

    long_condition1 = df['CORALUP'] is not None
    long_condition2 = df['RMA2'] > df['RMA6']
    long_condition3 = df['PSARUP'] is not None
    long_condition4 = df['TSI'] > df['TSISignal']
    entry1 = long_condition1 & long_condition2 & long_condition3 & long_condition4

    long_condition2 = df['close'] > df['SMA40']
    entry2 = long_condition1 & long_condition2 & long_condition3 & long_condition4
    df['Buy'] = entry1 | entry2
    df['BuyPrice'] = np.where(df.Buy, df.close * 0.99, np.nan)
    df.BuyPrice = df.BuyPrice.ffill()   # Forward Fill
    df['SellPrice'] = df['open'].shift(-1)
    print(df)
    # Display Indicators
    fig = plt.figure()

    # Price + EMA + PSAR Plot
    ax1 = fig.add_subplot(311, ylabel='Price')
    ax1.set_facecolor('xkcd:black')
    close_price.plot(ax=ax1, color='green', lw=0.7, legend=True)
    sma40.plot(ax=ax1, color='b', lw=0.7, legend=True)
    sar_up.plot(ax=ax1, color='green', lw=0.7, legend=True)
    sar_down.plot(ax=ax1, color='red', lw=0.7, legend=True)

    # TSI Plot
    ax2 = fig.add_subplot(312, ylabel='TSI')
    ax2.set_facecolor('xkcd:black')
    tsi_values.plot(ax=ax2, color='green', lw=0.7, legend=True)
    tsi_signal.plot(ax=ax2, color='red', lw=0.7, legend=True)

    # Coral Plot
    ax3 = fig.add_subplot(313, ylabel='Coral')
    ax3.set_facecolor('xkcd:black')
    coral_up.plot(ax=ax3, color='green', lw=0.7, legend=True)
    coral_down.plot(ax=ax3, color='red', lw=0.7, legend=True)



    plt.show()


main()
