'''什么情况下会执行 ``else`` 这段'''

for i in range(5):
    print(i)
else:
    print('循环正常结束')


print('第二个循环 ...')
for i in range(5):
    # if i > 2:
    #     break
    if i < 2:
        continue
    print(i)
else:
    print('循环正常结束了')
