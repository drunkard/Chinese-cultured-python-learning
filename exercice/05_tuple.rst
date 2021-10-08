元组操作技巧
============
通常用于存储不可变数据。

定义元组，倒腾清楚：

.. code-block:: python

    >>> a = (1, 2)
    >>> type(a)
    <type 'tuple'>
    >>> type(())
    <type 'tuple'>

    >>> a=(1)
    >>> type(a)
    <type 'int'>

    >>> a=(1,)
    >>> type(a)
    <type 'tuple'>

    # tuple使用+=奇怪的问题
    >>> t = (1, [2, 3])
    >>> t[1] += [4, 5]  # 会报错，但是操作成功了
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment
    >>> t
    (1, [2, 3, 4, 5])
    >>> t[1].append('x')
    >>> t[1].extend(['y'])
    >>> t
    (1, [2, 3, 4, 5, 'x', 'y'])


.. code-block:: python

    tuple
    tuple()

    type(tuple)    # tuple 的类型
    type(tuple())  # tuple() 的类型

    a = (5)
    b = (5, )
    isinstance(a, tuple)  # 判断 a 的类型是不是元组
    isinstance(b, tuple)  # 判断 b 的类型是不是元组
