from indicators.modified_ta import *
from pathlib import Path


def display_trading_results(year=0, month=0, day=0, account_size=1000, trades=0, wins=0):
    print(f'\n\n{str(year)}-{str(month)}-{str(day)} Total Money: {account_size}')
    print(f'Trades: {trades}')
    print(f'Wins: {wins}')
    if trades > 0:
        print(f'Losses: {trades - wins} ')
        print(f'Win Rate: {(wins / trades) * 100}%\n')


def backtest_monthly(start_year, end_year, ticker_name, timeframe):
    timeframe_string = get_timeframe_string(timeframe)

    for year in range(start_year, end_year + 1):

        for month in range(1, 12 + 1):
            path = './data/' + ticker_name + '/' + timeframe_string + '/monthly/' + str(year) + '/' + str(month) + '.csv'

            if Path(path).exists():
                df = pd.read_csv(path)

                _close = df['close']
                _low = df['low']
                _open = df['open']  # For entry price, shift
                _high = df['high']
                _hl2 = hl2(df)
                _sar_up, _sar_down = psar(_high, _low, _close, 0.02, 0.2)

                rma50 = rma(_hl2, 200)
                tsi_values1, tsi_signal1 = tsi_mod(_close, 12, 26, 19)
                tsi_values2, tsi_signal2 = tsi_mod(_close, 26, 52, 38)
                _atr_stoploss = atr(_high, _low, _close, 5)

                # Account Info
                account_size = 1000
                trades = 0
                wins = 0

                # Entry & Exit prices
                stoploss = 0
                entry_price = 0
                in_trade = False

                i = 1
                while i < (len(_open) - 1):

                    # Entry conditions
                    condition1 = tsi_values1.iloc[i - 1] <= tsi_signal1.iloc[i - 1]
                    condition2 = tsi_values1.iloc[i] > tsi_signal1.iloc[i]
                    condition3 = tsi_signal2.iloc[i] > -5
                    condition4 = _close.iloc[i] > rma50.iloc[i]
                    entry = condition1 & condition2 & condition3 & condition4

                    leverage = 400
                    risk = (account_size * 0.05)
                    position_size = round((risk * leverage) / 100) * 100
                    risk = position_size / leverage

                    # Fresh Entry
                    if entry & (not in_trade):
                        trades += 1
                        in_trade = True
                        entry_price = _open.iloc[i + 1]

                        if _sar_up.iloc[i] > 0:
                            stoploss = _sar_up.iloc[i]
                        else:
                            stoploss = entry_price - (_atr_stoploss.iloc[i]*2)

                    # Opened trade
                    if in_trade:

                        # If exit trade after stoploss has been hit
                        if _low.iloc[i] <= stoploss:
                            in_trade = False  # no more trade open
                            exit_price = stoploss
                            stoploss = 0

                            # Calculate profits
                            profit = (((exit_price - entry_price) / entry_price) * position_size)

                            # Add wins
                            if profit > 0:
                                wins += 1
                                account_size += profit

                            if profit < 0:
                                account_size -= abs(profit)

                        else:

                            # Adjust stop loss
                            temp_stoploss1 = _close.iloc[i - 1] - _atr_stoploss.iloc[i - 1]
                            temp_stoploss2 = _close.iloc[i] - _atr_stoploss.iloc[i]

                            if temp_stoploss2 > temp_stoploss1:
                                stoploss = temp_stoploss2

                    i += 1

                display_trading_results(year, month, 0, account_size, trades, wins)

            else:
                continue


backtest_monthly(2012, 2023, 'EURUSD#', mt5.TIMEFRAME_H2)