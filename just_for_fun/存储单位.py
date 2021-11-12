''' 存储单位bit、byte、KB、MB、GB、TB、PB、EB、ZB、YB、BB、NB、DB、CB、XB

bit（binary digit）比特，这是表示信息的最小单位,它只能表示 0 或 1。
byte（字节），其表示的值范围是0~255(无符号) 或 -127~127(有符号)，1 byte = 8 bit，一个英文字母1字节，一个汉字需要2字节（GBK编码）。

KB（Kilobyte），1 KB = 1024 byte，大约四五百个汉字的短篇小说。
MB（Megabyte），1 MB = 1024 KB，五十万多字的内容，《西游记》82万字2 MB就存完。
GB（Gigabyte），1 GB = 1024 MB，大约5.37亿个汉字，历史上字数最多的《永乐大典》有3亿7千万字。
TB（Terabyte），1 TB = 1024 GB，约1.1万亿字节，在线看的720P电影每部大概500MB~1GB大小，可以存放1000多部。
PB（Petabyte），1 PB = 1024 TB，按上例，可以存放100万部电影，人活到100岁也不到90万小时。
EB（Exabyte），1 EB = 1024 PB，相当于52.4万个2T硬盘，一个按300元计算，需要1.57亿人民币（原谅我庸俗）。
ZB（Zettabyte），1 ZB = 1024 EB，以 50MB/秒 的速度下载，需要71.4万年。
YB（Yottabyte），1 YB = 1024 ZB，据预测到2025年全球每天产生的数据量将达到491EB，可以存2135天，也就是5年多。目前，应该全球的数据（包括视频、图片）总和加起来都没有这么多...
BB（Brontobyte），1 BB = 1024 YB = 1237940039285380274899124224 Byte
NB（NonaByte），1 NB = 1024 BB = 1267650600228229401496703205376 Byte
DB（DoggaByte），1 DB = 1024 NB，数据到达这个量级是几百年之后的事情了，这时候8K视频都只能算一般画质，消费级硬盘都是以PB为单位了。
CB（corydonbyte），1 CB = 1024 DB，人工智能已无处不在，机器人已全面供养人类，彻底代替人类劳作，并成为最大的数据生产者。
XB（Xerobyte），1 XB = 1024 CB，他们会感叹老祖宗吃饱了撑着发明这么多自己都用不到的转换，因为基于新进制的存储技术已经成熟可靠。
?B（?byte），1 ?B = 1024 XB，火星殖民地不满地球控制，强行宣布独立，双方投入太空大战，与此同时一部分人类已飞出太阳系...

以上文字来自: https://www.cnblogs.com/xiii/p/14219293.html
'''

import time
import turtle as t

units = {
    "B": "byte",
    "KB": "Kilobyte",
    "MB": "Megabyte",
    "GB": "Gigabyte",
    "TB": "Terabyte",
    "PB": "Petabyte",
    "EB": "Exabyte",
    "ZB": "Zettabyte",
    "YB": "Yottabyte",
    "BB": "Brontobyte",
    "NB": "NonaByte",
    "DB": "DoggaByte",
    "CB": "corydonbyte",
    "XB": "Xerobyte",
}


def pretty_num(n, step=8):
    ss = str(n)
    segs, mod = divmod(len(ss), step)
    newss = ''
    seg, segdone = 0, 0
    if segs == 0:
        return ss
    for s in ss:
        seg += 1
        newss += s
        if seg == mod:
            newss += '_'
            seg = 0
            mod = 0  # already done, drop it
        if seg == step:
            segdone += 1
            if segdone < segs:
                newss += '_'
            seg = 0
    return newss

def show_names():
    # 挨个演示动画
    # 大数据风行，人们经常说到的这些B单位究竟是什么意思？
    t.setup(width=1.0, height=1.0)
    t.hideturtle(); t.penup()
    t.goto(0, -300)
    t.bgcolor('black')
    t.colormode(255)
    b = 0
    for u in units.keys():
        t.clear()
        t.color(255, 255, b)
        b += 18
        t.write(u, align='center', font=('Arial', 400, 'normal'))
        time.sleep(0.3)
    time.sleep(1)

def show_numbers():
    us = list(units.keys())
    pu = ''
    for idx, u in enumerate(us):
        power = idx * 10  # 幂次
        if idx != 0:
            print('1{} = 1024{} = {} 个2相乘 = {} 字节'
                  .format(u, pu, power, pretty_num(2**power)))
        pu = u

show_names()
show_numbers()
