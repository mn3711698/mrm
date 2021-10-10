# -*- coding: utf-8 -*-

##############################################################################
# Author：QQ173782910
##############################################################################

import talib
import logging
from apscheduler.schedulers.background import BlockingScheduler
from RunUse.TradeRun import TradeRun
from config import symbols_conf3

formats = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=formats, filename='gmlog_print.txt')
logger = logging.getLogger('print')
logging.getLogger("apscheduler").setLevel(logging.WARNING)  # 设置apscheduler.


if __name__ == '__main__':  # 25
    RunTrade = TradeRun(symbols_conf3)
    scheduler = BlockingScheduler()  # 定时的任务.
    minute_3 = '0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57'
    minute_5 = '0,5,10,15,20,25,30,35,40,45,50,55'
    minute_15 = '0,15,30,45'
    minute_30 = '0,30'
    hour_2 = '0,2,4,6,8,10,12,14,16,18,20,22'
    hour_4 = '0,4,8,12,16,20'

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1', second='2',
                      args=("LRCUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2', second='2',
                      args=("HBARUSDT", 20, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3', second='2',
                      args=("CHRUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4', second='2',
                      args=("SKLUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5', second='2',
                      args=("NKNUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6', second='2',
                      args=("XLMUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7', second='2',
                      args=("BZRXUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8', second='3',
                      args=("CHZUSDT", 20, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9', second='3',
                      args=("1000XECUSDT", 20, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10', second='3',
                      args=("BLZUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11', second='3',
                      args=("DOGEUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12', second='3',
                      args=("TLMUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13', second='3',
                      args=("ONEUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14', second='3',
                      args=("XEMUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15', second='4',
                      args=("CELRUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16', second='4',
                      args=("VETUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17', second='4',
                      args=("RVNUSDT", 27, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18', second='4',
                      args=("GALAUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19', second='4',
                      args=("ZILUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20', second='4',
                      args=("TRXUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21', second='4',
                      args=("ANKRUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22', second='5',
                      args=("IOSTUSDT", 20, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23', second='5',
                      args=("DGBUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24', second='5',
                      args=("RSRUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25', second='5',
                      args=("LINAUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26', second='5',
                      args=("BTSUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27', second='5',
                      args=("STMXUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28', second='5',
                      args=("AKROUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29', second='6',
                      args=("SCUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30', second='6',
                      args=("1000SHIBUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31', second='6',
                      args=("DENTUSDT", 20, 75.5, 10, 10, '1m',))  # 1min


    #############################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS3_1_3', minute=minute_3, second='7',
                      args=("LRCUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_3', minute=minute_3, second='7',
                      args=("HBARUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_3', minute=minute_3, second='7',
                      args=("CHRUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_3', minute=minute_3, second='7',
                      args=("SKLUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_3', minute=minute_3, second='7',
                      args=("NKNUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_3', minute=minute_3, second='7',
                      args=("XLMUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_3', minute=minute_3, second='7',
                      args=("BZRXUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_3', minute=minute_3, second='8',
                      args=("CHZUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_3', minute=minute_3, second='8',
                      args=("BLZUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_3', minute=minute_3, second='8',
                      args=("DOGEUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_3', minute=minute_3, second='8',
                      args=("TLMUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_3', minute=minute_3, second='8',
                      args=("ONEUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_3', minute=minute_3, second='8',
                      args=("XEMUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_3', minute=minute_3, second='8',
                      args=("CELRUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_3', minute=minute_3, second='9',
                      args=("RVNUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_3', minute=minute_3, second='9',
                      args=("GALAUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_3', minute=minute_3, second='9',
                      args=("ZILUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_3', minute=minute_3, second='9',
                      args=("TRXUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_3', minute=minute_3, second='9',
                      args=("ANKRUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_3', minute=minute_3, second='9',
                      args=("IOSTUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_3', minute=minute_3, second='10',
                      args=("DGBUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_3', minute=minute_3, second='10',
                      args=("RSRUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_3', minute=minute_3, second='10',
                      args=("LINAUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_3', minute=minute_3, second='10',
                      args=("BTSUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_3', minute=minute_3, second='10',
                      args=("STMXUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_3', minute=minute_3, second='10',
                      args=("AKROUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_3', minute=minute_3, second='10',
                      args=("SCUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_3', minute=minute_3, second='6',
                      args=("1000SHIBUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_3', minute=minute_3, second='6',
                      args=("DENTUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    ###############################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_5', minute=minute_5, second='11',
                      args=("HBARUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_5', minute=minute_5, second='11',
                      args=("CHRUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_5', minute=minute_5, second='11',
                      args=("SKLUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_5', minute=minute_5, second='11',
                      args=("NKNUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_5', minute=minute_5, second='11',
                      args=("BZRXUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_5', minute=minute_5, second='11',
                      args=("CHZUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_5', minute=minute_5, second='11',
                      args=("1000XECUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_5', minute=minute_5, second='12',
                      args=("BLZUSDT", 28, 75.5, 10, 10, '5m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_5', minute=minute_5, second='12',
                      args=("DOGEUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_5', minute=minute_5, second='12',
                      args=("ONEUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_5', minute=minute_5, second='12',
                      args=("CELRUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_5', minute=minute_5, second='12',
                      args=("VETUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_5', minute=minute_5, second='12',
                      args=("GALAUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_5', minute=minute_5, second='12',
                      args=("ANKRUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_5', minute=minute_5, second='13',
                      args=("IOSTUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_5', minute=minute_5, second='13',
                      args=("DGBUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_5', minute=minute_5, second='13',
                      args=("LINAUSDT", 28, 75.5, 10, 10, '5m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_5', minute=minute_5, second='13',
                      args=("BTSUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_5', minute=minute_5, second='13',
                      args=("STMXUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_5', minute=minute_5, second='13',
                      args=("AKROUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_5', minute=minute_5, second='13',
                      args=("SCUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_5', minute=minute_5, second='13',
                      args=("1000SHIBUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_5', minute=minute_5, second='6',
                      args=("DENTUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    ##################################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS15_1_15', minute=minute_15, second='14',
                      args=("LRCUSDT", 24, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_15', minute=minute_15, second='14',
                      args=("HBARUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_15', minute=minute_15, second='14',
                      args=("CHRUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_15', minute=minute_15, second='14',
                      args=("SKLUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_15', minute=minute_15, second='14',
                      args=("NKNUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_15', minute=minute_15, second='14',
                      args=("XLMUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_15', minute=minute_15, second='14',
                      args=("BZRXUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_15', minute=minute_15, second='14',
                      args=("1000XECUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_15', minute=minute_15, second='15',
                      args=("BLZUSDT", 28, 75.5, 10, 10, '15m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_15', minute=minute_15, second='15',
                      args=("TLMUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_15', minute=minute_15, second='15',
                      args=("ONEUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_15', minute=minute_15, second='15',
                      args=("CELRUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_15', minute=minute_15, second='15',
                      args=("RVNUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_15', minute=minute_15, second='15',
                      args=("GALAUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_15', minute=minute_15, second='15',
                      args=("ZILUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_15', minute=minute_15, second='15',
                      args=("ANKRUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_15', minute=minute_15, second='16',
                      args=("IOSTUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_15', minute=minute_15, second='16',
                      args=("DGBUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_15', minute=minute_15, second='16',
                      args=("LINAUSDT", 28, 75.5, 10, 10, '15m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_15', minute=minute_15, second='16',
                      args=("AKROUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_15', minute=minute_15, second='16',
                      args=("1000SHIBUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_15', minute=minute_15, second='16',
                      args=("DENTUSDT", 28, 75.5, 10, 10, '15m',))  # 15min


    #############################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_30', minute=minute_30, second='17',
                      args=("CHRUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_30', minute=minute_30, second='17',
                      args=("NKNUSDT", 28, 75.5, 10, 10, '30m',))  # 30min.
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_30', minute=minute_30, second='17',
                      args=("BZRXUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_30', minute=minute_30, second='17',
                      args=("1000XECUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_30', minute=minute_30, second='17',
                      args=("BLZUSDT", 28, 75.5, 10, 10, '30m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_30', minute=minute_30, second='17',
                      args=("TLMUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_30', minute=minute_30, second='17',
                      args=("ONEUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_30', minute=minute_30, second='17',
                      args=("CELRUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_30', minute=minute_30, second='18',
                      args=("RVNUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_30', minute=minute_30, second='18',
                      args=("GALAUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_30', minute=minute_30, second='18',
                      args=("ZILUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_30', minute=minute_30, second='18',
                      args=("ANKRUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_30', minute=minute_30, second='18',
                      args=("IOSTUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_30', minute=minute_30, second='18',
                      args=("SCUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_30', minute=minute_30, second='18',
                      args=("1000SHIBUSDT", 28, 75.5, 10, 10, '30m',))  # 30min

    ##################################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1h_1_60', minute='0', second='19',
                      args=("LRCUSDT", 24, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_60', minute='0', second='19',
                      args=("HBARUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_60', minute='0', second='19',
                      args=("CHRUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_60', minute='0', second='19',
                      args=("SKLUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_60', minute='0', second='19',
                      args=("BZRXUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_60', minute='0', second='19',
                      args=("CHZUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_60', minute='0', second='19',
                      args=("BLZUSDT", 28, 75.5, 10, 10, '1h',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_60', minute='0', second='20',
                      args=("DOGEUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_60', minute='0', second='20',
                      args=("ONEUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_60', minute='0', second='20',
                      args=("CELRUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_60', minute='0', second='20',
                      args=("RVNUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_60', minute='0', second='20',
                      args=("TRXUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_60', minute='0', second='20',
                      args=("ANKRUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_60', minute='0', second='20',
                      args=("IOSTUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_60', minute='0', second='21',
                      args=("RSRUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_60', minute='0', second='21',
                      args=("BTSUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_60', minute='0', second='21',
                      args=("AKROUSDT", 28, 75.5, 10, 10, '1h',))  # 1h


    ########################################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_70', hour=hour_2, minute='0',
                      second='21', args=("HBARUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_70', hour=hour_2, minute='0',
                      second='21', args=("CHRUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_70', hour=hour_2, minute='0',
                      second='21', args=("SKLUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_70', hour=hour_2, minute='0',
                      second='21', args=("CHZUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_70', hour=hour_2, minute='0',
                      second='22', args=("BLZUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_70', hour=hour_2, minute='0',
                      second='22', args=("DOGEUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_70', hour=hour_2, minute='0',
                      second='22', args=("ONEUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_70', hour=hour_2, minute='0',
                      second='22', args=("XEMUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_70', hour=hour_2, minute='0',
                      second='22', args=("CELRUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_70', hour=hour_2, minute='0',
                      second='22', args=("VETUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_70', hour=hour_2, minute='0',
                      second='22', args=("RVNUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_70', hour=hour_2, minute='0',
                      second='23', args=("ZILUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_70', hour=hour_2, minute='0',
                      second='23', args=("TRXUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_70', hour=hour_2, minute='0',
                      second='23', args=("ANKRUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_70', hour=hour_2, minute='0',
                      second='23', args=("IOSTUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_70', hour=hour_2, minute='0',
                      second='23', args=("DGBUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_70', hour=hour_2, minute='0',
                      second='23', args=("RSRUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_70', hour=hour_2, minute='0',
                      second='23', args=("BTSUSDT", 28, 75.5, 10, 10, '2h',))  # 2h

    ############################################################################################
    scheduler.add_job(RunTrade.get_position, trigger='cron', id='TradeRunSp', second='*/10')
    scheduler.start()
