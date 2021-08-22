'''装饰器
'''

"""
# 装饰器，完整格式
def outer(func):
    def inner():
        print('执行前，做些小动作')
        func()
        print('执行完了')
    return inner

@outer
def ff():
    print('被装饰的函数')

# outer()(ff())
ff()
"""

# 实例 - 用于调试
def debug(func):
    def wrapper():
        print('DEBUG: enter {}()'.format(func.__name__))
        return func()
    return wrapper

@debug
def worker():
    print('this is worker function, work done when you see this')

# worker()


# 实例 - 用于结果修饰
def to_money(func, *args):
    """把输入的数字转成人民币，浮点数四舍五入为2个小数"""
    def wrapper(*args):
        v = func(*args)
        v = round(v, ndigits=2)
        return '{} 元'.format(str(v))
    return wrapper

@to_money
def money(n):
    # print('money', n)
    return n * 0.802  # 扣税

print(money(12345.23))


# 作业 - 写个装饰器，实现认证功能；输入的密码正确才能执行程序，否则不执行
# 扩展功能：通过认证后其余函数都不再认证；不再使用后一段时间就重置认证状态；


# 作业：学会使用缓存装饰器
# from functools import lru_cache
