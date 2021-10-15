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
                      args=("LRCUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2', second='2',
                      args=("HBARUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3', second='2',
                      args=("CHRUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4', second='2',
                      args=("SKLUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5', second='2',
                      args=("NKNUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6', second='2',
                      args=("XLMUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7', second='3',
                      args=("BZRXUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8', second='3',
                      args=("CHZUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9', second='3',
                      args=("1000XECUSDT", 19, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10', second='3',
                      args=("BLZUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11', second='3',
                      args=("DOGEUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12', second='3',
                      args=("TLMUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13', second='4',
                      args=("ONEUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14', second='4',
                      args=("XEMUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15', second='4',
                      args=("CELRUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16', second='4',
                      args=("VETUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17', second='4',
                      args=("RVNUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18', second='4',
                      args=("GALAUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19', second='5',
                      args=("ZILUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20', second='5',
                      args=("TRXUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21', second='5',
                      args=("ANKRUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22', second='5',
                      args=("IOSTUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23', second='5',
                      args=("DGBUSDT", 19, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24', second='5',
                      args=("RSRUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25', second='6',
                      args=("LINAUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26', second='6',
                      args=("BTSUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27', second='6',
                      args=("STMXUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28', second='6',
                      args=("AKROUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29', second='6',
                      args=("SCUSDT", 20.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30', second='6',
                      args=("1000SHIBUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31', second='7',
                      args=("DENTUSDT", 20.5, 90.5, 10, 10, '1m',))  # 1min


    #############################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS3_1_3', minute=minute_3, second='7',
                      args=("LRCUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_3', minute=minute_3, second='7',
                      args=("HBARUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_3', minute=minute_3, second='7',
                      args=("CHRUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_3', minute=minute_3, second='7',
                      args=("SKLUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_3', minute=minute_3, second='7',
                      args=("NKNUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_3', minute=minute_3, second='8',
                      args=("XLMUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_3', minute=minute_3, second='8',
                      args=("BZRXUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_3', minute=minute_3, second='8',
                      args=("CHZUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_3', minute=minute_3, second='8',
                      args=("BLZUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_3', minute=minute_3, second='8',
                      args=("DOGEUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_3', minute=minute_3, second='8',
                      args=("TLMUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_3', minute=minute_3, second='9',
                      args=("ONEUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_3', minute=minute_3, second='9',
                      args=("XEMUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_3', minute=minute_3, second='9',
                      args=("CELRUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_3', minute=minute_3, second='9',
                      args=("RVNUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_3', minute=minute_3, second='9',
                      args=("GALAUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_3', minute=minute_3, second='9',
                      args=("ZILUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_3', minute=minute_3, second='10',
                      args=("TRXUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_3', minute=minute_3, second='10',
                      args=("ANKRUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_3', minute=minute_3, second='10',
                      args=("IOSTUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_3', minute=minute_3, second='10',
                      args=("DGBUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_3', minute=minute_3, second='10',
                      args=("RSRUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_3', minute=minute_3, second='10',
                      args=("LINAUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_3', minute=minute_3, second='11',
                      args=("BTSUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_3', minute=minute_3, second='11',
                      args=("STMXUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_3', minute=minute_3, second='11',
                      args=("AKROUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_3', minute=minute_3, second='11',
                      args=("SCUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_3', minute=minute_3, second='11',
                      args=("1000SHIBUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_3', minute=minute_3, second='11',
                      args=("DENTUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    ###############################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_5', minute=minute_5, second='12',
                      args=("HBARUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_5', minute=minute_5, second='12',
                      args=("CHRUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_5', minute=minute_5, second='12',
                      args=("SKLUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_5', minute=minute_5, second='12',
                      args=("NKNUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_5', minute=minute_5, second='12',
                      args=("BZRXUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_5', minute=minute_5, second='12',
                      args=("CHZUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_5', minute=minute_5, second='13',
                      args=("1000XECUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_5', minute=minute_5, second='13',
                      args=("BLZUSDT", 25.5, 80.5, 10, 10, '5m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_5', minute=minute_5, second='13',
                      args=("DOGEUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_5', minute=minute_5, second='13',
                      args=("ONEUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_5', minute=minute_5, second='13',
                      args=("CELRUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_5', minute=minute_5, second='13',
                      args=("VETUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_5', minute=minute_5, second='14',
                      args=("GALAUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_5', minute=minute_5, second='14',
                      args=("ANKRUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_5', minute=minute_5, second='14',
                      args=("IOSTUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_5', minute=minute_5, second='14',
                      args=("DGBUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_5', minute=minute_5, second='14',
                      args=("LINAUSDT", 25.5, 80.5, 10, 10, '5m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_5', minute=minute_5, second='14',
                      args=("BTSUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_27_5', minute=minute_5, second='15',
                      args=("STMXUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_5', minute=minute_5, second='15',
                      args=("AKROUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_5', minute=minute_5, second='15',
                      args=("SCUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_5', minute=minute_5, second='15',
                      args=("1000SHIBUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_5', minute=minute_5, second='15',
                      args=("DENTUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    ##################################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS15_1_15', minute=minute_15, second='15',
                      args=("LRCUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_15', minute=minute_15, second='16',
                      args=("HBARUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_15', minute=minute_15, second='16',
                      args=("CHRUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_15', minute=minute_15, second='16',
                      args=("SKLUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_15', minute=minute_15, second='16',
                      args=("NKNUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_15', minute=minute_15, second='16',
                      args=("XLMUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_15', minute=minute_15, second='16',
                      args=("BZRXUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_15', minute=minute_15, second='17',
                      args=("1000XECUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_15', minute=minute_15, second='17',
                      args=("BLZUSDT", 27, 75.5, 10, 10, '15m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_15', minute=minute_15, second='17',
                      args=("TLMUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_15', minute=minute_15, second='17',
                      args=("ONEUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_15', minute=minute_15, second='17',
                      args=("CELRUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_15', minute=minute_15, second='17',
                      args=("RVNUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_15', minute=minute_15, second='18',
                      args=("GALAUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_15', minute=minute_15, second='18',
                      args=("ZILUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_15', minute=minute_15, second='18',
                      args=("ANKRUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_15', minute=minute_15, second='18',
                      args=("IOSTUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_15', minute=minute_15, second='18',
                      args=("DGBUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_25_15', minute=minute_15, second='18',
                      args=("LINAUSDT", 27, 75.5, 10, 10, '15m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_15', minute=minute_15, second='19',
                      args=("AKROUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_15', minute=minute_15, second='19',
                      args=("1000SHIBUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_31_15', minute=minute_15, second='19',
                      args=("DENTUSDT", 27, 75.5, 10, 10, '15m',))  # 15min

    #############################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_30', minute=minute_30, second='19',
                      args=("CHRUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_30', minute=minute_30, second='19',
                      args=("NKNUSDT", 28, 75.5, 10, 10, '30m',))  # 30min.
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_30', minute=minute_30, second='19',
                      args=("BZRXUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_30', minute=minute_30, second='20',
                      args=("1000XECUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_30', minute=minute_30, second='20',
                      args=("BLZUSDT", 28, 75.5, 10, 10, '30m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_30', minute=minute_30, second='20',
                      args=("TLMUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_30', minute=minute_30, second='20',
                      args=("ONEUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_30', minute=minute_30, second='20',
                      args=("CELRUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_30', minute=minute_30, second='20',
                      args=("RVNUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_30', minute=minute_30, second='21',
                      args=("GALAUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_30', minute=minute_30, second='21',
                      args=("ZILUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_30', minute=minute_30, second='21',
                      args=("ANKRUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_30', minute=minute_30, second='21',
                      args=("IOSTUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_29_30', minute=minute_30, second='21',
                      args=("SCUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_30_30', minute=minute_30, second='21',
                      args=("1000SHIBUSDT", 28, 75.5, 10, 10, '30m',))  # 30min

    ##################################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1h_1_60', minute='0', second='22',
                      args=("LRCUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_60', minute='0', second='22',
                      args=("HBARUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_60', minute='0', second='22',
                      args=("CHRUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_60', minute='0', second='22',
                      args=("SKLUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_60', minute='0', second='22',
                      args=("BZRXUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_60', minute='0', second='22',
                      args=("CHZUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_60', minute='0', second='21',
                      args=("BLZUSDT", 28, 75.5, 10, 10, '1h',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_60', minute='0', second='21',
                      args=("DOGEUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_60', minute='0', second='21',
                      args=("ONEUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_60', minute='0', second='21',
                      args=("CELRUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_60', minute='0', second='21',
                      args=("RVNUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_60', minute='0', second='21',
                      args=("TRXUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_60', minute='0', second='22',
                      args=("ANKRUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_60', minute='0', second='22',
                      args=("IOSTUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_60', minute='0', second='22',
                      args=("RSRUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_60', minute='0', second='22',
                      args=("BTSUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_28_60', minute='0', second='22',
                      args=("AKROUSDT", 28, 75.5, 10, 10, '1h',))  # 1h

    ########################################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_70', hour=hour_2, minute='0',
                      second='22', args=("HBARUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_70', hour=hour_2, minute='0',
                      second='23', args=("CHRUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_70', hour=hour_2, minute='0',
                      second='23', args=("SKLUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_70', hour=hour_2, minute='0',
                      second='23', args=("CHZUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_70', hour=hour_2, minute='0',
                      second='23', args=("BLZUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_70', hour=hour_2, minute='0',
                      second='23', args=("DOGEUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_70', hour=hour_2, minute='0',
                      second='23', args=("ONEUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_70', hour=hour_2, minute='0',
                      second='24', args=("XEMUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_70', hour=hour_2, minute='0',
                      second='24', args=("CELRUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_70', hour=hour_2, minute='0',
                      second='24', args=("VETUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_70', hour=hour_2, minute='0',
                      second='24', args=("RVNUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_70', hour=hour_2, minute='0',
                      second='24', args=("ZILUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_70', hour=hour_2, minute='0',
                      second='24', args=("TRXUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_70', hour=hour_2, minute='0',
                      second='25', args=("ANKRUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_70', hour=hour_2, minute='0',
                      second='25', args=("IOSTUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_23_70', hour=hour_2, minute='0',
                      second='25', args=("DGBUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_24_70', hour=hour_2, minute='0',
                      second='25', args=("RSRUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_26_70', hour=hour_2, minute='0',
                      second='25', args=("BTSUSDT", 28, 75.5, 10, 10, '2h',))  # 2h

    ############################################################################################
    scheduler.add_job(RunTrade.get_position, trigger='cron', id='TradeRunSp', second='*/10')
    scheduler.start()
