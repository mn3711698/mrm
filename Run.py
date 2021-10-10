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
                      args=("AAVEUSDT", 25, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2', second='2',
                      args=("KSMUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3', second='2',
                      args=("UNIUSDT", 26, 75.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4', second='2',
                      args=("EGLDUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5', second='2',
                      args=("DOTUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM6', second='2',
                      args=("BCHUSDT", 22, 75.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7', second='2',
                      args=("LUNAUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8', second='3',
                      args=("TRBUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9', second='3',
                      args=("NEOUSDT", 26, 75.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM10', second='3',
                      args=("COMPUSDT", 26, 75.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11', second='3',
                      args=("ATOMUSDT", 22, 75.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12', second='3',
                      args=("BNBUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13', second='3',
                      args=("SOLUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14', second='3',
                      args=("MKRUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM15', second='4',
                      args=("YFIIUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16', second='4',
                      args=("XMRUSDT", 26, 75.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM17', second='4',
                      args=("AVAXUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM18', second='4',
                      args=("NEARUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20', second='4',
                      args=("YFIUSDT", 25, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21', second='4',
                      args=("ETHUSDT", 25, 75.5, 5, 10, '1m',))  # 1min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM22', second='5',
                      args=("LTCUSDT", 24, 75.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23', second='5',
                      args=("DASHUSDT", 25.5, 75.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24', second='5',
                      args=("ZECUSDT", 26, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM25', second='5',
                      args=("ZENUSDT", 25, 75.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM26', second='5',
                      args=("FILUSDT", 25.5, 75.5, 5, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1', second='5',
                      args=("AXSUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2', second='5',
                      args=("ICPUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3', second='6',
                      args=("WAVESUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4', second='6',
                      args=("LINKUSDT", 23, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5', second='6',
                      args=("BALUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6', second='6',
                      args=("HNTUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7', second='6',
                      args=("DYDXUSDT", 22, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8', second='6',
                      args=("ALICEUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9', second='6',
                      args=("SNXUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10', second='7',
                      args=("QTUMUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11', second='7',
                      args=("RAYUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12', second='7',
                      args=("SUSHIUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13', second='7',
                      args=("OMGUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14', second='7',
                      args=("MASKUSDT", 24, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15', second='7',
                      args=("UNFIUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16', second='7',
                      args=("SRMUSDT", 23, 75.5, 10, 10, '1m',))  # 1min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17', second='8',
                      args=("GTCUSDT", 25, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18', second='8',
                      args=("RUNEUSDT", 23, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19', second='8',
                      args=("BANDUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20', second='8',
                      args=("XTZUSDT", 23, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21', second='8',
                      args=("THETAUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22', second='8',
                      args=("KAVAUSDT", 25.5, 75.5, 10, 10, '1m',))  # 1min

    ###############################################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM1_3', minute=minute_3, second='9',
                      args=("AAVEUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2_3', minute=minute_3, second='9',
                      args=("KSMUSDT", 26, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_3', minute=minute_3, second='9',
                      args=("UNIUSDT", 28, 75.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4_3', minute=minute_3, second='9',
                      args=("EGLDUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5_3', minute=minute_3, second='9',
                      args=("DOTUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM6_3', minute=minute_3, second='9',
                      args=("BCHUSDT", 26, 75.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_3', minute=minute_3, second='9',
                      args=("LUNAUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8_3', minute=minute_3, second='10',
                      args=("TRBUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9_3', minute=minute_3, second='10',
                      args=("NEOUSDT", 28, 75.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM10_3', minute=minute_3, second='10',
                      args=("COMPUSDT", 28, 75.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12_3', minute=minute_3, second='10',
                      args=("BNBUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14_3', minute=minute_3, second='10',
                      args=("MKRUSDT", 27, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM15_3', minute=minute_3, second='10',
                      args=("YFIIUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_3', minute=minute_3, second='10',
                      args=("XMRUSDT", 28, 75.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM18_3', minute=minute_3, second='11',
                      args=("NEARUSDT", 27, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20_3', minute=minute_3, second='11',
                      args=("YFIUSDT", 27, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21_3', minute=minute_3, second='11',
                      args=("ETHUSDT", 27, 75.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM22_3', minute=minute_3, second='11',
                      args=("LTCUSDT", 27, 75.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23_3', minute=minute_3, second='11',
                      args=("DASHUSDT", 27, 75.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24_3', minute=minute_3, second='11',
                      args=("ZECUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM25_3', minute=minute_3, second='11',
                      args=("ZENUSDT", 27, 75.5, 5, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_3', minute=minute_3, second='12',
                      args=("AXSUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_3', minute=minute_3, second='12',
                      args=("ICPUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_3', minute=minute_3, second='12',
                      args=("WAVESUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_3', minute=minute_3, second='12',
                      args=("LINKUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_3', minute=minute_3, second='12',
                      args=("BALUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_3', minute=minute_3, second='12',
                      args=("HNTUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_3', minute=minute_3, second='12',
                      args=("DYDXUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_3', minute=minute_3, second='13',
                      args=("ALICEUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_3', minute=minute_3, second='13',
                      args=("SNXUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_3', minute=minute_3, second='13',
                      args=("QTUMUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_3', minute=minute_3, second='13',
                      args=("RAYUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_3', minute=minute_3, second='13',
                      args=("SUSHIUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_3', minute=minute_3, second='13',
                      args=("MASKUSDT", 27, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_3', minute=minute_3, second='13',
                      args=("UNFIUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_3', minute=minute_3, second='14',
                      args=("GTCUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_3', minute=minute_3, second='14',
                      args=("BANDUSDT", 28, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_3', minute=minute_3, second='14',
                      args=("XTZUSDT", 27, 75.5, 10, 10, '3m',))  # 3min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_3', minute=minute_3, second='14',
                      args=("THETAUSDT", 28, 75.5, 10, 10, '3m',))  # 3min

    ###############################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_5', minute=minute_5, second='14',
                      args=("UNIUSDT", 28, 75.5, 5, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4_5', minute=minute_5, second='14',
                      args=("EGLDUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5_5', minute=minute_5, second='14',
                      args=("DOTUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_5', minute=minute_5, second='15',
                      args=("LUNAUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8_5', minute=minute_5, second='15',
                      args=("TRBUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9_5', minute=minute_5, second='15',
                      args=("NEOUSDT", 28, 75.5, 5, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11_5', minute=minute_5, second='15',
                      args=("ATOMUSDT", 28, 75.5, 5, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12_5', minute=minute_5, second='15',
                      args=("BNBUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13_5', minute=minute_5, second='15',
                      args=("SOLUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM15_5', minute=minute_5, second='15',
                      args=("YFIIUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_5', minute=minute_5, second='16',
                      args=("XMRUSDT", 28, 75.5, 5, 10, '5m',))  # 5min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20_5', minute=minute_5, second='16',
                      args=("YFIUSDT", 27, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM22_5', minute=minute_5, second='16',
                      args=("LTCUSDT", 27, 75.5, 5, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23_5', minute=minute_5, second='16',
                      args=("DASHUSDT", 27, 75.5, 5, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24_5', minute=minute_5, second='16',
                      args=("ZECUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_5', minute=minute_5, second='16',
                      args=("AXSUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_5', minute=minute_5, second='17',
                      args=("ICPUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_5', minute=minute_5, second='17',
                      args=("WAVESUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_5', minute=minute_5, second='17',
                      args=("LINKUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_5', minute=minute_5, second='17',
                      args=("HNTUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_5', minute=minute_5, second='17',
                      args=("DYDXUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_5', minute=minute_5, second='17',
                      args=("ALICEUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_5', minute=minute_5, second='17',
                      args=("SNXUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_5', minute=minute_5, second='18',
                      args=("QTUMUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_5', minute=minute_5, second='18',
                      args=("SUSHIUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_5', minute=minute_5, second='18',
                      args=("OMGUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_14_5', minute=minute_5, second='18',
                      args=("MASKUSDT", 27, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_5', minute=minute_5, second='18',
                      args=("UNFIUSDT", 28, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_5', minute=minute_5, second='18',
                      args=("RUNEUSDT", 27, 75.5, 10, 10, '5m',))  # 5min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_5', minute=minute_5, second='18',
                      args=("KAVAUSDT", 27, 75.5, 10, 10, '5m',))  # 5min

    ###############################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2_15', minute=minute_15, second='18',
                      args=("KSMUSDT", 26, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_15', minute=minute_15, second='19',
                      args=("UNIUSDT", 28, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4_15', minute=minute_15, second='19',
                      args=("EGLDUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5_15', minute=minute_15, second='19',
                      args=("DOTUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_15', minute=minute_15, second='19',
                      args=("LUNAUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8_15', minute=minute_15, second='19',
                      args=("TRBUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9_15', minute=minute_15, second='19',
                      args=("NEOUSDT", 28, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11_15', minute=minute_15, second='19',
                      args=("ATOMUSDT", 28, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12_15', minute=minute_15, second='19',
                      args=("BNBUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13_15', minute=minute_15, second='20',
                      args=("SOLUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14_15', minute=minute_15, second='20',
                      args=("MKRUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM15_15', minute=minute_15, second='20',
                      args=("YFIIUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_15', minute=minute_15, second='20',
                      args=("XMRUSDT", 28, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM17_15', minute=minute_15, second='20',
                      args=("AVAXUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM18_15', minute=minute_15, second='20',
                      args=("NEARUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21_15', minute=minute_15, second='20',
                      args=("ETHUSDT", 27, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM25_15', minute=minute_15, second='20',
                      args=("ZENUSDT", 27, 75.5, 5, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_15', minute=minute_15, second='21',
                      args=("AXSUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_15', minute=minute_15, second='21',
                      args=("WAVESUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_15', minute=minute_15, second='21',
                      args=("HNTUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_15', minute=minute_15, second='21',
                      args=("DYDXUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_15', minute=minute_15, second='21',
                      args=("ALICEUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_15', minute=minute_15, second='21',
                      args=("SNXUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_10_15', minute=minute_15, second='21',
                      args=("QTUMUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_15', minute=minute_15, second='22',
                      args=("RAYUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_15', minute=minute_15, second='22',
                      args=("SUSHIUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_15', minute=minute_15, second='22',
                      args=("OMGUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_15', minute=minute_15, second='22',
                      args=("UNFIUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_15', minute=minute_15, second='22',
                      args=("GTCUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_18_15', minute=minute_15, second='22',
                      args=("RUNEUSDT", 27, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_19_15', minute=minute_15, second='22',
                      args=("BANDUSDT", 28, 75.5, 10, 10, '15m',))  # 15min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_15', minute=minute_15, second='22',
                      args=("XTZUSDT", 27, 75.5, 10, 10, '15m',))  # 15min

    #############################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2_30', minute=minute_30, second='23',
                      args=("KSMUSDT", 26, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_30', minute=minute_30, second='23',
                      args=("UNIUSDT", 28, 75.5, 5, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4_30', minute=minute_30, second='23',
                      args=("EGLDUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5_30', minute=minute_30, second='23',
                      args=("DOTUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_30', minute=minute_30, second='23',
                      args=("LUNAUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11_30', minute=minute_30, second='23',
                      args=("ATOMUSDT", 28, 75.5, 5, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13_30', minute=minute_30, second='23',
                      args=("SOLUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14_30', minute=minute_30, second='23',
                      args=("MKRUSDT", 27, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_30', minute=minute_30, second='24',
                      args=("XMRUSDT", 28, 75.5, 5, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM17_30', minute=minute_30, second='24',
                      args=("AVAXUSDT", 27, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM18_30', minute=minute_30, second='24',
                      args=("NEARUSDT", 27, 75.5, 10, 10, '30m',))  # 30min

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20_30', minute=minute_30, second='24',
                      args=("YFIUSDT", 27, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21_30', minute=minute_30, second='24',
                      args=("ETHUSDT", 27, 75.5, 5, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24_30', minute=minute_30, second='24',
                      args=("ZECUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_30', minute=minute_30, second='24',
                      args=("AXSUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_30', minute=minute_30, second='25',
                      args=("WAVESUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_30', minute=minute_30, second='25',
                      args=("LINKUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_30', minute=minute_30, second='25',
                      args=("HNTUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_7_30', minute=minute_30, second='25',
                      args=("DYDXUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_30', minute=minute_30, second='25',
                      args=("ALICEUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_30', minute=minute_30, second='25',
                      args=("SNXUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_11_30', minute=minute_30, second='25',
                      args=("RAYUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_30', minute=minute_30, second='25',
                      args=("SUSHIUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_30', minute=minute_30, second='26',
                      args=("UNFIUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_30', minute=minute_30, second='26',
                      args=("SRMUSDT", 28, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_30', minute=minute_30, second='26',
                      args=("XTZUSDT", 27, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_30', minute=minute_30, second='26',
                      args=("THETAUSDT", 24, 75.5, 10, 10, '30m',))  # 30min
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_30', minute=minute_30, second='26',
                      args=("KAVAUSDT", 26, 75.5, 10, 10, '30m',))  # 30min


    #############################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM2_60', minute='0', second='26',
                      args=("KSMUSDT", 26, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_60', minute='0', second='26',
                      args=("UNIUSDT", 28, 75.5, 5, 10, '1h',))  # 1H
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM4_60', minute='0', second='27',
                      args=("EGLDUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM5_60', minute='0', second='27',
                      args=("DOTUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_60', minute='0', second='27',
                      args=("LUNAUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8_60', minute='0', second='27',
                      args=("TRBUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM9_60', minute='0', second='27',
                      args=("NEOUSDT", 28, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM10_60', minute='0', second='27',
                      args=("COMPUSDT", 28, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11_60', minute='0', second='27',
                      args=("ATOMUSDT", 28, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM13_60', minute='0', second='28',
                      args=("SOLUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14_60', minute='0', second='28',
                      args=("YFIIUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_60', minute='0', second='28',
                      args=("XMRUSDT", 28, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM17_60', minute='0', second='28',
                      args=("AVAXUSDT", 27, 75.5, 10, 10, '1h',))  # 1h

    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM21_60', minute='0', second='28',
                      args=("ETHUSDT", 27, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23_60', minute='0', second='28',
                      args=("DASHUSDT", 27, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM25_60', minute='0', second='29',
                      args=("ZENUSDT", 27, 75.5, 5, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_60', minute='0', second='29',
                      args=("AXSUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_2_60', minute='0', second='29',
                      args=("ICPUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_60', minute='0', second='29',
                      args=("WAVESUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_60', minute='0', second='29',
                      args=("LINKUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_60', minute='0', second='29',
                      args=("BALUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_60', minute='0', second='29',
                      args=("SNXUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_12_60', minute='0', second='30',
                      args=("SUSHIUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_13_60', minute='0', second='30',
                      args=("OMGUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_15_60', minute='0', second='30',
                      args=("UNFIUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_16_60', minute='0', second='30',
                      args=("SRMUSDT", 28, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_60', minute='0', second='30',
                      args=("XTZUSDT", 27, 75.5, 10, 10, '1h',))  # 1h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_60', minute='0', second='30',
                      args=("KAVAUSDT", 27.5, 75.5, 10, 10, '1h',))  # 1hour

    ##############################################################
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM1_61',  hour=hour_2, minute='0',
                      second='30', args=("AAVEUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM3_61', hour=hour_2, minute='0',
                      second='31', args=("UNIUSDT", 28, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM6_61', hour=hour_2, minute='0',
                      second='31', args=("BCHUSDT", 28, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM7_61', hour=hour_2, minute='0',
                      second='31', args=("LUNAUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM8_61', hour=hour_2, minute='0',
                      second='31', args=("TRBUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM11_61', hour=hour_2, minute='0',
                      second='31', args=("ATOMUSDT", 28, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM12_61', hour=hour_2, minute='0',
                      second='31', args=("BNBUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM14_61', hour=hour_2, minute='0',
                      second='31', args=("MKRUSDT", 27, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM16_61', hour=hour_2, minute='0',
                      second='31', args=("XMRUSDT", 28, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM20_61', hour=hour_2, minute='0',
                      second='32', args=("YFIUSDT", 27, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM22_61', hour=hour_2, minute='0',
                      second='32', args=("LTCUSDT", 27, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM23_61', hour=hour_2, minute='0',
                      second='32', args=("DASHUSDT", 27, 75.5, 5, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunMRM24_61', hour=hour_2, minute='0',
                      second='32', args=("ZECUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_1_61', hour=hour_2, minute='0',
                      second='32', args=("AXSUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_3_61', hour=hour_2, minute='0',
                      second='32', args=("WAVESUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_4_61', hour=hour_2, minute='0',
                      second='33', args=("LINKUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_5_61', hour=hour_2, minute='0',
                      second='33', args=("BALUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_6_61', hour=hour_2, minute='0',
                      second='33', args=("HNTUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_8_61', hour=hour_2, minute='0',
                      second='33', args=("ALICEUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_9_61', hour=hour_2, minute='0',
                      second='33', args=("SNXUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_17_61', hour=hour_2, minute='0',
                      second='33', args=("GTCUSDT", 28, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_20_61', hour=hour_2, minute='0',
                      second='33', args=("XTZUSDT", 27, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_21_61', hour=hour_2, minute='0',
                      second='28', args=("THETAUSDT", 24, 75.5, 10, 10, '2h',))  # 2h
    scheduler.add_job(RunTrade.get_kline_data, trigger='cron', id='TradeRunS1_22_61', hour=hour_2, minute='0',
                      second='29', args=("KAVAUSDT", 27.5, 75.5, 10, 10, '2h',))  # 2hour

    scheduler.add_job(RunTrade.get_position, trigger='cron', id='TradeRunGMRMp', second='*/10')
    scheduler.start()
