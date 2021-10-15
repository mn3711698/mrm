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
    minute_3 = '0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57'
    minute_5 = '0,5,10,15,20,25,30,35,40,45,50,55'
    minute_15 = '0,15,30,45'
    minute_30 = '0,30'
    hour_2 = '0,2,4,6,8,10,12,14,16,18,20,22'
    hour_4 = '0,4,8,12,16,20'

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM1', second='2',
                      args=("AAVEUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2', second='2',
                      args=("KSMUSDT", 19, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3', second='2',
                      args=("UNIUSDT", 21.5, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4', second='2',
                      args=("EGLDUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5', second='2',
                      args=("DOTUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM6', second='2',
                      args=("BCHUSDT", 21, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7', second='3',
                      args=("LUNAUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8', second='3',
                      args=("TRBUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9', second='3',
                      args=("NEOUSDT", 21.5, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM10', second='3',
                      args=("COMPUSDT", 21.5, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11', second='3',
                      args=("ATOMUSDT", 21, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12', second='3',
                      args=("BNBUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13', second='4',
                      args=("SOLUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14', second='4',
                      args=("MKRUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM15', second='4',
                      args=("YFIIUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16', second='4',
                      args=("XMRUSDT", 21.5, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM17', second='4',
                      args=("AVAXUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM18', second='4',
                      args=("NEARUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20', second='5',
                      args=("YFIUSDT", 21.5, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21', second='5',
                      args=("ETHUSDT", 21.5, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM22', second='5',
                      args=("LTCUSDT", 20, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23', second='5',
                      args=("DASHUSDT", 21.5, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24', second='5',
                      args=("ZECUSDT", 22, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM25', second='5',
                      args=("ZENUSDT", 21.5, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM26', second='6',
                      args=("FILUSDT", 21.5, 90.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1', second='6',
                      args=("AXSUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2', second='6',
                      args=("ICPUSDT", 21, 90.5, 10, 10, '1m',))  # 1min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3', second='6',
                      args=("WAVESUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4', second='6',
                      args=("LINKUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5', second='6',
                      args=("BALUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6', second='7',
                      args=("HNTUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7', second='7',
                      args=("DYDXUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8', second='7',
                      args=("ALICEUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9', second='7',
                      args=("SNXUSDT", 21, 90.5, 10, 10, '1m',))  # 1min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10', second='7',
                      args=("QTUMUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11', second='7',
                      args=("RAYUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12', second='8',
                      args=("SUSHIUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13', second='8',
                      args=("OMGUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14', second='8',
                      args=("MASKUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15', second='8',
                      args=("UNFIUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16', second='8',
                      args=("SRMUSDT", 21, 90.5, 10, 10, '1m',))  # 1min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17', second='8',
                      args=("GTCUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18', second='9',
                      args=("RUNEUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19', second='9',
                      args=("BANDUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20', second='9',
                      args=("XTZUSDT", 20, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21', second='9',
                      args=("THETAUSDT", 21, 90.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22', second='9',
                      args=("KAVAUSDT", 21, 90.5, 10, 10, '1m',))  # 1min

    ###############################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM1_3', minute=minute_3, second='9',
                      args=("AAVEUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2_3', minute=minute_3, second='10',
                      args=("KSMUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_3', minute=minute_3, second='10',
                      args=("UNIUSDT", 24, 85.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4_3', minute=minute_3, second='10',
                      args=("EGLDUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5_3', minute=minute_3, second='10',
                      args=("DOTUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM6_3', minute=minute_3, second='10',
                      args=("BCHUSDT", 24, 85.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_3', minute=minute_3, second='10',
                      args=("LUNAUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8_3', minute=minute_3, second='11',
                      args=("TRBUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9_3', minute=minute_3, second='11',
                      args=("NEOUSDT", 24, 85.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM10_3', minute=minute_3, second='11',
                      args=("COMPUSDT", 24, 85.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12_3', minute=minute_3, second='11',
                      args=("BNBUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14_3', minute=minute_3, second='11',
                      args=("MKRUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM15_3', minute=minute_3, second='11',
                      args=("YFIIUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_3', minute=minute_3, second='12',
                      args=("XMRUSDT", 24, 85.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM18_3', minute=minute_3, second='12',
                      args=("NEARUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20_3', minute=minute_3, second='12',
                      args=("YFIUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21_3', minute=minute_3, second='12',
                      args=("ETHUSDT", 24, 85.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM22_3', minute=minute_3, second='12',
                      args=("LTCUSDT", 24, 85.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23_3', minute=minute_3, second='12',
                      args=("DASHUSDT", 24, 85.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24_3', minute=minute_3, second='13',
                      args=("ZECUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM25_3', minute=minute_3, second='13',
                      args=("ZENUSDT", 24, 85.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_3', minute=minute_3, second='13',
                      args=("AXSUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_3', minute=minute_3, second='13',
                      args=("ICPUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_3', minute=minute_3, second='13',
                      args=("WAVESUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_3', minute=minute_3, second='13',
                      args=("LINKUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_3', minute=minute_3, second='14',
                      args=("BALUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_3', minute=minute_3, second='14',
                      args=("HNTUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_3', minute=minute_3, second='14',
                      args=("DYDXUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_3', minute=minute_3, second='14',
                      args=("ALICEUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_3', minute=minute_3, second='14',
                      args=("SNXUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_3', minute=minute_3, second='14',
                      args=("QTUMUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_3', minute=minute_3, second='15',
                      args=("RAYUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_3', minute=minute_3, second='15',
                      args=("SUSHIUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_3', minute=minute_3, second='15',
                      args=("MASKUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_3', minute=minute_3, second='15',
                      args=("UNFIUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_3', minute=minute_3, second='15',
                      args=("GTCUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_3', minute=minute_3, second='15',
                      args=("BANDUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_3', minute=minute_3, second='16',
                      args=("XTZUSDT", 24, 85.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_3', minute=minute_3, second='16',
                      args=("THETAUSDT", 24, 85.5, 10, 10, '3m',))  # 3min

    ###############################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_5', minute=minute_5, second='16',
                      args=("UNIUSDT", 25.5, 80.5, 5, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4_5', minute=minute_5, second='16',
                      args=("EGLDUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5_5', minute=minute_5, second='16',
                      args=("DOTUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_5', minute=minute_5, second='16',
                      args=("LUNAUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8_5', minute=minute_5, second='17',
                      args=("TRBUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9_5', minute=minute_5, second='17',
                      args=("NEOUSDT", 25.5, 80.5, 5, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11_5', minute=minute_5, second='17',
                      args=("ATOMUSDT", 25.5, 80.5, 5, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12_5', minute=minute_5, second='17',
                      args=("BNBUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13_5', minute=minute_5, second='17',
                      args=("SOLUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM15_5', minute=minute_5, second='17',
                      args=("YFIIUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_5', minute=minute_5, second='18',
                      args=("XMRUSDT", 25.5, 80.5, 5, 10, '5m',))  # 5min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20_5', minute=minute_5, second='18',
                      args=("YFIUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM22_5', minute=minute_5, second='18',
                      args=("LTCUSDT", 25.5, 80.5, 5, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23_5', minute=minute_5, second='18',
                      args=("DASHUSDT", 25.5, 80.5, 5, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24_5', minute=minute_5, second='18',
                      args=("ZECUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_5', minute=minute_5, second='18',
                      args=("AXSUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_5', minute=minute_5, second='19',
                      args=("ICPUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_5', minute=minute_5, second='19',
                      args=("WAVESUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_5', minute=minute_5, second='19',
                      args=("LINKUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_5', minute=minute_5, second='19',
                      args=("HNTUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_5', minute=minute_5, second='19',
                      args=("DYDXUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_5', minute=minute_5, second='19',
                      args=("ALICEUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_5', minute=minute_5, second='20',
                      args=("SNXUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_5', minute=minute_5, second='20',
                      args=("QTUMUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_5', minute=minute_5, second='20',
                      args=("SUSHIUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_5', minute=minute_5, second='20',
                      args=("OMGUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_5', minute=minute_5, second='20',
                      args=("MASKUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_5', minute=minute_5, second='20',
                      args=("UNFIUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_5', minute=minute_5, second='21',
                      args=("RUNEUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_5', minute=minute_5, second='21',
                      args=("KAVAUSDT", 25.5, 80.5, 10, 10, '5m',))  # 5min

    ###############################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2_15', minute=minute_15, second='21',
                      args=("KSMUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_15', minute=minute_15, second='21',
                      args=("UNIUSDT", 27, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4_15', minute=minute_15, second='21',
                      args=("EGLDUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5_15', minute=minute_15, second='21',
                      args=("DOTUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_15', minute=minute_15, second='22',
                      args=("LUNAUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8_15', minute=minute_15, second='22',
                      args=("TRBUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9_15', minute=minute_15, second='22',
                      args=("NEOUSDT", 27, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11_15', minute=minute_15, second='22',
                      args=("ATOMUSDT", 27, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12_15', minute=minute_15, second='22',
                      args=("BNBUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13_15', minute=minute_15, second='22',
                      args=("SOLUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14_15', minute=minute_15, second='23',
                      args=("MKRUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM15_15', minute=minute_15, second='23',
                      args=("YFIIUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_15', minute=minute_15, second='23',
                      args=("XMRUSDT", 27, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM17_15', minute=minute_15, second='23',
                      args=("AVAXUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM18_15', minute=minute_15, second='23',
                      args=("NEARUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21_15', minute=minute_15, second='23',
                      args=("ETHUSDT", 27, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM25_15', minute=minute_15, second='24',
                      args=("ZENUSDT", 27, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_15', minute=minute_15, second='24',
                      args=("AXSUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_15', minute=minute_15, second='24',
                      args=("WAVESUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_15', minute=minute_15, second='24',
                      args=("HNTUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_15', minute=minute_15, second='24',
                      args=("DYDXUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_15', minute=minute_15, second='24',
                      args=("ALICEUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_15', minute=minute_15, second='25',
                      args=("SNXUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_15', minute=minute_15, second='25',
                      args=("QTUMUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_15', minute=minute_15, second='25',
                      args=("RAYUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_15', minute=minute_15, second='25',
                      args=("SUSHIUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_15', minute=minute_15, second='25',
                      args=("OMGUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_15', minute=minute_15, second='25',
                      args=("UNFIUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_15', minute=minute_15, second='26',
                      args=("GTCUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_15', minute=minute_15, second='26',
                      args=("RUNEUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_15', minute=minute_15, second='26',
                      args=("BANDUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_15', minute=minute_15, second='26',
                      args=("XTZUSDT", 27, 75.5, 10, 10, '15m',))  # 15min

    #############################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2_30', minute=minute_30, second='26',
                      args=("KSMUSDT", 27, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_30', minute=minute_30, second='26',
                      args=("UNIUSDT", 28, 75.5, 5, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4_30', minute=minute_30, second='27',
                      args=("EGLDUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5_30', minute=minute_30, second='27',
                      args=("DOTUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_30', minute=minute_30, second='27',
                      args=("LUNAUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11_30', minute=minute_30, second='27',
                      args=("ATOMUSDT", 28, 75.5, 5, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13_30', minute=minute_30, second='27',
                      args=("SOLUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14_30', minute=minute_30, second='27',
                      args=("MKRUSDT", 27, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_30', minute=minute_30, second='28',
                      args=("XMRUSDT", 28, 75.5, 5, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM17_30', minute=minute_30, second='28',
                      args=("AVAXUSDT", 27, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM18_30', minute=minute_30, second='28',
                      args=("NEARUSDT", 27, 75.5, 10, 10, '30m',))  # 30min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20_30', minute=minute_30, second='28',
                      args=("YFIUSDT", 27, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21_30', minute=minute_30, second='28',
                      args=("ETHUSDT", 27, 75.5, 5, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24_30', minute=minute_30, second='28',
                      args=("ZECUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_30', minute=minute_30, second='29',
                      args=("AXSUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_30', minute=minute_30, second='29',
                      args=("WAVESUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_30', minute=minute_30, second='29',
                      args=("LINKUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_30', minute=minute_30, second='29',
                      args=("HNTUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_30', minute=minute_30, second='29',
                      args=("DYDXUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_30', minute=minute_30, second='29',
                      args=("ALICEUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_30', minute=minute_30, second='30',
                      args=("SNXUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_30', minute=minute_30, second='30',
                      args=("RAYUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_30', minute=minute_30, second='30',
                      args=("SUSHIUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_30', minute=minute_30, second='30',
                      args=("UNFIUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_30', minute=minute_30, second='30',
                      args=("SRMUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_30', minute=minute_30, second='30',
                      args=("XTZUSDT", 27, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_30', minute=minute_30, second='31',
                      args=("THETAUSDT", 24, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_30', minute=minute_30, second='31',
                      args=("KAVAUSDT", 26, 75.5, 10, 10, '30m',))  # 30min


    #############################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2_60', minute='0', second='31',
                      args=("KSMUSDT", 26, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_60', minute='0', second='31',
                      args=("UNIUSDT", 28, 75.5, 5, 10, '1h',))  # 1H
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4_60', minute='0', second='31',
                      args=("EGLDUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5_60', minute='0', second='31',
                      args=("DOTUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_60', minute='0', second='32',
                      args=("LUNAUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8_60', minute='0', second='32',
                      args=("TRBUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9_60', minute='0', second='32',
                      args=("NEOUSDT", 28, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM10_60', minute='0', second='32',
                      args=("COMPUSDT", 28, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11_60', minute='0', second='32',
                      args=("ATOMUSDT", 28, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13_60', minute='0', second='32',
                      args=("SOLUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14_60', minute='0', second='33',
                      args=("YFIIUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_60', minute='0', second='33',
                      args=("XMRUSDT", 28, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM17_60', minute='0', second='33',
                      args=("AVAXUSDT", 27, 75.5, 10, 10, '1h',))  # 1h

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21_60', minute='0', second='33',
                      args=("ETHUSDT", 27, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23_60', minute='0', second='33',
                      args=("DASHUSDT", 27, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM25_60', minute='0', second='33',
                      args=("ZENUSDT", 27, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_60', minute='0', second='34',
                      args=("AXSUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_60', minute='0', second='34',
                      args=("ICPUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_60', minute='0', second='34',
                      args=("WAVESUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_60', minute='0', second='34',
                      args=("LINKUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_60', minute='0', second='34',
                      args=("BALUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_60', minute='0', second='34',
                      args=("SNXUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_60', minute='0', second='35',
                      args=("SUSHIUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_60', minute='0', second='35',
                      args=("OMGUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_60', minute='0', second='35',
                      args=("UNFIUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_60', minute='0', second='35',
                      args=("SRMUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_60', minute='0', second='35',
                      args=("XTZUSDT", 27, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_60', minute='0', second='35',
                      args=("KAVAUSDT", 27.5, 75.5, 10, 10, '1h',))  # 1hour

    ##############################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM1_61',  hour=hour_2, minute='0',
                      second='36', args=("AAVEUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_61', hour=hour_2, minute='0',
                      second='36', args=("UNIUSDT", 28, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM6_61', hour=hour_2, minute='0',
                      second='36', args=("BCHUSDT", 28, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_61', hour=hour_2, minute='0',
                      second='36', args=("LUNAUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8_61', hour=hour_2, minute='0',
                      second='36', args=("TRBUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11_61', hour=hour_2, minute='0',
                      second='36', args=("ATOMUSDT", 28, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12_61', hour=hour_2, minute='0',
                      second='37', args=("BNBUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14_61', hour=hour_2, minute='0',
                      second='37', args=("MKRUSDT", 27, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_61', hour=hour_2, minute='0',
                      second='37', args=("XMRUSDT", 28, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20_61', hour=hour_2, minute='0',
                      second='37', args=("YFIUSDT", 27, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM22_61', hour=hour_2, minute='0',
                      second='37', args=("LTCUSDT", 27, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23_61', hour=hour_2, minute='0',
                      second='37', args=("DASHUSDT", 27, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24_61', hour=hour_2, minute='0',
                      second='38', args=("ZECUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_61', hour=hour_2, minute='0',
                      second='38', args=("AXSUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_61', hour=hour_2, minute='0',
                      second='38', args=("WAVESUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_61', hour=hour_2, minute='0',
                      second='38', args=("LINKUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_61', hour=hour_2, minute='0',
                      second='38', args=("BALUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_61', hour=hour_2, minute='0',
                      second='38', args=("HNTUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_61', hour=hour_2, minute='0',
                      second='39', args=("ALICEUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_61', hour=hour_2, minute='0',
                      second='39', args=("SNXUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_61', hour=hour_2, minute='0',
                      second='39', args=("GTCUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_61', hour=hour_2, minute='0',
                      second='39', args=("XTZUSDT", 27, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_61', hour=hour_2, minute='0',
                      second='39', args=("THETAUSDT", 24, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_61', hour=hour_2, minute='0',
                      second='39', args=("KAVAUSDT", 27.5, 75.5, 10, 10, '2h',))  # 2hour

    scheduler.add_job(RunTrade.get_position, trigger='cron', id='TradeRunGMRMp', second='*/10')
    scheduler.start()
