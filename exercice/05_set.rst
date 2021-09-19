集合操作技巧
============
.. code-block:: python

    sa = {1, 2, 3, 4, 5, 6}
    sb = {2, 3}

    # 转为集合
    a = [1,4,2,3,1]
    set(a)

    # 冻结集合
    frozenset([1,1,3,2,3])

    # 集合的差集
    sa - sb
    # 交集
    sa & sb
    # 并集
    sa | sb
