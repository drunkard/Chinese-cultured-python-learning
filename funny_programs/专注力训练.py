#!/cc/bin/python
# 舒尔特表, 用来训练你的专注力
import random
import sys
import time
import turtle as t

# size*size 的方形网格
size = int(sys.argv[1]) if len(sys.argv) == 2 and sys.argv[1].isdigit() else 4
width = 900
grid_size = width / size

# 准备各方格里要填入的数字
nums = list(range(1, size**2 + 1))
random.shuffle(nums)  # 随机排列

# 用法
hi = '''这个表可以用来训练你的专注力，程序用法： {p} [网格数量]
    如： {p} {size}

从 1 开始，挨个数到 {total_size} ，按<空格键>结束计时'''\
    .format(p=sys.argv[0], size=size, total_size=size**2)
print(hi)

t.setup(width=width, height=width)
t.speed(0)
up = width / 2
x, y = up, up
for i in range(size):
    # 画横线
    t.penup()
    t.goto(-x, y - grid_size * i)
    t.pendown()
    t.seth(0)
    t.fd(width)

    # 画纵线
    t.penup()
    t.goto(-x + grid_size * i, y)
    t.pendown()
    t.seth(270)
    t.fd(width)

    # 填一行数字
    for grid in range(size):
        t.penup()
        t.goto(-x + grid_size*grid + grid_size/2, y - grid_size*i - grid_size/1.35)
        t.pendown()
        t.write(nums.pop(), align='center', font=('STFangsong', int(grid_size/3), 'bold'))
t.hideturtle()

# 计时、评级
t.penup(); t.goto(0, 0); t.pendown()
t.color('red')
t.write('开始数吧\n按<空格>键结束', align='center', font=('STFangsong', 64, 'normal'))
time.sleep(1)
t.undo()
t.undo()

def report():
    time_used = round(time.time() - start)
    a, b, c, d = ['相当厉害', '优秀', '还可以', '还需提升', ]
    if time_used < size**2 - 2:
        level = a
    elif size**2 - 2 <= time_used <= size**2 + 2:
        level = b
    elif size**2 + 2 < time_used < size**2 * 2:
        level = c
    else:
        level = d
    t.bgcolor('black')
    t.color('orange')
    t.write(F'    用时 {time_used} 秒\n专注力{level}', align='center', font=('STFangsong', 64, 'normal'))
    time.sleep(3)
    t.bye()

start = time.time()
t.onkeypress(report, 'space')
t.listen()
t.mainloop()
