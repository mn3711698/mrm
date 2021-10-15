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
                      args=("ARUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2', second='2',
                      args=("CELOUSDT", 19, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3', second='2',
                      args=("RLCUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4', second='2',
                      args=("LITUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5', second='2',
                      args=("C98USDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6', second='2',
                      args=("MTLUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7', second='3',
                      args=("1INCHUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8', second='3',
                      args=("CRVUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9', second='3',
                      args=("SXPUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10', second='3',
                      args=("AUDIOUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11', second='3',
                      args=("TOMOUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12', second='3',
                      args=("ADAUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13', second='4',
                      args=("ICXUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14', second='4',
                      args=("BAKEUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15', second='4',
                      args=("BELUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16', second='4',
                      args=("ALGOUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17', second='4',
                      args=("CTKUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18', second='4',
                      args=("KNCUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19', second='5',
                      args=("ENJUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20', second='5',
                      args=("FTMUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21', second='5',
                      args=("DODOUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22', second='5',
                      args=("MATICUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23', second='5',
                      args=("IOTAUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24', second='5',
                      args=("STORJUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25', second='7',
                      args=("XRPUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26', second='7',
                      args=("RENUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27', second='7',
                      args=("SFPUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28', second='7',
                      args=("ZRXUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29', second='7',
                      args=("ALPHAUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30', second='7',
                      args=("ATAUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31', second='8',
                      args=("ONTUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_32', second='8',
                      args=("OGNUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33', second='8',
                      args=("SANDUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34', second='8',
                      args=("MANAUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_35', second='8',
                      args=("GRTUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_36', second='8',
                      args=("OCEANUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37', second='9',
                      args=("BATUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_38', second='9',
                      args=("CVCUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39', second='9',
                      args=("FLMUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40', second='9',
                      args=("KEEPUSDT", 20, 90.5, 10, 10, '1m',))  # 1min

    ########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_3', minute=minute_3, second='9',
                      args=("ARUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_3', minute=minute_3, second='9',
                      args=("LITUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_3', minute=minute_3, second='10',
                      args=("C98USDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_3', minute=minute_3, second='10',
                      args=("MTLUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_3', minute=minute_3, second='10',
                      args=("1INCHUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_3', minute=minute_3, second='10',
                      args=("CRVUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_3', minute=minute_3, second='10',
                      args=("SXPUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_3', minute=minute_3, second='10',
                      args=("AUDIOUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_3', minute=minute_3, second='11',
                      args=("TOMOUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_3', minute=minute_3, second='11',
                      args=("ADAUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_3', minute=minute_3, second='11',
                      args=("ICXUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_3', minute=minute_3, second='11',
                      args=("BAKEUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_3', minute=minute_3, second='11',
                      args=("BELUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_3', minute=minute_3, second='11',
                      args=("ALGOUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_3', minute=minute_3, second='12',
                      args=("CTKUSDT", 22.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_3', minute=minute_3, second='12',
                      args=("KNCUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_3', minute=minute_3, second='12',
                      args=("ENJUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_3', minute=minute_3, second='12',
                      args=("FTMUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_3', minute=minute_3, second='12',
                      args=("DODOUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_3', minute=minute_3, second='12',
                      args=("MATICUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_3', minute=minute_3, second='13',
                      args=("IOTAUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_3', minute=minute_3, second='13',
                      args=("STORJUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_3', minute=minute_3, second='13',
                      args=("XRPUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_3', minute=minute_3, second='13',
                      args=("SFPUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_3', minute=minute_3, second='13',
                      args=("ZRXUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_3', minute=minute_3, second='13',
                      args=("ALPHAUSDT", 23.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_3', minute=minute_3, second='14',
                      args=("ATAUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_3', minute=minute_3, second='14',
                      args=("ONTUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_32_3', minute=minute_3, second='14',
                      args=("OGNUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_3', minute=minute_3, second='14',
                      args=("SANDUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34_3', minute=minute_3, second='14',
                      args=("MANAUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_35_3', minute=minute_3, second='14',
                      args=("GRTUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_36_3', minute=minute_3, second='15',
                      args=("OCEANUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37_3', minute=minute_3, second='15',
                      args=("BATUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_38_3', minute=minute_3, second='15',
                      args=("CVCUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_3', minute=minute_3, second='15',
                      args=("FLMUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40_3', minute=minute_3, second='15',
                      args=("KEEPUSDT", 24.5, 85.5, 10, 10, '3m',))  # 3min

    ##########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_5', minute=minute_5, second='15',
                      args=("ARUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_5', minute=minute_5, second='16',
                      args=("CELOUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_5', minute=minute_5, second='16',
                      args=("RLCUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_5', minute=minute_5, second='16',
                      args=("LITUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_5', minute=minute_5, second='16',
                      args=("C98USDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_5', minute=minute_5, second='16',
                      args=("MTLUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_5', minute=minute_5, second='16',
                      args=("1INCHUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_5', minute=minute_5, second='17',
                      args=("CRVUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_5', minute=minute_5, second='17',
                      args=("SXPUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_5', minute=minute_5, second='17',
                      args=("TOMOUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_5', minute=minute_5, second='17',
                      args=("ADAUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_5', minute=minute_5, second='17',
                      args=("ICXUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_5', minute=minute_5, second='17',
                      args=("BAKEUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_5', minute=minute_5, second='18',
                      args=("BELUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_5', minute=minute_5, second='18',
                      args=("ALGOUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_5', minute=minute_5, second='18',
                      args=("CTKUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_5', minute=minute_5, second='18',
                      args=("KNCUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_5', minute=minute_5, second='18',
                      args=("ENJUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_5', minute=minute_5, second='18',
                      args=("FTMUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_5', minute=minute_5, second='19',
                      args=("DODOUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_5', minute=minute_5, second='19',
                      args=("MATICUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_5', minute=minute_5, second='19',
                      args=("STORJUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_5', minute=minute_5, second='19',
                      args=("XRPUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_5', minute=minute_5, second='19',
                      args=("RENUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_5', minute=minute_5, second='19',
                      args=("SFPUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_5', minute=minute_5, second='20',
                      args=("ALPHAUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_5', minute=minute_5, second='20',
                      args=("ATAUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_5', minute=minute_5, second='20',
                      args=("ONTUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_32_5', minute=minute_5, second='20',
                      args=("OGNUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_5', minute=minute_5, second='20',
                      args=("SANDUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34_5', minute=minute_5, second='20',
                      args=("MANAUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_35_5', minute=minute_5, second='21',
                      args=("GRTUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_36_5', minute=minute_5, second='21',
                      args=("OCEANUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37_5', minute=minute_5, second='21',
                      args=("BATUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_5', minute=minute_5, second='21',
                      args=("FLMUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40_5', minute=minute_5, second='21',
                      args=("KEEPUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min

    ##########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_15', minute=minute_15, second='21',
                      args=("ARUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_15', minute=minute_15, second='22',
                      args=("1INCHUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_15', minute=minute_15, second='22',
                      args=("CRVUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_15', minute=minute_15, second='22',
                      args=("TOMOUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_15', minute=minute_15, second='22',
                      args=("ICXUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_15', minute=minute_15, second='22',
                      args=("BAKEUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_15', minute=minute_15, second='22',
                      args=("BELUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_15', minute=minute_15, second='23',
                      args=("CTKUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_15', minute=minute_15, second='23',
                      args=("KNCUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_15', minute=minute_15, second='23',
                      args=("FTMUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_15', minute=minute_15, second='23',
                      args=("DODOUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_15', minute=minute_15, second='23',
                      args=("MATICUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_15', minute=minute_15, second='23',
                      args=("XRPUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_15', minute=minute_15, second='24',
                      args=("RENUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_15', minute=minute_15, second='24',
                      args=("SFPUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_15', minute=minute_15, second='24',
                      args=("ZRXUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_15', minute=minute_15, second='24',
                      args=("ONTUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_15', minute=minute_15, second='24',
                      args=("SANDUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_35_15', minute=minute_15, second='24',
                      args=("GRTUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_36_15', minute=minute_15, second='25',
                      args=("OCEANUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_15', minute=minute_15, second='25',
                      args=("FLMUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40_15', minute=minute_15, second='25',
                      args=("KEEPUSDT", 27, 75.5, 10, 10, '15m',))  # 15min

    ##################################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_30', minute=minute_30, second='25',
                      args=("LITUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_30', minute=minute_30, second='25',
                      args=("C98USDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_30', minute=minute_30, second='25',
                      args=("1INCHUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_30', minute=minute_30, second='26',
                      args=("CRVUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_30', minute=minute_30, second='26',
                      args=("AUDIOUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_30', minute=minute_30, second='26',
                      args=("TOMOUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_30', minute=minute_30, second='26',
                      args=("ICXUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_30', minute=minute_30, second='26',
                      args=("BAKEUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_30', minute=minute_30, second='26',
                      args=("ALGOUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_30', minute=minute_30, second='27',
                      args=("ENJUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_30', minute=minute_30, second='27',
                      args=("FTMUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_30', minute=minute_30, second='27',
                      args=("MATICUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_30', minute=minute_30, second='27',
                      args=("IOTAUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_30', minute=minute_30, second='27',
                      args=("ALPHAUSDT", 24, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_30', minute=minute_30, second='27',
                      args=("SANDUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34_30', minute=minute_30, second='28',
                      args=("MANAUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_35_30', minute=minute_30, second='28',
                      args=("GRTUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_38_30', minute=minute_30, second='28',
                      args=("CVCUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40_30', minute=minute_30, second='28',
                      args=("KEEPUSDT", 28, 75.5, 10, 10, '30m',))  # 30min

    ############################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_60', minute='0', second='28',
                      args=("RLCUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_60', minute='0', second='28',
                      args=("C98USDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_60', minute='0', second='29',
                      args=("MTLUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_60', minute='0', second='29',
                      args=("1INCHUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_60', minute='0', second='29',
                      args=("CRVUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_60', minute='0', second='29',
                      args=("AUDIOUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_60', minute='0', second='29',
                      args=("TOMOUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_60', minute='0', second='29',
                      args=("ADAUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_60', minute='0', second='30',
                      args=("ICXUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_60', minute='0', second='30',
                      args=("ALGOUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_60', minute='0', second='30',
                      args=("KNCUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_60', minute='0', second='30',
                      args=("DODOUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_60', minute='0', second='30',
                      args=("STORJUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_60', minute='0', second='30',
                      args=("XRPUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_60', minute='0', second='31',
                      args=("RENUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_60', minute='0', second='31',
                      args=("ZRXUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_60', minute='0', second='31',
                      args=("ALPHAUSDT", 24, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_60', minute='0', second='31',
                      args=("ATAUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_60', minute='0', second='31',
                      args=("ONTUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_32_60', minute='0', second='31',
                      args=("OGNUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_60', minute='0', second='32',
                      args=("SANDUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34_60', minute='0', second='32',
                      args=("MANAUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37_60', minute='0', second='32',
                      args=("BATUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_39_60', minute='0', second='32',
                      args=("FLMUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_40_60', minute='0', second='32',
                      args=("KEEPUSDT", 28, 75.5, 10, 10, '1h',))  # 1H

    ########################################################################

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_61', hour=hour_2, minute='0',
                      second='32', args=("RLCUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_61', hour=hour_2, minute='0',
                      second='33', args=("SXPUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_61', hour=hour_2, minute='0',
                      second='33', args=("TOMOUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_61', hour=hour_2, minute='0',
                      second='33', args=("ADAUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_61', hour=hour_2, minute='0',
                      second='33', args=("ICXUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_61', hour=hour_2, minute='0',
                      second='33', args=("BELUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_61', hour=hour_2, minute='0',
                      second='33', args=("ALGOUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_61', hour=hour_2,  minute='0',
                      second='34', args=("CTKUSDT", 22, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_61', hour=hour_2, minute='0',
                      second='34', args=("KNCUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_61', hour=hour_2, minute='0',
                      second='34', args=("MATICUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_61', hour=hour_2, minute='0',
                      second='34', args=("STORJUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_61', hour=hour_2, minute='0',
                      second='34', args=("XRPUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_61', hour=hour_2, minute='0',
                      second='34', args=("RENUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_61', hour=hour_2, minute='0',
                      second='35', args=("SFPUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_61', hour=hour_2, minute='0',
                      second='35', args=("ZRXUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_61', hour=hour_2, minute='0',
                      second='35', args=("ATAUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_61', hour=hour_2, minute='0',
                      second='35', args=("ONTUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_33_61', hour=hour_2, minute='0',
                      second='35', args=("SANDUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_34_61', hour=hour_2, minute='0',
                      second='35', args=("MANAUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37_61', hour=hour_2, minute='0',
                      second='36', args=("BATUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_38_61', hour=hour_2, minute='0',
                      second='36', args=("CVCUSDT", 28, 75.5, 10, 10, '2h',))  # 2h

    #########################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_62', hour=hour_4, minute='0',
                      second='36', args=("1INCHUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_62', hour=hour_4, minute='0',
                      second='36', args=("CRVUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_62', hour=hour_4, minute='0',
                      second='36', args=("TOMOUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_62', hour=hour_4, minute='0',
                      second='36', args=("ADAUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_62', hour=hour_4, minute='0',
                      second='37', args=("ICXUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_62', hour=hour_4, minute='0',
                      second='37', args=("BELUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_62', hour=hour_4, minute='0',
                      second='37', args=("ALGOUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_62', hour=hour_4, minute='0',
                      second='37', args=("CTKUSDT", 22, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_62', hour=hour_4, minute='0',
                      second='37', args=("ENJUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_62', hour=hour_4, minute='0',
                      second='37', args=("FTMUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_62', hour=hour_4, minute='0',
                      second='38', args=("MATICUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_62', hour=hour_4, minute='0',
                      second='38', args=("IOTAUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_62', hour=hour_4, minute='0',
                      second='38', args=("STORJUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_62', hour=hour_4, minute='0',
                      second='38', args=("XRPUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_62', hour=hour_4, minute='0',
                      second='38', args=("RENUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_37_62', hour=hour_4, minute='0',
                      second='38', args=("BATUSDT", 28, 75.5, 10, 10, '4h',))  # 4h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_38_62', hour=hour_4, minute='0',
                      second='39', args=("CVCUSDT", 28, 75.5, 10, 10, '4h',))  # 4h

    #################################################

    scheduler.add_job(RunTrade.get_position, trigger='cron', id='TradeRunSp', second='*/10')
    scheduler.start()
