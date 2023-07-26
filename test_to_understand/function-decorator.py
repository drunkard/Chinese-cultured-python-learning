'''装饰器
'''

# 装饰器，完整格式
def outer(func):  # 外层函数，传参数、开路的
    def inner():  # 内层函数，被装饰函数的实际执行者
        print('执行前，做些小动作')
        func()  # 执行被装饰函数，执行前、后都可以加入你想插入的功能
        print('执行完了')
        # return func()  # 也可以直接返回函数执行结果
    return inner  # 这里没有 () ，也就是说，只是返回函数，不执行

@outer  # 使用装饰器
def ff():
    print('被装饰的函数')

# outer()(ff())  # 不使用装饰器的情况下，类似此种写法
ff()  # 还是执行原来的函数，但是结果已经被装饰器处理过了

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
