# 函数


# 通过条件判断决定调用哪个函数
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 5, 10
print((add if b > a else subtract)(a,b))

