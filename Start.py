# -*- coding: utf-8 -*-

##############################################################################
# Author：QQ173782910
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

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1', second='2',
                      args=("ARUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2', second='2',
                      args=("CELOUSDT", 21, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3', second='2',
                      args=("RLCUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4', second='2',
                      args=("LITUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5', second='2',
                      args=("C98USDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6', second='2',
                      args=("MTLUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7', second='2',
                      args=("1INCHUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8', second='3',
                      args=("CRVUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9', second='3',
                      args=("SXPUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10', second='3',
                      args=("AUDIOUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11', second='3',
                      args=("TOMOUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12', second='3',
                      args=("ADAUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13', second='3',
                      args=("ICXUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14', second='3',
                      args=("BAKEUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15', second='4',
                      args=("BELUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16', second='4',
                      args=("ALGOUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17', second='4',
                      args=("CTKUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18', second='4',
                      args=("KNCUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19', second='4',
                      args=("ENJUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20', second='4',
                      args=("FTMUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21', second='4',
                      args=("DODOUSDT", 24, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22', second='5',
                      args=("MATICUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23', second='5',
                      args=("IOTAUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24', second='5',
                      args=("STORJUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25', second='5',
                      args=("XRPUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26', second='5',
                      args=("RENUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27', second='5',
                      args=("SFPUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28', second='5',
                      args=("ZRXUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29', second='6',
                      args=("ALPHAUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30', second='6',
                      args=("ATAUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31', second='6',
                      args=("ONTUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_32', second='6',
                      args=("OGNUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33', second='6',
                      args=("SANDUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34', second='6',
                      args=("MANAUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_35', second='6',
                      args=("GRTUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_36', second='7',
                      args=("OCEANUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37', second='7',
                      args=("BATUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_38', second='7',
                      args=("CVCUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39', second='7',
                      args=("FLMUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40', second='7',
                      args=("KEEPUSDT", 26, 75.5, 10, 10, '1m',))  # 1min

    ########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_3', minute=minute_3, second='8',
                      args=("ARUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_3', minute=minute_3, second='8',
                      args=("LITUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_3', minute=minute_3, second='8',
                      args=("C98USDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_3', minute=minute_3, second='8',
                      args=("MTLUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_3', minute=minute_3, second='8',
                      args=("1INCHUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_3', minute=minute_3, second='8',
                      args=("CRVUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_3', minute=minute_3, second='8',
                      args=("SXPUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_3', minute=minute_3, second='9',
                      args=("AUDIOUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_3', minute=minute_3, second='9',
                      args=("TOMOUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_3', minute=minute_3, second='9',
                      args=("ADAUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_3', minute=minute_3, second='9',
                      args=("ICXUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_3', minute=minute_3, second='9',
                      args=("BAKEUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_3', minute=minute_3, second='9',
                      args=("BELUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_3', minute=minute_3, second='9',
                      args=("ALGOUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_3', minute=minute_3, second='10',
                      args=("CTKUSDT", 22, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_3', minute=minute_3, second='10',
                      args=("KNCUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_3', minute=minute_3, second='10',
                      args=("ENJUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_3', minute=minute_3, second='10',
                      args=("FTMUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_3', minute=minute_3, second='10',
                      args=("DODOUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_3', minute=minute_3, second='10',
                      args=("MATICUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_3', minute=minute_3, second='10',
                      args=("IOTAUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_3', minute=minute_3, second='11',
                      args=("STORJUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_3', minute=minute_3, second='11',
                      args=("XRPUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_3', minute=minute_3, second='11',
                      args=("SFPUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_3', minute=minute_3, second='11',
                      args=("ZRXUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_3', minute=minute_3, second='11',
                      args=("ALPHAUSDT", 24, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_3', minute=minute_3, second='11',
                      args=("ATAUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_3', minute=minute_3, second='11',
                      args=("ONTUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_32_3', minute=minute_3, second='12',
                      args=("OGNUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_3', minute=minute_3, second='12',
                      args=("SANDUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34_3', minute=minute_3, second='12',
                      args=("MANAUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_35_3', minute=minute_3, second='12',
                      args=("GRTUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_36_3', minute=minute_3, second='12',
                      args=("OCEANUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37_3', minute=minute_3, second='12',
                      args=("BATUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_38_3', minute=minute_3, second='12',
                      args=("CVCUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_3', minute=minute_3, second='13',
                      args=("FLMUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40_3', minute=minute_3, second='13',
                      args=("KEEPUSDT", 28, 75.5, 10, 10, '3m',))  # 3min

    ##########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_5', minute=minute_5, second='13',
                      args=("ARUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_5', minute=minute_5, second='13',
                      args=("CELOUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_5', minute=minute_5, second='13',
                      args=("RLCUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_5', minute=minute_5, second='13',
                      args=("LITUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_5', minute=minute_5, second='13',
                      args=("C98USDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_5', minute=minute_5, second='14',
                      args=("MTLUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_5', minute=minute_5, second='14',
                      args=("1INCHUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_5', minute=minute_5, second='14',
                      args=("CRVUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_5', minute=minute_5, second='14',
                      args=("SXPUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_5', minute=minute_5, second='14',
                      args=("TOMOUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_5', minute=minute_5, second='14',
                      args=("ADAUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_5', minute=minute_5, second='14',
                      args=("ICXUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_5', minute=minute_5, second='15',
                      args=("BAKEUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_5', minute=minute_5, second='15',
                      args=("BELUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_5', minute=minute_5, second='15',
                      args=("ALGOUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_5', minute=minute_5, second='15',
                      args=("CTKUSDT", 22, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_5', minute=minute_5, second='15',
                      args=("KNCUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_5', minute=minute_5, second='15',
                      args=("ENJUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_5', minute=minute_5, second='15',
                      args=("FTMUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_5', minute=minute_5, second='16',
                      args=("DODOUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_5', minute=minute_5, second='16',
                      args=("MATICUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_5', minute=minute_5, second='16',
                      args=("STORJUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_5', minute=minute_5, second='16',
                      args=("XRPUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_5', minute=minute_5, second='16',
                      args=("RENUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_5', minute=minute_5, second='16',
                      args=("SFPUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_5', minute=minute_5, second='16',
                      args=("ALPHAUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_5', minute=minute_5, second='17',
                      args=("ATAUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_5', minute=minute_5, second='17',
                      args=("ONTUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_32_5', minute=minute_5, second='17',
                      args=("OGNUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_5', minute=minute_5, second='17',
                      args=("SANDUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34_5', minute=minute_5, second='17',
                      args=("MANAUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_35_5', minute=minute_5, second='17',
                      args=("GRTUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_36_5', minute=minute_5, second='17',
                      args=("OCEANUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37_5', minute=minute_5, second='18',
                      args=("BATUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_5', minute=minute_5, second='18',
                      args=("FLMUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40_5', minute=minute_5, second='18',
                      args=("KEEPUSDT", 28, 75.5, 10, 10, '5m',))  # 5min

    ##########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_15', minute=minute_15, second='18',
                      args=("ARUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_15', minute=minute_15, second='18',
                      args=("1INCHUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_15', minute=minute_15, second='18',
                      args=("CRVUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_15', minute=minute_15, second='18',
                      args=("TOMOUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_15', minute=minute_15, second='19',
                      args=("ICXUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_15', minute=minute_15, second='19',
                      args=("BAKEUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_15', minute=minute_15, second='19',
                      args=("BELUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_15', minute=minute_15, second='19',
                      args=("CTKUSDT", 22, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_15', minute=minute_15, second='19',
                      args=("KNCUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_15', minute=minute_15, second='19',
                      args=("FTMUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_15', minute=minute_15, second='19',
                      args=("DODOUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_15', minute=minute_15, second='20',
                      args=("MATICUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_15', minute=minute_15, second='20',
                      args=("XRPUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_15', minute=minute_15, second='20',
                      args=("RENUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_15', minute=minute_15, second='20',
                      args=("SFPUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_15', minute=minute_15, second='20',
                      args=("ZRXUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_15', minute=minute_15, second='20',
                      args=("ONTUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_15', minute=minute_15, second='20',
                      args=("SANDUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_35_15', minute=minute_15, second='21',
                      args=("GRTUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_36_15', minute=minute_15, second='21',
                      args=("OCEANUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_15', minute=minute_15, second='21',
                      args=("FLMUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40_15', minute=minute_15, second='21',
                      args=("KEEPUSDT", 28, 75.5, 10, 10, '15m',))  # 15min

    ##################################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_30', minute=minute_30, second='21',
                      args=("LITUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_30', minute=minute_30, second='21',
                      args=("C98USDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_30', minute=minute_30, second='21',
                      args=("1INCHUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_30', minute=minute_30, second='22',
                      args=("CRVUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_30', minute=minute_30, second='22',
                      args=("AUDIOUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_30', minute=minute_30, second='22',
                      args=("TOMOUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_30', minute=minute_30, second='22',
                      args=("ICXUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_30', minute=minute_30, second='22',
                      args=("BAKEUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_30', minute=minute_30, second='22',
                      args=("ALGOUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_30', minute=minute_30, second='23',
                      args=("ENJUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_30', minute=minute_30, second='23',
                      args=("FTMUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_30', minute=minute_30, second='23',
                      args=("MATICUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_30', minute=minute_30, second='23',
                      args=("IOTAUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_30', minute=minute_30, second='23',
                      args=("ALPHAUSDT", 24, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_30', minute=minute_30, second='23',
                      args=("SANDUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34_30', minute=minute_30, second='23',
                      args=("MANAUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_35_30', minute=minute_30, second='24',
                      args=("GRTUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_38_30', minute=minute_30, second='24',
                      args=("CVCUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40_30', minute=minute_30, second='24',
                      args=("KEEPUSDT", 28, 75.5, 10, 10, '30m',))  # 30min

    ############################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_60', minute='0', second='24',
                      args=("RLCUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_60', minute='0', second='24',
                      args=("C98USDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_60', minute='0', second='24',
                      args=("MTLUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_60', minute='0', second='24',
                      args=("1INCHUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_60', minute='0', second='25',
                      args=("CRVUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_60', minute='0', second='25',
                      args=("AUDIOUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_60', minute='0', second='25',
                      args=("TOMOUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_60', minute='0', second='25',
                      args=("ADAUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_60', minute='0', second='25',
                      args=("ICXUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_60', minute='0', second='25',
                      args=("ALGOUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_60', minute='0', second='25',
                      args=("KNCUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_60', minute='0', second='26',
                      args=("DODOUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_60', minute='0', second='26',
                      args=("STORJUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_60', minute='0', second='26',
                      args=("XRPUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_60', minute='0', second='26',
                      args=("RENUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_60', minute='0', second='26',
                      args=("ZRXUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_60', minute='0', second='26',
                      args=("ALPHAUSDT", 24, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_60', minute='0', second='26',
                      args=("ATAUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_60', minute='0', second='27',
                      args=("ONTUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_32_60', minute='0', second='27',
                      args=("OGNUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_60', minute='0', second='27',
                      args=("SANDUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34_60', minute='0', second='27',
                      args=("MANAUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37_60', minute='0', second='27',
                      args=("BATUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_60', minute='0', second='27',
                      args=("FLMUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40_60', minute='0', second='27',
                      args=("KEEPUSDT", 28, 75.5, 10, 10, '1h',))  # 1H

    ########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_61', hour=hour_2, minute='0',
                      second='28', args=("RLCUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_61', hour=hour_2, minute='0',
                      second='28', args=("SXPUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_61', hour=hour_2, minute='0',
                      second='28', args=("TOMOUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_61', hour=hour_2, minute='0',
                      second='28', args=("ADAUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_61', hour=hour_2, minute='0',
                      second='28', args=("ICXUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_61', hour=hour_2, minute='0',
                      second='28', args=("BELUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_61', hour=hour_2, minute='0',
                      second='28', args=("ALGOUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_61', hour=hour_2,  minute='0',
                      second='29', args=("CTKUSDT", 22, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_61', hour=hour_2, minute='0',
                      second='29', args=("KNCUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_61', hour=hour_2, minute='0',
                      second='29', args=("MATICUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_61', hour=hour_2, minute='0',
                      second='29', args=("STORJUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_61', hour=hour_2, minute='0',
                      second='29', args=("XRPUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_61', hour=hour_2, minute='0',
                      second='29', args=("RENUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_61', hour=hour_2, minute='0',
                      second='29', args=("SFPUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_61', hour=hour_2, minute='0',
                      second='30', args=("ZRXUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_61', hour=hour_2, minute='0',
                      second='30', args=("ATAUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_61', hour=hour_2, minute='0',
                      second='30', args=("ONTUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_61', hour=hour_2, minute='0',
                      second='30', args=("SANDUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34_61', hour=hour_2, minute='0',
                      second='30', args=("MANAUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37_61', hour=hour_2, minute='0',
                      second='30', args=("BATUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_38_61', hour=hour_2, minute='0',
                      second='30', args=("CVCUSDT", 28, 75.5, 10, 10, '2h',))  # 2h

    #########################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_62', hour=hour_4, minute='0',
                      second='31', args=("1INCHUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_62', hour=hour_4, minute='0',
                      second='31', args=("CRVUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_62', hour=hour_4, minute='0',
                      second='31', args=("TOMOUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_62', hour=hour_4, minute='0',
                      second='31', args=("ADAUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_62', hour=hour_4, minute='0',
                      second='31', args=("ICXUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_62', hour=hour_4, minute='0',
                      second='31', args=("BELUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_62', hour=hour_4, minute='0',
                      second='31', args=("ALGOUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_62', hour=hour_4, minute='0',
                      second='32', args=("CTKUSDT", 22, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_62', hour=hour_4, minute='0',
                      second='32', args=("ENJUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_62', hour=hour_4, minute='0',
                      second='32', args=("FTMUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_62', hour=hour_4, minute='0',
                      second='32', args=("MATICUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_62', hour=hour_4, minute='0',
                      second='32', args=("IOTAUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_62', hour=hour_4, minute='0',
                      second='32', args=("STORJUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_62', hour=hour_4, minute='0',
                      second='32', args=("XRPUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_62', hour=hour_4, minute='0',
                      second='33', args=("RENUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37_62', hour=hour_4, minute='0',
                      second='33', args=("BATUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_38_62', hour=hour_4, minute='0',
                      second='33', args=("CVCUSDT", 28, 75.5, 10, 10, '4h',))  # 4h

    #################################################

    scheduler.add_job(RunTrade.get_position, trigger='cron', id='TradeRunSp', second='*/10')
    scheduler.start()
