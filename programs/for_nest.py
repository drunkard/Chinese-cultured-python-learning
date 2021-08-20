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


"""
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

分析：
- 可填在百位、十位、个位的数字都是1、2、3、4
- 组成所有的排列后再去掉不满足条件的排列
"""
def mesh_number(*numbers):
    pass
