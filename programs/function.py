'''
函数
'''

# define function
def func(arg1, arg2, kwarg1=None, kwarg2=2, *args, **kwargs):
    """函数实例

    这里放置函数的文档，至少应该说明函数的用途、参数的含义和类型、用法实例；

    这里的内容可以通过 func.__doc__ 或 help(func) 看到。

    arg1, arg2:
        位置参数，定义的参数位置是什么样，调用时也必须用同样的顺序指定参数；
        没有默认值，调用时必须指定参数；
        可以定义任意多个；

    kwargs1, kwargs2:
        关键字参数，类似字典：一个名字对应一个值；
        调用它时，如果不写前面的 kwarg1= 那就按位置确定对应关系，最好指定名字；如果这个函数还定义了 *args 就不能这样用，否则就被当成 *args 了；
        可以定义任意多个；

    *args:
        位置参数，数量不确定；
        函数内部看到的是个元组；

    **kwargs:
        关键字参数，数量不确定，内容不确定；
        函数内部看到的是个字典；

    def 函数名(参数列表):
        //实现特定功能的多行代码
        [return [返回值]]
    """
    pass  # TODO not implemented

    return 1 > 2

def aa():
    a = dict(a='a')
    b = 'asd'
    return a or b
    # return a if a else b


def big_number(a, b):
    '返回较大的数字'
    if a > b:
        return a
    else:
        return b
    # return a if a > b else b


def sort(a, b):
    '排序'
    return a, b if a < b else b, a


def swap(a, b):
    return b, a


def max_as_digit(*args):
    '''返回最大值，不是数字的转成数字比较'''
    # print(type(args), args)  # debug
    new = {}
    # 数据清洗。。。
    for n in args:
        if type(n) == int or type(n) == float:
            new[n] = n
        elif type(n) == str:
            ns = [ord(nc) for nc in n]
            new[sum(ns)] = n
        else:
            print(F'未知数据类型 {n}')
    return new.get(max(new.keys()))


# Write a program to generate a dictionary that contains (n,n*n) as
# key-value pairs from keys ranging from 0 to m.
def gen_sqrt(m):
    "返回字典， n: n*n"
    '''
    d = dict()
    for n in range(m):
        d[n] = n * n
    return d
    '''
    return {n: n*n for n in range(m)}


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



if __name__ == '__main__':
    # print(sqrt(21))
    # val = gen_sqrt(21)
    # print(val)

    # v = aa()
    # print(v)

    # print(big_number(2, 33))

    m = max_as_digit(1.2, 2, 'a', '汉', 'w', 'word', '道德经', 'help me on coding')
    print(m)
