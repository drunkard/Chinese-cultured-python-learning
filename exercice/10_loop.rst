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

