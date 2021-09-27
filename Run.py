# -*- coding: utf-8 -*-

##############################################################################
# Author：QQ173782910
##############################################################################

import talib
import logging
from apscheduler.schedulers.background import BlockingScheduler
from RunUse.TradeRun import TradeRun
from config import symbols_conf

formats = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=formats, filename='gmlog_print.txt')
logger = logging.getLogger('print')
logging.getLogger("apscheduler").setLevel(logging.WARNING)  # 设置apscheduler.


if __name__ == '__main__':  # 25
    RunTrade = TradeRun(symbols_conf)
    scheduler = BlockingScheduler()  # 定时的任务.
    minute_5 = '0,5,10,15,20,25,30,35,40,45,50,55'
    minute_3 = '0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57'

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM1', second='2',
                      args=("AAVEUSDT", 24, 72.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2', second='2',
                      args=("KSMUSDT", 24, 71.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3', second='2',
                      args=("UNIUSDT", 24, 71.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4', second='2',
                      args=("EGLDUSDT", 28, 71.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7', second='2',
                      args=("DOTUSDT", 26, 71.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12', second='3',
                      args=("BCHUSDT", 24, 71.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM19',  second='3',
                      args=("LUNAUSDT", 24, 71.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23', second='3',
                      args=("TRBUSDT", 27, 71.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24', second='3',
                      args=("NEOUSDT", 26, 71.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21', second='3',
                      args=("COMPUSDT", 26, 71.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM26', second='4',
                      args=("ATOMUSDT", 28, 71.5, 5, 10, '1m',))  # 1min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5', second='4',
                      args=("BNBUSDT", 28, 71.5, 10, 10, '1m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM6', second='4',
                      args=("SOLUSDT", 26, 71.5, 10, 10, '1m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13', second='4',
                      args=("MKRUSDT", 24, 71.5, 10, 10, '1m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20', second='4',
                      args=("YFIIUSDT", 25, 71.5, 10, 10, '1m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM22', second='5',
                      args=("XMRUSDT", 25, 71.5, 5, 10, '1m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM18', second='5',
                      args=("AVAXUSDT", 27.5, 71.5, 10, 10, '1m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM25', second='5',
                      args=("NEARUSDT", 28.5, 71.5, 10, 10, '1m',))  # 3min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8', second='5',
                      args=("BTCUSDT", 23, 71.5, 10, 10, '1m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9', second='5',
                      args=("YFIUSDT", 24, 71.5, 10, 10, '1m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM10', second='5',
                      args=("ETHUSDT", 28, 71.5, 5, 10, '1m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11', second='6',
                      args=("LTCUSDT", 23, 71.5, 5, 10, '1m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14', second='6',
                      args=("DASHUSDT", 24, 71.5, 5, 10, '1m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM15', second='6',
                      args=("ZECUSDT", 26, 71.5, 10, 10, '1m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16', second='6',
                      args=("ZENUSDT", 24, 71.5, 5, 10, '1m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM17', second='6',
                      args=("FILUSDT", 28.5, 71.5, 5, 10, '1m',))  # 5min

    scheduler.add_job(RunTrade.get_position, trigger='cron', id='TradeRunGMRMp', second='*/10')
    scheduler.start()
