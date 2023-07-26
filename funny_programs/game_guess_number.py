import random

start, end = 1, 10

com = random.randint(start, end)
counter = 0
print(F'猜数字游戏现在开始，猜 {start} - {end} 之间的数字')
for i in range(5):
    human = int(input('请输入你猜到的数字 '))
    counter += 1
    if human > com:
        print('输入的大了，还剩 {} 次机会'.format(5 - counter))
    elif human < com:
        print('输入的小了，还剩 {} 次机会'.format(5 - counter))
    else:
        print('猜对了')
        break

levels = {
    1: '王者',
    2: '脑白金',
    3: '黄金的',
    4: '银子？',
    5: '铜锈',
}
print('评级： {}'.format(levels.get(counter, '不知道哎')))
