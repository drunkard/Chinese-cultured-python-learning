#!/usr/bin/python3
"""
绘制标准的中国国旗
"""
import sys
import time
import turtle as t

debug = False

# 只需定义国旗尺寸即可，五角星位置都是计算出来的
flag_width = 900
flag_height = int(flag_width / 3 * 2)
extra = 10  # 为了让滚动条消失


def _debug_grid(width=flag_width, height=flag_height):
    '调试代码，画格子，验证画出来的国旗是否合规'
    if not debug:
        return
    t.pencolor('grey')  # 调试线颜色
    t.speed(0)  # fast, 画得快些
    # draw grid
    t.seth(0); goto((-width / 2, 0)); t.fd(width)
    t.seth(90); goto((0, -height / 2)); t.fd(height)

    # 调试线，小格的竖线
    for x in range(0, -width // 2, -width // 2 // 15):
        goto((x, 0))
        t.seth(90)
        t.fd(height / 2)

    # 调试线，小格的横线
    for y in range(0, height // 2, height // 2 // 10):
        goto((0, y))
        t.seth(180)
        t.fd(width / 2)

    # 小星到大星的连线，用于看小五角星是否指向大五角星中心
    pos0 = get_star_pos(0, width, height)
    for posn in range(1, 5):
        goto(get_star_pos(posn, width, height))
        t.setpos(pos0)

    print('画完了')


def draw_star(core_pos, radius, heading):
    """画一个五角星
    core_pos 五角星中心点坐标；
    heading 画笔指向，应该指向五角星中心点；
    step_size 五角星边线长度；

    eg: draw_star((-300, 150), 100, 270)
    """
    # goto right start pos
    goto(core_pos)
    t.setheading(heading)  # 设置笔头朝向
    t.penup(); t.backward(radius); t.pendown()  # 后退一个半径的距离
    t.left(18)  # 左转半个五角星内角 36/2=18 度

    # draw starts
    step_size = rim_len(radius)  # 算出五角星边长
    t.fillcolor('yellow')  # 设置填充颜色
    t.begin_fill()
    for _ in range(5):
        t.fd(step_size)
        t.left(72)
        t.fd(step_size)
        t.right(180 - 36)
    t.end_fill()

    # 调试代码，画五角星的圈
    # 前面刚画完五角星，所以笔还在画五角星的起始位置，只需要转对角度就可以开画了
    if debug:
        # time.sleep(2)  # 稍等一下，看看箭头指向
        t.pencolor('grey')
        t.right(90 + 18)
        t.circle(radius)


def get_star_pos(sn, width, height):
    """五角星位置
    sn 是五角星序号
    """
    # if debug:
    #     print('w2={}  h2={}  unit={}'.format(w2, h2, unit))

    # 定义五角星位置的小格的边长
    unit = int(width / 30)

    positions = {
        0: (-unit * 10, unit * 5),  # 大五角星
        1: (-unit * 5, unit * 8),  # 小五角星1
        2: (-unit * 3, unit * 6),
        3: (-unit * 3, unit * 3),
        4: (-unit * 5, unit * 1),
    }
    return positions[sn]


def get_star_specs(width, height):
    # 定义五角星位置的小格的边长
    unit = int(width / 30)

    # 五角星半径
    radius1 = int(height / 2 / 3)  # 大五角星

    args = []
    # 大星
    args.append((get_star_pos(0, width, height), radius1, 270))
    # TODO 计算正确的角度，不知道怎么计算的话可以估算一个，调试中不断优化
    # 小星1
    args.append((get_star_pos(1, width, height), unit, 33.2))
    # 小星2
    args.append((get_star_pos(2, width, height), unit, 10))
    # 小星3
    args.append((get_star_pos(3, width, height), unit, 343.6))
    # 小星4
    args.append((get_star_pos(4, width, height), unit, 320))

    print(args)
    if debug:
        print('Got star args:\n{}'.format(args))
    return args


def goto(pos):
    # 这个功能要多次用到，封装起来以后用的时候少写2行
    t.penup()
    t.setpos(*pos)
    t.pendown()


def rim_len(radius):
    '根据半径计算五角星边长'
    # TODO 准确计算，不知道怎么算的话根据半径估算一个
    return radius * 0.72


def draw_flag(width=flag_width, height=flag_height):
    # 设置窗口尺寸
    t.setup(width=width + extra, height=height + extra)
    # 设置画布尺寸、背景颜色
    t.screensize(canvwidth=width, canvheight=height, bg='red')

    # 更新一下，否则背景色不会即时显示
    t.update()
    t.pencolor('yellow')  # 笔的颜色。默认黑色，五角星就成了黑边。

    # 画五角星
    for core_pos, radius, heading in get_star_specs(width, height):
        draw_star(core_pos, radius, heading)

    # 如果不是调试，就隐藏画笔
    if not debug:
        t.hideturtle()
        t.update()

if __name__ == '__main__':
    t.speed(0)  # fast

    # 读参数，国旗尺寸
    # TODO 判断取到的尺寸是不是数字，不是的话提示一下
    if len(sys.argv) == 2:
        size = sys.argv[1]
        size = int(size)
    else:
        size = flag_height

    draw_flag(width=size * 1.5, height=size)
    _debug_grid()

    try:
        time.sleep(30)  # 国旗画完窗口就关闭了，让它延后退出
    except KeyboardInterrupt:
        print('等待中断')
    else:
        print('睡醒了')
