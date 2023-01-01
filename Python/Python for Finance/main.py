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

    ohlc_data = pd.DataFrame(mt5.copy_rates_range('EURUSD#',
                                                  mt5.TIMEFRAME_D1,
                                                  datetime(2012, 1, 1),
                                                  datetime(2022, 12, 27)))

    ohlc_data = ohlc_data.assign(OpenPrice=pd.Series(ohlc_data['open'], index=ohlc_data.index))
    ohlc_data = ohlc_data.assign(HighPrice=pd.Series(ohlc_data['high'], index=ohlc_data.index))
    ohlc_data = ohlc_data.assign(LowPrice=pd.Series(ohlc_data['low'], index=ohlc_data.index))
    ohlc_data = ohlc_data.assign(ClosePrice=pd.Series(ohlc_data['close'], index=ohlc_data.index))
    open_price = ohlc_data['OpenPrice']
    high_price = ohlc_data['HighPrice']
    low_price = ohlc_data['LowPrice']
    close_price = ohlc_data['ClosePrice']
    hl2_price = hl2(ohlc_data)

    # Exponential Moving Average (EMA)
    ema_length = 100
    ema_values = ema(close_price, ema_length)
    ohlc_data = ohlc_data.assign(EMA=ema_values)

    # True Strength Index (TSI)
    tsi_slow = 12
    tsi_fast = 26
    tsi_smooth = 19
    tsi_values, tsi_signal = tsi_mod(hl2_price, tsi_slow, tsi_fast, tsi_smooth)
    ohlc_data = ohlc_data.assign(TSI=tsi_values)
    ohlc_data = ohlc_data.assign(TSISignal=tsi_signal)

    # Parabolic SAR
    psar_increment = 0.06
    psar_maximum = 0.035
    sar_up, sar_down = psar(high_price, low_price, close_price, psar_increment, psar_maximum)
    ohlc_data = ohlc_data.assign(PSARUP=sar_up)
    ohlc_data = ohlc_data.assign(PSARDOWN=sar_down)

    # Coral
    coral_length = 20
    coral_multiplier = 0.7
    coral_up, coral_down = coral(close_price, coral_length, coral_multiplier)
    ohlc_data = ohlc_data.assign(CORALUP=coral_up)
    ohlc_data = ohlc_data.assign(CORALDOWN=coral_down)

    # Display Indicators
    fig = plt.figure()

    # Price + EMA + PSAR Plot
    ax1 = fig.add_subplot(311, ylabel='Price')
    ax1.set_facecolor('xkcd:black')
    close_price.plot(ax=ax1, color='green', lw=0.7, legend=True)
    ema_values.plot(ax=ax1, color='b', lw=0.7, legend=True)
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
