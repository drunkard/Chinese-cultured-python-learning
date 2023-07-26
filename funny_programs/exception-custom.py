# 类和函数命名惯例
def funny_exception(arg):
    pass

class FunnyException(Exception):
    '没什么错误，就逗逗你'

class BigFunnyError(FunnyException):
    'Holla'

# raise FunnyException('自定义原因')
raise FunnyException(FunnyException.__doc__)
