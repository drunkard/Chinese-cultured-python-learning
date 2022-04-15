#!/cc/bin/python3
import matplotlib.pyplot as plt
import pandas as pd
import re


_cs = '美国、欧盟成员国（全部27国）、乌克兰、英国、日本、澳大利亚、新西兰、加拿大、韩国、新加坡、瑞士、黑山、阿尔巴尼亚、挪威、冰岛、列支敦士登、安道尔、摩纳哥、北马其顿、圣马力诺、密克罗尼西亚、中国台湾地区'.split('、')
eu27 = '奥地利、比利时、保加利亚、塞浦路斯、克罗地亚、捷克共和国、丹麦、爱沙尼亚、芬兰、法国、德国、希腊、匈牙利、爱尔兰、意大利、拉脱维亚、立陶宛、卢森堡、马耳他、荷兰、波兰、葡萄牙、罗马尼亚、斯洛伐克、斯洛文尼亚、西班牙、瑞典'.split('、')
c48 = _cs + eu27
c48.remove('欧盟成员国（全部27国）')
# print(len(c48), c48)

def to_raw_num(x):
    if isinstance(x, (int, float)):
        return x
    if x.isdigit():
        return int(x)
    r = r = r"(?<=\()(.*)(?=\))"
    n = re.findall(r, x)[-1]
    n = n.replace(',', '')
    if not n.isdigit():
        print(f'bad data: {n}')
        n = 0
    return int(n)


def area():
    '''result like:

          排名  国家/地区  所在洲    年份  国土面积(平方公里)     占世界比重
    1      1    俄罗斯   欧洲  2018    17098250  12.7084%
    2      2    加拿大   美洲  2018     9879750   7.3432%
    3      3     美国   美洲  2018     9831510   7.3074%
    4      4     中国   亚洲  2018     9600012   7.1353%
    ..   ...    ...  ...   ...         ...       ...
    217  213     瑙鲁  大洋洲  2018          20   0.0000%
    218  214   直布罗陀   欧洲  2018          10   0.0000%
    '''
    # 国土面积
    url = 'https://www.kylc.com/stats/global/yearly_overview/g_area_surface.html'
    d = pd.read_html(url)[0]

    fixcol = '国土面积(平方公里)'
    d[fixcol] = d[fixcol].apply(to_raw_num)
    d.drop(index=0, inplace=True)
    d.drop(columns=["排名", "所在洲", "年份", "占世界比重"], inplace=True)
    # print(d)
    return d


def population():
    '''data like:
           排名    国家/地区 年份  人口      占世界比例(%)  儿童(%)  老年人(%)
    0      NaN      全世界  2020  7752840000       NaN    NaN     NaN
    1      1.0       中国  2020  1402110000   18.0851  17.71   11.97
    2      2.0       印度  2020  1380000000   17.8000  26.16    6.57
    3      NaN       欧盟  2020   447795000    5.7759    NaN     NaN
    4      3.0       美国  2020   329484000    4.2499  18.37   16.63
    ..     ...      ...   ...         ...       ...    ...     ...
    215  214.0      图瓦卢  2020       11792    0.0002    NaN     NaN
    216  215.0       瑙鲁  2020       10834    0.0001    NaN     NaN
    '''
    # 人口
    url = 'https://population.gotohui.com/word'
    d = pd.read_html(url)[0]

    # TODO drop ['全世界', '欧盟']
    d.drop(index=0, inplace=True)
    d.drop(columns=["排名", "年份", "占世界比例(%)", '儿童(%)', '老年人(%)'], inplace=True)
    # print(d)
    return d


def gdp():
    '''data like:
            排名  国家/地区    年份         GDP(美元)  2020年占世界比例(%)
    0      NaN    全世界  2020  84705400000000       100.0000
    1      1.0     美国  2021  22993500000000        24.7170
    2      2.0     中国  2021  17727200000000        17.3811
    3      NaN     欧盟  2020  15192700000000        17.9359
    4      3.0     日本  2021   4934720000000         5.9728
    ..     ...    ...   ...             ...            ...
    205  204.0     瑙鲁  2019       118223000         0.0001
    206  205.0    图瓦卢  2020        48855600         0.0001
    '''
    # GDP
    d = pd.read_html('https://gdp.gotohui.com/word')
    d = d[0]
    fixcol = 'GDP(美元)'
    d[fixcol] = d[fixcol].apply(to_raw_num)
    # TODO drop ['全世界', '欧盟']
    d.drop(index=0, inplace=True)
    d.drop(columns=["排名", "年份", '2020年占世界比例(%)'], inplace=True)
    # print(d)
    return d


def compared_data(name, df, filter_col, data_col):
    '过滤出48国的数据，和所有其他国家的进行比较'
    df48 = df[df[filter_col].isin(c48)]
    dfo = df[~df[filter_col].isin(c48)]  # others
    dfo_sum = pd.DataFrame(
        [{filter_col: '其余国家', data_col: dfo.agg({data_col: sum}).values[0]}]
    )
    new_df = pd.concat([df48, dfo_sum])
    new_df.set_index(filter_col, inplace=True)
    return new_df


def plot(name, y, df):
    # 绘图，饼图
    # 设置 可视化风格
    plt.style.use('tableau-colorblind10')

    # 以下代码从全局设置字体为SimHei（黑体），解决显示中文问题
    plt.rcParams['font.sans-serif'] = ['STXihei']
    plt.rcParams["font.family"] = "sans-serif"

    # 解决中文字体下坐标轴负数的负号显示问题
    plt.rcParams['axes.unicode_minus'] = False

    # 全局设置图尺寸，英寸
    plt.rcParams['figure.figsize'] = (14, 14)

    plt.rcParams['text.color'] = '#1874CD'

    dfp = df.plot.pie(
        y=y,
        fontsize=24,
        rotatelabels=45,
        # radius=0.8,
        legend=False,
        ylabel='',  # hide figure title
    )
    # plt.show()
    fig = dfp.get_figure()
    fn = f"/data/DOWNLOAD/48国_{name}.png"
    print(f'正在绘图 ... {fn}')
    fig.savefig(fn)


if __name__ == '__main__':
    print('、'.join(c48))
    plot('国土面积', '国土面积(平方公里)',
        compared_data('国土面积', area(), '国家/地区', '国土面积(平方公里)'))
    plot('人口', '人口',
        compared_data('人口', population(), '国家/地区', '人口'))
    plot('GDP', 'GDP(美元)',
        compared_data('GDP', gdp(), '国家/地区', 'GDP(美元)'))
