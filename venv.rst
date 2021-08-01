venv 虚拟环境配置
=================
深度Linux默认没有安装venv，我们手动安装一下 ::

        sudo apt install python3-venv python3-tk
        
        # 新开一个虚拟环境
        python3 -m venv venv37
        ls  # 当前目录下应该多了一个 venv37
        cd venv37  # 进入这个目录
        . bin/activate  # 执行完之后，shell 提示符前面多了个 (ve) ，就说明安装没问题； 就是 PS1 变了

用国外源站很慢，我们改用国内的，清华大学镜像 ::

        mkdir -p ~/.pip/  # 创建配置文件目录
        vi ~/.pip/pip.conf  # 打开配置文件

        # 把下面2行写入刚才打开的文件
        [global]
        index-url = https://pypi.tuna.tsinghua.edu.cn/simple

再次确认：检查 python 、 pip 版本，看看是否为 python 3 ::

        $ pip --version
        pip 21.2 from /cc/lib/python3.9/site-packages/pip (python 3.9)

        $ python3 --version
        Python 3.9.6

都是基于 python 3 的，没问题我们就可以继续前行了。


探索几个 python 库
------------------

请安装这几个库： wheel 、 qrcode 、 tushare 、 zhconv ，了解其功能，并试着用一下。
在 shell 终端内执行 ::

        pip install ipython wheel qrcode tushare zhconv  # 安装
        pip show qrcode  # 看看这个库的简介
        pip show tushare

有些库会安装一个可执行文件到 bin/ 目录下，通常可以调用它最常用的功能。但是也可以在 Python 程序里直接调用。

比如， qrcode 就有一个，可以直接执行它，生成二维码 ::

        ./bin/qr 'hello python'
        █████████████████████████████
        █████████████████████████████
        ████ ▄▄▄▄▄ ██▀▀▄ █ ▄▄▄▄▄ ████
        ████ █   █ █ ▀▄▄▀█ █   █ ████
        ████ █▄▄▄█ █  ▀▄ █ █▄▄▄█ ████
        ████▄▄▄▄▄▄▄█ █ ▀ █▄▄▄▄▄▄▄████
        ████ █▄  ▄▄▀██▀█ █ ▄   █▀████
        █████▀▄▄█▄▄▄  ▄▄█ █▀█  ▄█████
        █████▄▄█▄█▄█ ▀█▄▀ ▄▄▀▀██ ████
        ████ ▄▄▄▄▄ █▀▄ █▄▀█▀█▀ ▄█████
        ████ █   █ █ ▀▀▄██  ▀▀█▄▄████
        ████ █▄▄▄█ █▄▀█ ▄▀█▄▀▀ ██████
        ████▄▄▄▄▄▄▄█▄█▄▄██▄█▄██▄█████
        █████████████████████████████
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

但是 tushare 就没有，我们只能在 python 里调用它，比如：

.. code-block:: python
    (ve) 14:16:53 /tmp/ve $ python
    Python 3.9.6 (default, Jul 25 2021, 11:21:03)
    [GCC 11.1.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import tushare
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/tmp/ve/lib/python3.9/site-packages/tushare/__init__.py", line 11, in <module>
        from tushare.stock.trading import (get_hist_data, get_tick_data,
      File "/tmp/ve/lib/python3.9/site-packages/tushare/stock/trading.py", line 15, in <module>
        import pandas as pd
    ModuleNotFoundError: No module named 'pandas'
    >>> import tushare
    >>> dir(tushare)
    ['MailMerge', 'TraderAPI', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'bar', 'bdi', 'broker_tops', 'cap_tops', 'close_apis', 'codecs', 'coins', 'coins_bar', 'coins_snapshot', 'coins_tick', 'coins_trade', 'day_boxoffice', 'day_cinema', 'forecast_data', 'fund', 'fund_holdings', 'futures', 'get_apis', 'get_area_classified', 'get_balance_sheet', 'get_cash_flow', 'get_cashflow_data', 'get_cffex_daily', 'get_concept_classified', 'get_cpi', 'get_czce_daily', 'get_day_all', 'get_dce_daily', 'get_debtpaying_data', 'get_deposit_rate', 'get_fund_info', 'get_future_daily', 'get_gdp_contrib', 'get_gdp_for', 'get_gdp_pull', 'get_gdp_quarter', 'get_gdp_year', 'get_gem_classified', 'get_gold_and_foreign_reserves', 'get_growth_data', 'get_h_data', 'get_hist_data', 'get_hists', 'get_hs300s', 'get_index', 'get_industry_classified', 'get_instrument', 'get_intlfuture', 'get_k_data', 'get_latest_news', 'get_loan_rate', 'get_markets', 'get_money_supply', 'get_money_supply_bal', 'get_nav_close', 'get_nav_grading', 'get_nav_history', 'get_nav_open', 'get_notices', 'get_operation_data', 'get_ppi', 'get_profit_data', 'get_profit_statement', 'get_realtime_quotes', 'get_report_data', 'get_rrr', 'get_shfe_daily', 'get_shfe_vwap', 'get_sina_dd', 'get_sme_classified', 'get_st_classified', 'get_stock_basics', 'get_suspended', 'get_sz50s', 'get_terminated', 'get_tick_data', 'get_today_all', 'get_today_ticks', 'get_token', 'get_zz500s', 'global_realtime', 'guba_sina', 'inst_detail', 'inst_tops', 'internet', 'is_holiday', 'latest_content', 'lpr_data', 'lpr_ma_data', 'margin_detail', 'margin_offset', 'margin_target', 'margin_zsl', 'moneyflow_hsgt', 'month_boxoffice', 'new_cbonds', 'new_stocks', 'notice_content', 'os', 'pledged_detail', 'pro', 'pro_api', 'pro_bar', 'profit_data', 'profit_divis', 'quotes', 'realtime_boxoffice', 'reset_instrument', 'set_token', 'sh_margin_details', 'sh_margins', 'shibor_data', 'shibor_ma_data', 'shibor_quote_data', 'stock_issuance', 'stock_pledged', 'subs', 'sz_margin_details', 'sz_margins', 'tick', 'top10_holders', 'top_list', 'trade_cal', 'trader', 'util', 'xsg_data']
    >>> tushare.global_realtime()
          symbol                name        price      chga      chgp             datetime
    0   sh000001                上证指数    3397.3574  -14.3666 -0.421095  2021-07-30 15:02:28
    1      hkHSI                恒生指数    25935.580  -379.740    -1.443  2021-07-30 16:05:00
    2        UKX             英国富时100    7034.8000    -43.62     -0.62  2021-07-30 04:00:00
    3        DAX             德国DAX30   15545.6000    -94.87     -0.61  2021-07-30 04:00:00
    4    INDEXCF            俄罗斯MICEX    3771.5800    -32.75     -0.86  2021-07-30 15:50:00
    [...]

其他功能自己查文档试试。


我们再试试另外一个数据源库 akshare ，先安装 ``pip install akshare`` 。

.. code-block:: python
    >>> import akshare as ak
    # 筛选一下和黄金有关的
    >>> [x for x in dir(ak) if 'gold' in x]
    ['macro_china_foreign_exchange_gold', 'macro_china_fx_gold', 'macro_cons_gold_amount', 'macro_cons_gold_change', 'macro_cons_gold_volume']
    >>> ak.macro_china_fx_gold()  # 随便试一个
                 月份   国家外汇储备-数值    国家外汇储备-同比    国家外汇储备-环比 黄金储备-数值 黄金储备-同比 黄金储备-环比
    0    2021-06-01     32140.1   3.26707211  -0.24188319                        
    1    2021-05-01    32218.03   3.87243479   0.73863885    6264       0       0
    2    2021-04-01     31981.8   3.45212406   0.88803604    6264       0       0
    3    2021-03-01    31700.29   3.57429329  -1.09095368    6264       0       0
    4    2021-02-01    32049.94   3.16333829  -0.17681662    6264       0       0
    ..          ...         ...          ...          ...     ...     ...     ...
    157  2008-05-01  17969.6074  39.01145518   2.29445149    1929       0       0
    158  2008-04-01  17566.5514  40.91959398   4.42748534    1929       0       0
    159  2008-03-01    16821.77  39.94455701   2.12753159    1929       0       0
    160  2008-02-01  16471.3371  42.31667678   3.60566958    1929       0       0
    161  2008-01-01   15898.104  43.91438669   4.02822351    1929       0       0

    [162 rows x 7 columns]
    # 再看看与 GDP 有关的
    >>> [x for x in dir(ak) if 'gdp' in x]
    ['macro_canada_gdp_monthly', 'macro_china_gdp', 'macro_china_gdp_yearly', 'macro_euro_gdp_yoy', 'macro_germany_gdp', 'macro_swiss_gdp_quarterly', 'macro_uk_gdp_quarterly', 'macro_uk_gdp_yearly', 'macro_usa_gdp_monthly', 'qhkc_tool_gdp']
    >>> ak.macro_china_gdp()  # 看看中国的 GDP
              季度  国内生产总值-绝对值  国内生产总值-同比增长  第一产业-绝对值  第一产业-同比增长  第二产业-绝对值  第二产业-同比增长  第三产业-绝对值  第三产业-同比增长
    0   2021-06-01    532167.0         12.7   28401.0        7.8  207154.0       14.8  296611.0       11.8
    1   2021-03-01    249310.0         18.3   11332.0        8.1   92623.0       24.4  145355.0       15.6
    2   2020-12-01   1015986.2          2.3   77754.1        3.0  384255.3        2.6  553976.8        2.1
    3   2020-09-01    719688.4          0.7   48123.9        2.3  270315.4        0.9  401249.1        0.4
    4   2020-06-01    454712.1         -1.6   26051.9        0.9  170232.8       -1.9  258427.4       -1.6
    ..         ...         ...          ...       ...        ...       ...        ...       ...        ...
    57  2007-03-01     57159.3         13.8    3473.0        4.1   25983.1       14.8   27703.2       14.1
    58  2006-12-01    219438.5         12.7   23317.0        4.8  104359.2       13.5   91762.2       14.1
    59  2006-09-01    155816.8         12.8   14700.4        4.7   73929.5       13.7   67187.0       13.7
    60  2006-06-01     99752.2         13.1    7762.7        4.8   46992.9       14.2   44996.5       13.6
    61  2006-03-01     47078.9         12.5    3012.7        4.4   21418.2       13.1   22648.0       13.1

    [62 rows x 9 columns]

    >>> ak.movie_boxoffice_weekly()
       排序      影片名称  排名变化   单周票房 环比变化    累计票房  平均票价  场均人次  口碑指数  上映天数
    0   1    我和我的家乡  9999  30969  -71  246166    38    11   NaN    18
    1   2     一点就到家     2   8059  -35   23280    37     8  7.36    15
    2   3       姜子牙    -1   7798  -81  153567    38     6  6.79    18
    3   4        夺冠    -1   7434  -65   76960    37     7  7.39    24
    4   5        喜宝     0   5122    0    5123    36    10  5.90     3
    5   6       急先锋    -1   2755  -56   26815    37     5  6.49    19
    6   7       天道王     0   2263    0    2263    31    27   NaN     4
    7   8    七号房的礼物     0   1091    0    1174    33     6  7.63     4
    8   9        八佰    -3   1072  -48  309432    38     7  7.70    59
    9  10  2019阅兵盛典    -3    552  -57    2830    35    11   NaN    18

其余功能自己研究一下，文档在 https://www.akshare.xyz/zh_CN/latest/tutorial.html


pip 其他常用功能
----------------
以下命令都是在激活 venv 的情况下执行的 ::

        pip install -U zhconv   # 升级
        pip uninstall zhconv    # 卸载
        pip list                # 罗列已安装的库
        pip freeze              # 冻结当前环境，也就是生成一份python库列表，拿着这份列表就可以在别处部署出完全一样的环境

        pip search <keyword>    # 按关键词搜索
        pip search debug        # 实例，搜索与调试（即 debug ）相关的库

        pip install -h          # install 子命令说明书
        pip install -r requirement.txt  # 安装 requirement.txt 文件内的库
        pip freeze > requirement.txt    # 生成一份 requirement.txt 文件，可以当作备份
