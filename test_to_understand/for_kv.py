'for 循环一次取出多个对象'
dic = {1: '石头',
       2: '剪刀',
       3: '布',
}
print(dic.items())

for k, v in dic.items():
    print(v)


a = range(5)
b = range(97, 102)
# cc = zip(a, b)
# print(cc)
# print(list(cc))
for av, bv in zip(a, b):
    print(F'{av} -- {bv}')


# 源数据必须合乎规则
for a, b in [range(5), range(6, 11)]: print(a, b)  # 会出错
for a, b in [[range(5), range(6, 11)]]: print(a, b)
for a, b, c, d in ['A', 'B', 'C', 'D']: print(a, b, c, d)  # 会出错
for a, b, c, d in [['A', 'B', 'C', 'D']]: print(a, b, c, d)
