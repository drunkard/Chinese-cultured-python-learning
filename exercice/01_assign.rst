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

    # 自动、批量赋值
    >>> d
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'd' is not defined
    >>> globals()['d'] = 'object'
    >>> d
    'object'

    >>> exec('f = str')
    >>> f
    <class 'str'>

    # 多重赋值
    # 内部机制：先全部完成右边的表达式之后，再进行赋值。
    # In an assignment statement, the right-hand side is always evaluated fully before doing the actual setting of variables.
    a, b = 1, 2
    a, b = b, a  # 交换变量的值
    a, b = b, a + b

    a, b = [1, 'a']
    a, b = [1, 'b']
    (a, b, c), d = [(1, 2, 3), 'd']

    a, *b, c = [1, 2, 3, 4, 5]

    first_val, first_val[0] = [1], 2  # first_val 最终结果是什么？

    a, b, c = 'ABC'
    a, b, c = ['A', 'B', 'C']
    a, b, c = ('A', 'B', 'C')
    a, b, c = {1, 2, 3}
    a, b, c  = {'A': 1, 'A': 2, 'A': 3}
    a, b, c  = {'A': 1, 'A': 2, 'A': 3}.items()

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


LEGB
----
属性查找规则 LEGB（local，enclousing，global，bulitin）


避开可能的错误
``````````````
.. code-block:: python

    >>> def create_multipliers():
    ...     return [lambda x:i*x for i in range(5)]
    ...
    >>> for multiplier in create_multipliers():
    ...     print(multiplier(2))

    # 预期的结果时0，2，4，6，8. 但结果是5个8，意外不意外。
    # 修正
    def create_multipliers():
        return [lambda x, i = i:i*x for i in range(5)]


赋值题
------

