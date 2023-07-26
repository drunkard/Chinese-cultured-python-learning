raise Exception
raise KeyboardInterrupt('别价，等我跑完啊')


"""
try:
    assert 2 > 3, 'data not qualified'
except AssertionError as e:
    print(e)
print('后续代码运行了')
"""


# 作业：判断运行此程序的用户是否为 root ，是的话才能运行、否则报错；
# 用到：嵌套函数、装饰器、 os.getuid()
