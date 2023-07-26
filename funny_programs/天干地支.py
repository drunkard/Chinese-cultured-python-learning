#!/cc/bin/python

def _gzs():
    gzs = []  # 生成的干支
    for i in range(1, 61):
        tg_cursor = i % 10 - 1
        dz_cursor = i % 12 - 1
        gzs.append([tgs[tg_cursor], dzs[dz_cursor]])
    return gzs


def _gzs_table(tgs, dzs, gzs):
    table = {}  # 干支: 打印位置
    for gz in gzs:
        tidx = tgs.index(gz[0])
        didx = dzs.index(gz[1])
        table[''.join(gz)] = [tidx + 1, didx + 1]
    return table


def print_gz_table(tgs, dzs, gzs):
    table = _gzs_table(tgs, dzs, gzs)  # 干支: 打印位置
    print(' '*4 + '  '.join(tgs))  # 表头
    for dz in dzs:
        line = f'{dz} '
        for tg in tgs:
            gz = tg + dz
            line += gz if table.get(gz) else ' '*4
        print(line)


tgs = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
dzs = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

gzs = _gzs()
gzs2 = [''.join(gz) for gz in gzs]
gzs_table = _gzs_table(tgs, dzs, gzs)

if __name__ == '__main__':
    print(gzs)
    print(gzs2)
    print_gz_table(tgs, dzs, gzs)
