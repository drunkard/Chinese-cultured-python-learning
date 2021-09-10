# 函数


# 通过条件判断决定调用哪个函数
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 5, 10
print((add if b > a else subtract)(a,b))

[add, subtract][1](a, b)


# 参数
from inspect import signature
def f(a, b, c=2, *args, **kwargs):
    print(f'a={a} b={b} c={c} args={args} kwargs={kwargs}')

f(1, 2, 3, 4, 5, width=200, height=100)
f(1, 2, 3, 4, c='AAA', width=200, height=100)  # 会出错
f(1, 2, c=3, width=200, height=100)
f(1, 2)

for k,v in signature(f).parameters.items():
    print(k, v.kind)  # 查看函数的参数类型
'''结果：
a POSITIONAL_OR_KEYWORD
b POSITIONAL_OR_KEYWORD
c POSITIONAL_OR_KEYWORD
args VAR_POSITIONAL
kwargs VAR_KEYWORD
'''

# 只允许关键字参数：第一个参数设置为 *
'''
def f(*, a, b, c=2, *args, **kwargs):  # 语法错误，因为第一个参数是*，表示只允许位置参数，后面却有 *args
    print(f'a={a} b={b} c={c} args={args} kwargs={kwargs}')
'''
def f(*, a, b, c=2, **kwargs):
    print(f'a={a} b={b} c={c} kwargs={kwargs}')
f(1, 2, 3, 4)  # 会报错，因为此时函数不接受位置参数
    # TypeError: f() takes 0 positional arguments but 4 were given
f(a=1, b=2, x=3, y=4)

for k,v in signature(f).parameters.items():
    print(k, v.kind)  # 查看函数的参数类型
'''结果：
a KEYWORD_ONLY
b KEYWORD_ONLY
c KEYWORD_ONLY
kwargs VAR_KEYWORD
'''


# lambda
def max_len(*lists):
    return max(*lists, key=lambda v: len(v))
max_len([1, 2, 3], [4, 5, 6, 7], [8])



# 容易出错的地方：
"""
python中一切都是对象，函数也不列外，默认参数只是函数的一个属性。而默认参数在函数定义的时候已经求值了。

Default parameter values are evaluated when the function definition is executed.
默认参数是在定义的时候求值，而不是调用的时候。

解决方法：
A way around this is to use None as the default, and explicitly test for it in the body of the function.
"""
# eg1
'''
>>> def f(lst = []):
...     lst.append(1)
...     return lst
...
>>> f()
[1]
>>> f()
[1, 1]
'''
# eg2:
'''
>>> import time
>>> def report(when=time.time()):
...     return when
...
>>> report()
1500113234.487932
>>> report()
1500113234.487932
'''
