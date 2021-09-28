# -*- coding: utf-8 -*-
##############################################################################
# Author：QQ173782910
##############################################################################
import redis
# 注意：
#    持仓方向为单向,不会设置杠杆
#    下边的dingding_token,wx_openid为空的话是不会发送钉钉消息和公众号消息

version_flag = '20210928'

key = ""  # 币安API的key
secret = ""  # 币安API的secret

dingding_token = ""  # 钉钉webhook的access_token
wx_openid = ""  # 关注简道斋后发送openid得到的那一串字符就是这个

tactics_flag = 0  # 此为机器人执行策略计算无信号是否发送钉钉消息，约5分钟发送一次，1为发送，不发送请留空或其他值
add_pos_flag = 0  # 加仓标识，为1开启，0关闭,加仓是当币在扛单中，再次遇到开仓信号就又开一次仓，这样会降低持仓均价，但爆仓风险更大
add_pos_amount = 0  # 加仓次数，0不限次数，其他的整数值为最大加仓次数，每个币的次数一样，不单独设置
# [币对,下单量,止盈参数,补仓参数]  补仓:是币已经止盈，当前无持仓，当币价回调到一定价格就再次开仓
symbols_conf = [["AAVEUSDT", 0.1, 1.006, 0.985],  # ok
                ["KSMUSDT", 0.3, 1.006, 0.985],  # ok
                ["UNIUSDT", 1.0, 1.006, 0.985],  # ok
                ["EGLDUSDT", 0.6, 1.01, 0.985],  # ok
                ["BNBUSDT", 0.03, 1.006, 0.985],  # ok
                ["SOLUSDT", 1, 1.01, 0.985],  # ok
                ["DOTUSDT", 0.4, 1.006, 0.985],  # ok
                ["BTCUSDT", 0.002, 1.006, 0.985],  # ok
                ["YFIUSDT", 0.002, 1.006, 0.985],  # ok
                ["ETHUSDT", 0.002, 1.006, 0.985],  # ok
                ["LTCUSDT", 0.03, 1.006, 0.985],  # ok
                ["BCHUSDT", 0.08, 1.006, 0.985],  # ok
                ["MKRUSDT", 0.005, 1.006, 0.985],  # ok
                ["DASHUSDT", 0.05, 1.006, 0.985],  # ok
                ["ZECUSDT", 0.5, 1.008, 0.985],  # ok
                ["ZENUSDT", 0.3, 1.006, 0.985],  # ok
                ["FILUSDT", 0.4, 1.006, 0.985],  # ok
                ["AVAXUSDT", 1, 1.008, 0.985],  # ok
                ["LUNAUSDT", 2, 1.006, 0.985],  # ok
                ["YFIIUSDT", 0.003, 1.006, 0.985],  # ok
                ["COMPUSDT", 0.03, 1.006, 0.985],  # ok
                ["XMRUSDT", 0.05, 1.006, 0.985],  # ok
                ["TRBUSDT", 0.5, 1.008, 0.985],  # ok
                ["NEOUSDT", 0.5, 1.008, 0.985],  # ok
                ["NEARUSDT", 4.0, 1.008, 0.985],  # ok
                ["ATOMUSDT", 0.5, 1.008, 0.985],  # ok
                ]

symbols_conf2 = [["AXSUSDT", 1, 1.006, 0.985],
                 ["ICPUSDT", 0.4, 1.006, 0.985],
                 ["WAVESUSDT", 0.4, 1.006, 0.985],
                 ["LINKUSDT", 0.4, 1.006, 0.985],
                 ["BALUSDT", 0.4, 1.006, 0.985],
                 ["HNTUSDT", 1, 1.006, 0.985],
                 ["DYDXUSDT", 0.5, 1.006, 0.985],
                 ["ALICEUSDT", 0.7, 1.006, 0.985],
                 ["SNXUSDT", 0.8, 1.006, 0.985],
                 ["QTUMUSDT", 0.7, 1.006, 0.985],
                 ["RAYUSDT", 0.6, 1.006, 0.985],
                 ["SUSHIUSDT", 2, 1.008, 0.985],
                 ["OMGUSDT", 0.7, 1.006, 0.985],
                 ["MASKUSDT", 1, 1.006, 0.985],
                 ["UNFIUSDT", 0.8, 1.006, 0.985],
                 ["SRMUSDT", 2, 1.006, 0.985],
                 ["GTCUSDT", 0.9, 1.006, 0.985],
                 ["RUNEUSDT", 2, 1.006, 0.985],
                 ["BANDUSDT", 1, 1.006, 0.985],
                 ["XTZUSDT", 0.9, 1.006, 0.985],
                 ["THETAUSDT", 2, 1.006, 0.985],
                 ["KAVAUSDT", 2, 1.006, 0.985],
                 # ["FTTUSDT", 1.0, 28, 72.5, 10, 10], 无usdt
                ]

redis_pool = redis.ConnectionPool(host='127.0.0.1', port='6379', db='0', password='')
redisc = redis.StrictRedis(connection_pool=redis_pool)