集合操作技巧
============
.. code-block:: python

    sa = {1, 2, 3, 4, 5, 6}
    sb = {2, 3}

    # 转为集合
    a = [1,4,2,3,1]
    set(a)

    # 合并列表
    a = {1, 2, 3}
    b = {2, 'a', 'b', 'c'}
    a.update(b)
    a | b

    # 集合推导式
    {x for x in range(10)}

    # 冻结集合
    frozenset([1,1,3,2,3])

    # 集合的差集
    sa - sb
    # 交集
    sa & sb
    # 并集
    sa | sb
