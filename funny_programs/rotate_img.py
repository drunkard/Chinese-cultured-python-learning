# 假设下面是一个图片的数据矩阵
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

'''
右转90度应该是：
matrix2 = [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
'''


# eg1
def rotate1(matrix):
    matrix[:] = map(lambda x:x[::-1], zip(*matrix))
    return matrix


# eg2
def rotate2(matrix):
    n = len(matrix)
    for i in range(n):
        new_row = [row[i] for row in matrix[:n][::-1]]
        matrix.append(new_row)
    del matrix[:n]
    return matrix


if __name__ == '__main__':
    # print(rotate1(matrix))
    print(rotate2(matrix))
