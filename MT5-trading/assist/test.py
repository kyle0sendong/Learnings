from datetime import datetime, timedelta
import MetaTrader5 as mt5
import pandas as pd

mt5.initialize()
login = 65813096
password = 'maskinanO1'
server = 'XMGlobal-MT5 2'
mt5.login(login, password, server)


current_date = datetime.now()

one_month_ago = current_date - timedelta(days=30)  # Assuming 30 days per month

df = pd.DataFrame(mt5.copy_rates_range('SILVER#', mt5.TIMEFRAME_H2, one_month_ago, current_date))
print(df['close'])
