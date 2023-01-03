"""Connecting to MetaTrade5 test"""

import MetaTrader5 as mt5


def connect_to_mt(login, password, server):

    mt5.initialize()
    mt5.login(login, password, server)
    account_info = mt5.account_info()
    print(account_info)
