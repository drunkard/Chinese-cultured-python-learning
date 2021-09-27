循环
====

有限循环用 for
--------------
.. code-block:: python

    # 一次脱壳2个元素
    for a, b in [range(5), range(6, 11)]: print(a, b)  # 会出错
    for a, b in [[range(5), range(6, 11)]]: print(a, b)

    # 还可以脱壳任意多个
    for a, b, c, d in ['A', 'B', 'C', 'D']: print(a, b, c, d)  # 会出错
    for a, b, c, d in [['A', 'B', 'C', 'D']]: print(a, b, c, d)


看不到头的循环用 while
----------------------
.. code:: python

    # 无限循环
    while True: print('一直叨叨到没电')
    while 1: print('一直叨叨到没电')

    # 累加到100
    total = 0
    while i <= 100:
        total += i
        i += 1
