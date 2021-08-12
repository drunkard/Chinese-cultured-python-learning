#!/usr/bin/python3
import sys
import time
import turtle as t


# area for single number
num_area = (100, 200)

# t.reset()  # debug
t.pensize(5)


def move_pen():
    pass


def num0():
    t.reset()  # debug
    t.pensize(5); t.shape('turtle');
    t.setheading(90)
    t.circle(80, 180)
    t.forward(100)
    t.circle(80, 180)
    t.forward(100)


def num1(pos=(0, 0)):
    t.right(90)
    t.forward(200)


def num2(pos=(0, 0)):
    t.left(90)
    t.circle(-30, 180)
    t.right(30)
    t.forward(100)
    t.left(120)
    t.forward(60)


def num3(pos=(0, 0)):
    # t.reset()  # debug
    # t.pensize(5)
    t.forward(70)
    t.right(90)
    t.forward(9)

    t.right(45)
    t.forward(90)
    t.left(130)  # 下半个
    t.forward(15)
    t.circle(-45, 180)
    t.forward(15)


def num4(pos=(0, 0)):
    t.reset()  # debug
    t.pensize(5)
    t.right(115)
    t.forward(100)

    t.left(25); t.forward(15)
    t.left(90)
    t.forward(70)

    t.penup(); t.home(); t.pendown()
    t.right(90)
    t.forward(160)


def num5():
    # t.reset()  # debug
    # t.pensize(5); t.shape('turtle');
    t.forward(70)
    t.backward(70)
    t.right(90)
    t.forward(50)
    t.left(110)
    t.forward(10)
    t.circle(-45, 240)


def num6():
    t.reset()  # debug
    t.pensize(5); t.shape('turtle');
    t.left(100)
    t.circle(45, 160)
    t.setheading(270)
    t.forward(60)
    t.circle(45)


def num7():
    # t.reset()  # debug
    # t.pensize(5); t.shape('turtle');
    t.forward(70)
    t.right(115)
    t.circle(800, 10)


def num8():
    t.reset()  # debug
    t.pensize(5); t.shape('turtle');

    size = 100
    upfactor, downfactor = 0.65, 0.8
    t.circle(0 - size * upfactor, -180)
    t.circle(size * downfactor, -360)
    t.circle(0 - size * upfactor, -180)


def num9():
    # t.reset()  # debug
    # t.pensize(5); t.shape('turtle');

    size = 100
    factor = 0.8
    t.setheading(90)
    t.circle(size * factor, -360)
    t.setheading(270)
    t.forward(120)
    t.circle(0 - size * factor, 160)


def reset_panel():
    t.reset()  # debug
    t.pensize(5); t.shape('turtle');


def say_done():
    t.write('完事儿了，收工', move=False, align='left', font=('Arial', 20, 'bold'))
    time.sleep(2)


def draw_num(n):
    # 额外判断
    reset_panel()
    if isinstance(n, str) and not n.isdigit():
        print('{} is not number, passed'.format(n))
        return
    n = int(n)
    if n in draw_map:
        draw_map.get(n)(n)
        say_done()
    else:
        print('unknown number: {}'.format(n))


# draw_map = {n: 'num' + str(n) for n in range(0, 10)}
draw_map = {
    0: num0,
    1: num1,
    2: num2,
    3: num3,
    4: num4,
    5: num5,
    6: num6,
    7: num7,
    8: num8,
    9: num9,
}

# if __name__ == "__main__":
# print(sys.argv)  # debug
num = sys.argv[1]  # 提取要画的数字

print(num, type(num))  # debug
key = int(num)  # 字符串转数字

func = draw_map.get(key)  # debug, 找到此数字对应的函数
print(func)  # debug
draw_map.get(key)()  # 直接执行

time.sleep(2)  # 停顿一下，看清画出的数字
