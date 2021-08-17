# 正方形蝴蝶结
import turtle
turtle.reset()
turtle.speed(0)
for i in range(38):
    turtle.right(91)
    for a in range(5):
        turtle.fd(100)
        turtle.right(90)


# 小九九
for i in range(1, 10):
    for j in range(1, 10):
        print('{}x{}={}'.format(j, i, i*j), end=' ')
        if j >= i:
            break
    print()
