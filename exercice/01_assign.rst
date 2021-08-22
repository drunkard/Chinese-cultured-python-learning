赋值
====
单个等于号用于赋值。

变量内可以装载任何内容？！！因为，在 Python 里，一切皆对象，那么它们就是一样的 - 都是对象，所以地位相似，都可以装进变量。

.. code-block:: python

    # 变量可以装载任何“对象”
    a = 1
    b = 'string'

    func = max
    alist = [1, 2, 4]
    max(alist)
    func(alist)

    # 多重赋值
    # 内部机制：先全部完成右边的表达式之后，再进行赋值。
    # In an assignment statement, the right-hand side is always evaluated fully before doing the actual setting of variables.
    a, b = 1, 2
    a, b = b, a  # 交换变量的值
    a, b = b, a + b

    a, b = [1, 'a']
    a, b = [1, 'b']
    (a, b, c), d = [(1, 2, 3), 'd']

    first_val, first_val[0] = [1], 2  # first_val 最终结果是什么？

    # 赋值表达式 - 赋值时带条件判断
    a = 'value 1' if True else 'value 2'
    a = 'value 1' if 'expr' is True else 'value 2'
    a = 1 if 3 >= 4 else 0
    a = True if 3 >= 4 and chr('a') == 65 else False
    a = True if 3 >= 4 or chr('a') == 65 else False

    # 赋值表达式 - 值为条件判断表达式
    a = 0 or 1
    a = False or True
    a = False or None or True
    a = False or None or True or []
