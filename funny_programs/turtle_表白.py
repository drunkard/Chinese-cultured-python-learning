#!/cc/bin/python
import turtle as t

word = '罗'

def tohex(n):
    s = str(hex(n))
    s = s.removeprefix('0x')
    return s if len(s) == 2 else '0' + s

size = 600
t.setup(width=size, height=size)
t.penup(); t.right(90); t.forward(int(size/2))
for i in range(255):
    g = tohex(255 - i)
    b = tohex(i)
    t.pencolor('#CF' + g + b)
    t.write(word, move=False, align='center', font=('STKaiti', 420, 'bold'))
