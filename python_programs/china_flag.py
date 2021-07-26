#!/usr/bin/python3
"""
绘制标准的中国国旗
"""
import time
import turtle as t

debug = True

# 只需定义国旗尺寸即可，五角星位置都是计算出来的
flag_width = 900
flag_height = int(flag_width / 3 * 2)
extra = 10  # 为了让滚动条消失

# 五角星半径
radius1 = int(flag_height / 2 / 3)  # 大五角星
radius2 = int(flag_height / 2 / 10)  # 小五角星


def _debug_grid():
    '调试代码，画格子，验证画出来的国旗是否合规'
    if not debug:
        return
    t.pencolor('grey')
    t.speed(0)  # fast
    # draw grid
    t.seth(0); goto((-flag_width / 2, 0)); t.fd(flag_width)
    t.seth(90); goto((0, -flag_height / 2)); t.fd(flag_height)

    # 小格，竖线
    for x in range(0, -flag_width // 2, -flag_width // 2 // 15):
        goto((x, 0))
        t.seth(90)
        t.fd(flag_height / 2)

    # 小格，横线
    for y in range(0, flag_height // 2, flag_height // 2 // 10):
        goto((0, y))
        t.seth(180)
        t.fd(flag_width / 2)

    # 小星到大星的连线
    pos0 = get_star_pos(0)
    for posn in range(1, 5):
        goto(get_star_pos(posn))
        t.setpos(pos0)


def draw_star(core_pos, radius, heading):
    """画一个五角星
    core_pos 五角星中心点坐标；
    heading 画笔指向，应该指向五角星中心点；
    step_size 五角星边线长度；
    """
    # goto right start pos
    goto(core_pos)
    t.setheading(heading)
    t.penup(); t.backward(radius); t.pendown()
    t.left(18)

    # draw starts
    step_size = rim_len(radius)
    t.fillcolor('yellow')
    t.begin_fill()
    for _ in range(5):
        t.fd(step_size)
        t.left(72)
        t.fd(step_size)
        t.right(180 - 36)
    t.end_fill()
    # 画五角星的圈
    if debug:
        # time.sleep(2)  # 稍等一下，看看箭头指向
        t.right(90 + 18)
        t.circle(radius)


def get_star_pos(sn, width=flag_width, height=flag_height):
    """五角星位置
    sn 是五角星序号
    """
    unit = int(width / 30)
    # if debug:
    #     print('w2={}  h2={}  unit={}'.format(w2, h2, unit))
    positions = {
        0: (-unit * 10, unit * 5),  # 大五角星
        1: (-unit * 5, unit * 8),
        2: (-unit * 3, unit * 6),
        3: (-unit * 3, unit * 3),
        4: (-unit * 5, unit * 1),
    }
    return positions[sn]


def get_star_specs(width, height):
    args = []
    unit = int(width / 30)
    # 大星
    args.append((get_star_pos(0), radius1, 270))
    # TODO 计算正确的角度，不知道怎么计算的话可以估算一个，调试中不断优化
    # 小星1
    args.append((get_star_pos(1), unit, 33.2))
    # 小星2
    args.append((get_star_pos(2), unit, 10))
    # 小星3
    args.append((get_star_pos(3), unit, 343.6))
    # 小星4
    args.append((get_star_pos(4), unit, 320))

    if debug:
        print('Got args:\n{}'.format(args))
    return args


def goto(pos):
    t.penup()
    t.setpos(*pos)
    t.pendown()


def rim_len(radius):
    '根据半径计算五角星边长'
    # TODO 准确计算，不知道怎么算的话根据半径估算一个
    return radius * 0.72


def draw_flag(width=flag_width, height=flag_height):
    # 国旗尺寸
    t.setup(width=flag_width + extra, height=flag_height + extra)
    t.screensize(canvwidth=flag_width, canvheight=flag_height, bg='red')
    t.update()
    t.pencolor('yellow')

    # 画五角星
    for core_pos, radius, heading in get_star_specs(width, height):
        draw_star(core_pos, radius, heading)
    if not debug:
        t.hideturtle()
        t.update()
        time.sleep(9)

if __name__ == '__main__':
    if debug:
        t.speed(0)  # fast
    draw_flag()
    _debug_grid()
    if debug:
        print('画完了')
        time.sleep(55)
