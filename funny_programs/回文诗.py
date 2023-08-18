'''
按距离算法实现
先画格7x7，然后挨个填格
'''
import time
import turtle as t


txt = '''
牛郎織女會佳期，月底彈琴又賦詩。
寺靜惟聞鐘鼓響，音停始覺星斗移。
多少黄冠歸道觀，見機而作盡忘机。
几時得到桃园洞，同彼仙人下象棋。
'''

txt2 = '''
机時得到桃园洞
忘鐘鼓響停始彼
盡聞會佳期覺仙
作惟女牛底星人
而靜織郎彈斗下
機詩賦又琴移象
觀道歸冠黄少棋
'''

# t.goto(-200, -400)
# t.write(txt2, font=('Arial', 56, 'normal'))


# exs = ['月', '音', '见', '同', '寺', '多', '几']
t.reset(); t.penup()
t.speed('slowest')
wmin = 90
side_len, side_cursor = 2, 0
second = False  # 每个边长使用2次
current_sentence = 1  # 当前在第几句
sentence_len = 7  # 第一句是7个字，其余都是6个
sentence_cursor = 0  # 当前走到了句子的第几个字
colors = ['black', 'red']

for c in txt.strip():
    if c in ['，', '。', ' ', '\n', ]:
        continue
    print(f'{c}: side_len={side_len} side_cursor={side_cursor} second={second}')
    if not second:
        if side_cursor >= (side_len - 2):
            second = True
            side_cursor = 0
            t.right(90)
    elif second:
        if side_cursor >= (side_len - 1):
            side_len += 1
            second = False
            side_cursor = 0
            t.right(90)

    t.color(colors[(current_sentence + 1) % 2])
    if sentence_cursor == 0 and current_sentence > 1:
        print(f'ignored {c}')
        sentence_cursor += 1
        time.sleep(2)
        continue
    sentence_cursor += 1
    if sentence_cursor >= sentence_len:
        current_sentence += 1
        sentence_cursor = 0

    t.write(c, move=False, align='center', font=('Consolas', 60, 'bold'))
    t.forward(wmin)
    side_cursor += 1
time.sleep(5)
