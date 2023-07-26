# 捕获异常
try:
    exec('''
if 1:
    print('ok')
''')
except NameError as e:
    # print(dir(e))
    # print(e.with_traceback())
    print(e)
    print('I got it')
else:
    print('该干嘛干嘛')


try:
    exec('print("a")')
except NameError:
    print('哦，知道了')
except SyntaxError as e:
    print(e)
else:
    print('else')
finally:
    print('finally')

# 异常继承关系，抓不到就找他家长
