# -*- coding: utf-8 -*-
##############################################################################
# Author：QQ173782910
##############################################################################

import traceback
from utils.brokers import Broker
from getaway.binance_http import BinanceFutureHttp
from getaway.send_msg import bugcode, getToday
from constant.constant import (EVENT_POS, EVENT_KLINE)
from utils.event import EventEngine, Event
from strategies.LineWith import LineWith
from config import key, secret, redisc


class TradeRun:

    def __init__(self, symbols_conf):
        self.min_volume_dict = {}
        self.symbols_list = []
        self.symbols_dict = {}
        self.trading_size_dict = {}
        self.kline_time_dict = {}
        self.redisc = redisc
        self.conf_initialize(symbols_conf)
        self.bugcode = bugcode
        self.getToday = getToday
        self.min_volume = 0.001
        self.key = key
        self.secret = secret
        self.engine = EventEngine()
        self.broker = Broker(self.engine, self.key, secret=self.secret, symbols_list=self.symbols_list)
        self.initialization_data()
        self.broker.add_strategy(LineWith, self.symbols_dict, self.min_volume_dict, self.trading_size_dict)

    def conf_initialize(self, symbolsconf):
        # 初始化dict
        # [symbol, trading_size, win_arg, add_arg]
        for i in symbolsconf:
            symbol, trading_size, win_arg, add_arg = i
            self.symbols_list.append(symbol)
            self.symbols_dict[symbol] = [win_arg, add_arg]
            self.trading_size_dict[symbol] = trading_size

    def initialization_data(self):
        try:
            binance_http = BinanceFutureHttp(key=self.key, secret=self.secret)
            einfo = binance_http.exchangeInfo()
            if isinstance(einfo, dict):
                esymbols = einfo['symbols']
                for i in esymbols:
                    _symbol = i['symbol']
                    if _symbol in self.trading_size_dict:
                        for j in i['filters']:
                            if j['filterType'] == 'LOT_SIZE':
                                minQty = float(j['minQty'])
                                trading_size = self.trading_size_dict[_symbol]
                                if minQty > trading_size:
                                    self.trading_size_dict[_symbol] = minQty
                                    msg = f"config里的symbol:{_symbol},trading_size:{trading_size},太小,minQty{minQty}"
                                    self.bugcode(msg)
                                self.min_volume_dict[_symbol] = minQty
        except:
            self.bugcode(traceback, "TradeRun_initialization_data")

    def get_kline_data(self, symbol, sold, bought, sold_bar, bought_bar, interval):
        try:

            if symbol in self.symbols_dict:
                try:
                    data = self.broker.binance_http.get_kline_interval(symbol=symbol, interval=interval, limit=100)
                except Exception as e:
                    self.bugcode(f"{e}")
                    data = self.broker.binance_http.get_kline_interval(symbol=symbol, interval=interval, limit=100)
                if isinstance(data, list):
                    if len(data):
                        kline_time = data[-1][0]
                        if kline_time != self.kline_time_dict.get(symbol, 0):
                            edata = {'symbol': symbol, "data": data, "sold": sold, "bought": bought,
                                     "sold_bar": sold_bar, "bought_bar": bought_bar, 'interval': interval}
                            event = Event(EVENT_KLINE, edata)
                            self.broker.event_engine.put(event)
                            self.kline_time_dict[symbol] = kline_time
                else:
                    self.bugcode(f"{data}")
        except:
            self.bugcode(traceback, "TradeRun_get_kline_data")

    def get_position(self):
        try:
            info = self.broker.binance_http.get_position_info()
            if isinstance(info, list):
                for item in info:
                    symbolm = item["symbol"]
                    positionSide = item["positionSide"]
                    # 当持仓为多空双向，策略仅为多方向，只处理多方向的仓位
                    # if item['positionSide'] != 'LONG':
                    #     return
                    if symbolm in self.symbols_dict and positionSide == 'BOTH':
                        event = Event(EVENT_POS, {"symbol": symbolm, "pos": item})
                        self.broker.event_engine.put(event)
            else:
                self.bugcode(f"{info}")
        except:
            self.bugcode(traceback, "TradeRun_get_position")
