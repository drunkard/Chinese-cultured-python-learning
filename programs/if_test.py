

# eg1
def sort_nums1():
    a = int(input('请输入数字 a = '))
    b = int(input('请输入数字 b = '))

    print('从小到大依次是： ', end='')
    if a > b:
        print(b, a)
    elif a < b:  # else if
        print(a, b)
    else:
        print(F'相等，都是 {a}')


# eg2
def sort_nums2():
    a = int(input('请输入数字 a = '))
    b = int(input('请输入数字 b = '))
    print(sorted([a, b]))


# eg3
def iq_test():
    iq = float(input('请输入你的智商 IQ 数值： '))
    print('\t', end='')
    if iq >= 160:
        print('你TND还真是个天才！！！')
    elif 160 > iq >= 140:
        print('嗯，你相当优秀')
    elif 140 > iq >= 110:
        print('还算聪明')
    elif 110 > iq >= 90:
        print('一般般')
    elif 90 > iq >= 80:
        print('还可以努力努力')
    elif 80 > iq >= 70:
        print('急需充值')
    elif 70 > iq:
        print('可能有窟窿，先去补吧')
    else:
        print('呃，你不属于这个世界')


# eg4 判断能否组成三角形
def trigon_test():
    i = input('给我三个数字，告诉你能不能组成三角形： ')
    nums = i.split(' ')
    nums = [float(x) for x in nums if x.isdigit()]  # 去除非数字、空字符
    # print(nums)  # debug
    if len(nums) == 3:
        a = max(nums)  # 取出最大数
        nums.remove(a)  # 删掉最大数
        # print(nums)  # debug
        b, c = nums
        if (b + c) > a:
            print('能', end='')
        else:
            print('不能', end='')
        print('组成三角形')
    else:
        print('错了，要三个数字')

# eg5
def isosceles_triangle_test():
    '等腰三角形判断'
    i = input('给我三个数字，告诉你能不能组成等腰三角形： ')
    nums = i.split(' ')
    nums = [float(x) for x in nums if x.isdigit()]  # 去除非数字、空字符
    if len(nums) == 3:
        a = max(nums)  # 取出最大数
        nums.remove(a)  # 删掉最大数
        b, c = nums
        if b == c and (b + c) > a:
            print('能', end='')
        else:
            print('不能', end='')
        print('组成等腰三角形')
    else:
        print('错了，要三个数字')

# eg6
def right_triangle_test():
    '直角三角形判断'
    i = input('给我三个数字，告诉你能不能组成直角三角形： ')
    nums = i.split(' ')
    nums = [float(x) for x in nums if x.isdigit()]  # 去除非数字、空字符
    if len(nums) == 3:
        a = max(nums)  # 取出最大数
        nums.remove(a)  # 删掉最大数
        b, c = nums
        if b**2 + c**2 == a**2 and (b + c) > a:
            print('能', end='')
        else:
            print('不能', end='')
        print('组成直角三角形')
    else:
        print('错了，要三个数字')


def login_lock():
    '''连续输错密码时锁定'''
    # import getpass
    import time
    retry = 2
    pwd = 'douniwan'
    counter = 0
    while True:
        p = input('请输入密码： ')
        # p = getpass.getpass(prompt='请输入密码： ')
        if p == pwd:
            return True
        else:
            counter += 1  # counter = counter + 1
            retry *= counter  # retry = retry * counter
            print(F'密码错误， {retry} 秒之后再试')
            time.sleep(retry)


def figure_guess1():
    """figure_guess1()

    石头剪刀布游戏
    """
    import random

    def won():
        print('你赢了')

    def lost():
        print('你输了')

    def even():
        print('平手')

    print('石头剪刀布，游戏开始啦')
    choices = ['石头', '剪刀', '布']
    while True:
        computer, human = random.choice(choices), input('请输入你的: ')
        if human == '石头':
            if computer == '石头':
                even()
            elif computer == '剪刀':
                won()
            else:
                lost()
        elif human == '剪刀':
            if computer == '石头':
                lost()
            elif computer == '剪刀':
                even()
            else:
                won()
        elif human == '布':
            if computer == '石头':
                won()
            elif computer == '剪刀':
                lost()
            else:
                even()
        else:
            print('你开小差了……')


def figure_guess2():
    import random

    def computer_vs_human(c, h):
        print(F'DEBUG: 我是{c}, 你是{h}')  # debug
        if c == h:
            print('平手')
        elif (c == '石头' and h == '布') or \
            (c == '剪刀' and h == '石头') or \
            (c == '布' and h == '剪刀'):
            print('你赢了')
        else:
            print('你输了')

    print('石头剪刀布，游戏开始啦')
    choices = ['石头', '剪刀', '布']
    while True:
        computer, human = random.choice(choices), input('请输入你的: ')
        if human in choices:
            computer_vs_human(computer, human)
        else:
            print('你开小差了……')


if __name__ == '__main__':
    # trigon_test()
    # isosceles_triangle_test()
    # while True:
    #     right_triangle_test()

    # if login_lock():
    #     print('登录成功了')

    # figure_guess1()
    # print(figure_guess1.__doc__)
    # figure_guess2()

    vars()
