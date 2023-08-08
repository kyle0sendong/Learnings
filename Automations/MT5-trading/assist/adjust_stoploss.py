import time
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from ta.trend import psar_up, psar_down, ema_indicator
from ta.volatility import average_true_range

pd.set_option('display.max_rows', None)


# Function to modify an open position
def adjust_stoploss(ticket, symbol, new_stop_loss):
    # Create the request
    request = {
        "action": mt5.TRADE_ACTION_SLTP,
        "symbol": symbol,
        "sl": new_stop_loss,
        "position": ticket
    }

    # Send order to MT5
    result = mt5.order_send(request)
    if result.retcode == 10009:
        print(f'{symbol}\' Stop Loss Adjusted to {new_stop_loss}')


def main():
    # Connect account
    mt5.initialize()
    login = 65813096
    password = 'maskinanO1'
    server = 'XMGlobal-MT5 2'
    mt5.login(login, password, server)

    # Get all orders
    orders = mt5.positions_get()

    while True:

        for order in orders:
            print(f'{order.symbol}')
            current_date = datetime.now()
            one_month_ago = current_date - timedelta(days=30)

            df = pd.DataFrame(mt5.copy_rates_range(order.symbol, mt5.TIMEFRAME_M15, one_month_ago, current_date))
            atr = average_true_range(df['high'], df['low'], df['close'], 50) * 2
            length = len(atr) - 1

            new_sl = 0.0
            order_sl = order.sl
            if order.type == 0:

                sar = psar_up(df['high'], df['low'], df['close'], 0.01, 0.4)

                atr_sl = df['low'].iloc[length] - atr.iloc[length]
                sar_sl = sar.iloc[length]

                print(f'ATR SL: {atr_sl}')
                print(f'SAR SL: {sar_sl}')

                if np.isnan(sar_sl):
                    sar_sl = 0

                if order_sl == 0:  # Initialize order stop loss if it has not been set
                    order_sl = 0

                if atr_sl > sar_sl:
                    if atr_sl > order_sl:
                        new_sl = atr_sl

                elif sar_sl > atr_sl:
                    if sar_sl > order_sl:
                        new_sl = sar_sl

                print(new_sl)

            elif order.type == 1:
                sar = psar_down(df['high'], df['low'], df['close'], 0.01, 0.4)
                atr_sl = atr.iloc[length] + df['high'].iloc[length]
                sar_sl = sar.iloc[length]

                print(f'ATR SL: {atr_sl}')
                print(f'SAR SL: {sar_sl}')

                if np.isnan(sar_sl):
                    sar_sl = atr_sl

                if order_sl == 0:  # Initialize order stop loss if it has not been set
                    order_sl = 99999999

                if atr_sl <= sar_sl:
                    if atr_sl < order_sl:
                        new_sl = atr_sl

                elif sar_sl < atr_sl:
                    if sar_sl < order_sl:
                        new_sl = sar_sl

            if new_sl > 0:
                adjust_stoploss(order.ticket, order.symbol, new_sl)
            else:
                print(f'{order.symbol}\'s Stop Loss has not been changed at {order.sl}')

            print()

        seconds = 900
        print(f'Sleep for {seconds} seconds')
        time.sleep(seconds)
        print('Continue Setting Stop Loss.\n')


main()
