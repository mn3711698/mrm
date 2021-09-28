# mrm(支持windows+linux的多币机器人,交易所目前只支持币安)  本策略不提供永久白嫖

## 非开源，慎用! 建议一定要加群(打开http://small.yjyzj.cn 可以扫码加开发者微信或微信群)

此机器人我从2021-08-20左右开始调试，初始资金是100U，到2021-09-26(币安今天27只能看前一天26的整天收益)为止，总收益103.89971234U。采用的是复得在跑。

config.py的symbols_conf配置，币对的后一个值为每个币下单的量，如果完全按照我的量来跑，至少200U资金，并不要动手加仓，只要不是币跌去3分之2就不会爆仓。

可以修改为每个币最低下单量，资金为100U就可以跑，如果资金不够，建议少跑几个币。


# 机器人逻辑及运行说明
运行：Run.py和Start.py两个不同的脚本，跑不同的币，要注意保证金，如果同一个帐户同时跑两个脚本，帐户本金不低于300U，最好有400U。
单跑Run.py要有200U或者更多，单跑Start.py要有100U。如果在单个服务器内跑两个脚本，可能会受到交易所并发限制，我是用两个服务器在跑

开平仓：采用威科夫动量计算，判断能量值，结合两条移动条，综合得出策略开仓平仓信号。

仓位：Run.py这个的仓位会比较大，资金少的要减少仓位。Start.py这个目前我设定的是最低开仓，如果保证金够，可以适当增加仓位。

止盈：目前，在LineWith.py的28行winPrice = entryPrice * 1.01，entryPrice为持仓价，当最新价大于winPrice止盈。

止损：不存在的，浮亏就扛单，当有平仓信号时也不平仓。

止盈后再开仓:在LineWith.py的35行self.order_flag_dict[symbol] = entryPrice * 0.985，entryPrice为上一次的持仓价，
在未出来平仓信号前，如果已经止盈了，当最新价低于entryPrice * 0.985，就又开一次仓。

加仓: config.py里的add_pos_flag=1为开启加仓，add_pos_amount=0为不限制加仓次数，当add_pos_amount = 1，这个值大于0时，加仓次数等于这个值
## 以下为策略在tradingview进行的回测
btcusdt
![](https://github.com/mn3711698/mrm/blob/main/btcusdt.png)

yfiusdt
![](https://github.com/mn3711698/mrm/blob/main/yfiusdt.png)

zecusdt
![](https://github.com/mn3711698/mrm/blob/main/zecusdt.png)

## 本项目只是提供代码，不对使用者因使用本代码实际产生的盈亏负责。不要跟我说开源，我从来就没有想过要开源，只是开放使用。

## 可以自行设置计算止盈的配置参数及修改止损配置

# 注意(白嫖更要注意安全，因为核心代码没有开源，大家慎用)

## API的权限只需要有交易权限就够了，不要开提币权限,还要限制ip！

## API的权限只需要有交易权限就够了，不要开提币权限,还要限制ip！

## API的权限只需要有交易权限就够了，不要开提币权限,还要限制ip！

# 需要准备云主机，windows支持64位的python,3.8或3.7,linux系统支持python3.6

# 需要网络可以访问币安交易所，否则机器人无法使用

# TA-Lib的安装请自行百度

## windows使用说明(路径写死了)
安装redis，并启动。

TA-Lib的安装 请参数链接 https://blog.csdn.net/weixin_45544350/article/details/102873988 安装

下载本项目代码压缩包，放在C盘根目录下，解压，最终代码在C:\mrm\下。如果是git下载，也请代码放在C:\mrm\下，建议使用git下载，方便后续更新

先下载 https://download.microsoft.com/download/5/f/7/5f7acaeb-8363-451f-9425-68a90f98b238/visualcppbuildtools_full.exe
安装时，直接下一步，不需要选择其他的。

安装相关库(只支持python3)  pip3 install -r requirements.txt 或 pip install -r requirements.txt

填好config.py里边的配置项，确认python是不是64版本，如果使用的是python3.7要将strategies下的base_w37.pyd重命名为base.pyd,
如果使用的是python3.8要将strategies下的base_w38.pyd重命名为base.pyd


到此，准备工作做好。在项目目录C:\mrm\下执行python3 Run.py,就可以躺着赚钱了

相关持仓及订单信息请看币安的网页或者APP对应的交易对下的数据。

如果后续有更新代码，可以直接git下载就好了。下载好后，关掉cdm窗口，重新打开窗口执行python3 Run.py就好了

注意:持仓方向是单向(双向持仓要改为单向否则无法下单)，杠杆是交易所默认未进行另外设定

## linux使用说明(路径写死了)
安装redis，并启动。

TA-Lib的安装 请参数链接 https://blog.csdn.net/tumin999/article/details/103364555 安装

下载本项目代码压缩包，放在/var/games/目录下，解压，最终代码在/var/games/mrm/下。

如果是git下载，也请代码放在/var/games/mrm/下，建议使用git下载，方便后续更新

安装相关库(只支持python3)  pip3 install -r requirements.txt 或 pip install -r requirements.txt

填好config.py里边的配置项，确认python版本为python3.6，strategies下的base_l36.so重命名为base.so

到此所有准备工作都做好了。在项目目录/var/games/mrm/下执行python3 Run.py 或python Run.py ,就可以躺着赚钱了

相关持仓及订单信息请看币安的网页或者APP对应的交易对下的数据。

建议使用Supervisor启动

如果后续有更新代码，可以直接git下载就好了。重新执行python3 Start.py就好了

注意:持仓方向是单向(双向持仓要改为单向否则无法下单)，杠杆是交易所默认未进行另外设定

## 关于代码更新说明
建议使用git命令来下载，这样更新就不影响。

# 更新日志

2021-09-28  增加加仓开关，默认关闭

2021-09-27  增加redis缓存,让重启也能保持补仓状态值。

2021-09-24  再增加22个币

2021-09-23  优化策略计算，效率提升

2021-09-23  初始始上传


# 联系
打开http://small.yjyzj.cn 可以扫码加开发者微信或微信群

# 关于核心代码编译的说明

大家想赚钱，那只有跟着大户的车赚点小钱。那些已经实现财富自由的人，请不要使用本机器人，为散户留口汤喝。
当一个交易对某开仓的方向资金量达到一定的程度，那必然会成为大户的目标，这样再好的策略或者机器人都只能是下酒菜。
所以，我为了一个策略能使用的足够久而不需要经常去修改参数只能对部分代码进行编译。
这样首先就让一部分担心安全的人没有了使用的冲动，那会使用的人必然资金量不大或者会使用小号去跑这个机器人。
这样的结果必然是只要机器人够好，那使用者都可以跟着大户的车赚点小钱。
当然我也有点小心思，想着这个机器人足够好的话，那我完全可以基于这个策略去做量化平台或者进行收费。为了收费核心代码编译是必须的。

# 用到的链接

wss://fstream.binance.com/  币安ws
https://fapi.binance.com  币安api
https://oapi.dingtalk.com  发送钉钉webhook消息
https://link.yjyzj.cn/  我的，用来收集异常错误及发微信公众号消息，后续如果收费也会用这个进行授权

## 看到这还在担心资金安全问题，请不要使用本机器人

