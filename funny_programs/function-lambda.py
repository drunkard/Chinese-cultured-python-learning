"""匿名函数
"""

data = [
    {"name": "wang", "age": 10},
    {"name": "xiaoming", "age": 13},
    {"name": "banzhang", "age": 20},
    {"name": "xixi", "age": 11},
]

# 对列表内的字典排序
data.sort(key=lambda x: x['name'])
data.sort(key=lambda x: x['age'])
sorted(data, key=lambda x: x['age'])

# 匿名函数另一个常用的地方就是配合 map() 函数一起使用
map(lambda x: x**2, range(11, 20))
list(map(lambda x: x**2, range(11, 20)))
# 当然， map() 不是非得用匿名函数
def f(x):
    return x * x
map(f, [1, 2, 3, 4])
map(f, (1, 2, 3, 4))

# filter 接受的函数应该返回 True/False
list(filter(lambda x: x%2 == 0, range(11, 20)))
def f(x):
    return x % 3 == 0
list(filter(f, range(11, 20)))

