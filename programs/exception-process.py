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

# 异常继承关系，抓不到就找他家长
