赋值
====
单个等于号用于赋值。

变量内可以装载任何内容？！！因为，在 Python 里，一切皆对象，那么它们就是一样的 - 都是对象，所以地位相似，都可以装进变量。

.. code-block:: python

    a = 1
    b = 'string'

    func = max
    alist = [1, 2, 4]
    max(alist)
    func(alist)

    a, b = 1, 2
    a, b = b, a  # 交换变量的值

    a, b = [1, 'a']
    a, b = [1, 'b']
    (a, b, c), d = [(1, 2, 3), 'd']

    # 赋值时带条件判断
    a = 'value 1' if True else 'value 2'
    a = 'value 1' if 'expr' is True else 'value 2'
    a = 1 if 3 >= 4 else 0
    a = True if 3 >= 4 and chr('a') == 65 else False
    a = True if 3 >= 4 or chr('a') == 65 else False

    # 值为条件判断表达式
    a = 0 or 1
    a = False or True
    a = False or None or True
    a = False or None or True or []
