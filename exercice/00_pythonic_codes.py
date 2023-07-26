# 符合 Python 风格的代码，就是 pythonic 的


# 交换变量值
a, b = 1, 3
print(a, b)
a, b = b, a
print(a, b)


# 分词、组句
# ss = 'Gautham Santhosh 带我们回顾了 17 个非常有用的 Python 技巧'
ss = 'Python is elegant programming language'
slist = ss.split()
print(slist)
print('这样又组合成了一句话：',
      ' '.join(slist))


# 组合成逗号分隔的，转换成 csv 时也许能用得到
es = ['a', 'b', 'c']
','.join(es)

ns = [1, 2, 3]
','.join(ns)    # 会出错  TypeError: sequence item 0: expected str instance, int found
','.join(map(str, ns))  # 必须先转换成字符串，因为 'x'.join 是字符串的方法

mixs = [1, 'a', 2, list]
','.join(map(str, mixs))    # 混合对象列表也得先转换成字符串才能拼凑


# 列表中出现频率最高的值
a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 3]
print(max(set(a), key=a.count))
# 用 collections.Counter
from collections import Counter
cnt = Counter(a)
print(cnt.most_common())  # 结果为 (列表元素, 数量) 组成的列表
print(cnt.most_common(3))


# 检查两个字符串是不是由相同字母不同顺序组成
from collections import Counter
str1, str2 = 'dam', 'mad'
Counter(str1) == Counter(str2)


# 反转字符串
a = 'dam is a word'
print(a[::-1])

for char in reversed(a):
    print(char, end='')

n = 123456789
print(int(str(n)[::-1]))


# 反转列表
a = ['1', '2', '3', '4', '5']
print(a[::-1])

new_list = []
for element in reversed(a):
    new_list.append(element)


# 转置二维数组
a = [[1, 2], [3, 4], [5, 6]]
list(zip(*a))
# [(1, 3, 5), (2, 4, 6)]


# 链式比较
b = 6
4 < b < 7   # True, (4 < b and b < 7)
1 == b < 21     # False, (1 == b and b < 21)


# 链式函数调用
def product(a, b):
    return a * b

def add(a, b):
    return a + b

b = True
print((product if b else add)(5, 7))


# 复制列表，正确地复制很重要，否则会影响原来的列表
a = [1, 2, 3]

# 法1，不行的
b = a
b[0] = 'a'
print(a, b)
['a', 2, 3] ['a', 2, 3]     # a, b 都变了

# 法2， typecasting method
b = list(a)

# 法3
b = a.copy()

# 法4
from copy import deepcopy
b = deepcopy(a)


# 列表里最大值和最小值的索引
es = [10, 20, 5, 40]
min(range(len(es)), key=es.__getitem__)     # 最小值的索引
max(range(len(es)), key=es.__getitem__)     # 最大值的索引


# 列表去重
es = [2, 2, 4, 4, 1, 5, 2, 1]
# 法1
list(set(es))
# 法2，去重并保持顺序
from collections import OrderedDict
es = ['a', 'b', 'a', 'c', 'b']
list(OrderedDict.fromkeys(es).keys())
# 输出: ['a', 'b', 'c']


# 字典 get
d = {'a': 1, 'b': 2}
d.get('c', 3)  # 取c，如果没有，返回默认值3
d['c']  # 如果字典没有这个key，会报错


# 字典排序
d = {'apple': 10, 'pear': 20, 'orange': 21, 'tomato': 5}

# 按值排序
sorted(d.items(), key=lambda x: x[1])

# 按值排序， operator.itemgetter
from operator import itemgetter
sorted(d.items(), key=itemgetter(1))

# 按值排序, get
sorted(d, key=d.get)



# 字典合并
d1, d2 = {'a': 1}, {'b': 2}

# 法1
{**d1, **d2}

# 法2
dict(d1.items() | d2.items())

# 法3
d1.update(d2)



# else: 在 for|while|try 等很多语句之都有 else ，在遇到条件不符最后退出时执行
a = [1, 2, 3]
for e in a:
    if e == 0:
        break
else:
    print('没有执行 break ，正常完成了，所以显示')



# or 简化代码
d = {'a': 1, 'b': 2, 'c': 3}
# 常规写法
if d.get('d'):
    char = d.get('d')
else:
    char = 'd'
# python极简写法
char = d.get('d', 4)  # 仅限于字典
char = d.get('d') or 4
