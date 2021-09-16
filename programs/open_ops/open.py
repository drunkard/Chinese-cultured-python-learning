#!/usr/bin/python3
'''用法：
file_obj = open('file_name', 'r')

r - 只读
w - 写入模式
a - 追加模式
r+ - 读取+写入模式
b - bytes

# eg1, 换行？ \n
# \n = newline; \r\n = return, newline;
f = open('eg1', mode='w')
f.write('文王勤于日昃，大禹惜寸阴，周公坐待旦。\n')
f.write('为学日益，为道日损。\n')
f.write('也许我不能成功，但我一定不会放弃努力。\n')
f.close()

f = open('eg1', 'r')
print(f.read(6))
f.close()

f = open('eg1', 'rb')
print(f.read(6))
f.close()

f = open('eg1', 'r')
print(f.readlines())
# for line in f:
#     print(line, end='')
f.close()
'''

'''
with open('eg1', 'r') as f:
    with open('eg2', 'w') as f2:
        n = 1
        for line in f:
            f2.write(str(n) + line)
            n += 1
    # for line in f.readlines():
    #     print(line)
'''



'''
# 整理文件
with open('绕口令', 'r') as f:
    for line in f.readlines():
        if line == '\n':
            continue
        if line[0].isdigit():
            line = '\n' + line
        print(line, end='')
'''
