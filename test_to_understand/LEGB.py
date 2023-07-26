# 作用域 - 变量能产生作用的范围，或者说，使用的变量到底出自哪里

# local和enclosing是相对的，enclosing变量相对上层来说也是local;

'''先整体认识一下
x = int(2.9)  # built-in
v = 999  # global

def f1():
    v = 2  # enclosing
    def f2():
        # global v
        v = 3  # local
        print('f2:', v)

    f2()
    v = 6
    print(v)
    # v = 6

print('main block:', v)
'''


# 只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如if、try、for等）是不会引入新的作用域的

# 没有引进新的作用域
if 2 > 1:
    x = 1
print(x)


# def、class、lambda是可以引入新作用域的
# 新的函数引入了新的作用域，函数内的变量不为外面所知
'''
def f3():
    xx = 2
print(xx)
'''


''' 会出错：
y = 66
def f4():
    print(y)
    y = 7
f4()

# 出错原因和上面的类似
y = 66
def f5():
    y += 1
f5()
'''


"""
global 关键字

当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了，
当修改的变量是在全局作用域（global作用域）上的，就要使用global先声明一下:
    要修改的变量属于全局作用域
"""
'''
count = 10
def f6():
    global count
    print(count)
    count = 100
    print(count)
f6()

def f6():  # 与前一个函数类似
    global count
    print(count)
    count += 100
    print(count)
f6()
'''


# global关键字声明的变量必须在全局作用域上，不能嵌套作用域上，
# 当要修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量就需要nonlocal关键字了
def outer():
    c = 22
    def inner():
        nonlocal c
        c = 3
        print(c)
    inner()
    print(c)
outer()


if __name__ == '__main__':
    pass
    # f1()
    # print(globals())
