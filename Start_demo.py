# -*- coding: utf-8 -*-

##############################################################################
# Author：QQ173782910  此脚本专供测试使用，测试只跟这一个脚本就好了
##############################################################################

import talib
import logging
from apscheduler.schedulers.background import BlockingScheduler
from RunUse.TradeRun import TradeRun
from config import symbols_conf2

formats = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=formats, filename='gmlog_print.txt')
logger = logging.getLogger('print')
logging.getLogger("apscheduler").setLevel(logging.WARNING)  # 设置apscheduler.


if __name__ == '__main__':  # 25
    RunTrade = TradeRun(symbols_conf2)
    scheduler = BlockingScheduler()  # 定时的任务.
    minute_5 = '0,5,10,15,20,25,30,35,40,45,50,55'
    minute_3 = '0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57'
    minute_15 = '0,15,30,45'
    minute_30 = '0,30'
    hour_2 = '0,2,4,6,8,10,12,14,16,18,20,22'
    hour_4 = '0,4,8,12,16,20'

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5', second='2',
                      args=("C98USDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16', second='2',
                      args=("ALGOUSDT", 19, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25', second='2',
                      args=("XRPUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39', second='2',
                      args=("FLMUSDT", 18, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20', second='2',
                      args=("FTMUSDT", 20, 90.5, 10, 10, '1m',))  # 1min

    ########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_3', minute=minute_3, second='3',
                      args=("C98USDT", 23, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_3', minute=minute_3, second='3',
                      args=("ALGOUSDT", 23, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_3', minute=minute_3, second='3',
                      args=("XRPUSDT", 23, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_3', minute=minute_3, second='3',
                      args=("FLMUSDT", 23, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_3', minute=minute_3, second='3',
                      args=("FTMUSDT", 23, 85.5, 10, 10, '3m',))  # 3min

    ##########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_5', minute=minute_5, second='4',
                      args=("C98USDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_5', minute=minute_5, second='4',
                      args=("ALGOUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_5', minute=minute_5, second='4',
                      args=("XRPUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_5', minute=minute_5, second='4',
                      args=("FLMUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_5', minute=minute_5, second='4',
                      args=("FTMUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min

    ##########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_15', minute=minute_15, second='5',
                      args=("XRPUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_15', minute=minute_15, second='5',
                      args=("FLMUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_15', minute=minute_15, second='5',
                      args=("FTMUSDT", 27, 75.5, 10, 10, '15m',))  # 15min

    ##################################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_30', minute=minute_30, second='5',
                      args=("C98USDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_30', minute=minute_30, second='5',
                      args=("ALGOUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_30', minute=minute_30, second='5',
                      args=("FTMUSDT", 28, 75.5, 10, 10, '30m',))  # 30min

    ############################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_60', minute='0', second='6',
                      args=("C98USDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_60', minute='0', second='6',
                      args=("ALGOUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_60', minute='0', second='6',
                      args=("XRPUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_60', minute='0', second='6',
                      args=("FLMUSDT", 28, 75.5, 10, 10, '1h',))  # 1h

    ########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_61', hour=hour_2, minute='0',
                      second='6', args=("ALGOUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_61', hour=hour_2, minute='0',
                      second='6', args=("XRPUSDT", 28, 75.5, 10, 10, '2h',))  # 2h

    #########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_62', hour=hour_4, minute='0',
                      second='7', args=("ALGOUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_62', hour=hour_4, minute='0',
                      second='7', args=("FTMUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_62', hour=hour_4, minute='0',
                      second='7', args=("XRPUSDT", 28, 75.5, 10, 10, '4h',))  # 4h

    #################################################

    scheduler.add_job(RunTrade.get_position, trigger='cron', id='TradeRunSp', second='*/10')
    scheduler.start()
