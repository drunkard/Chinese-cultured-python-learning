深入理解 Python 关键词
======================

True or False ?
---------------
每行一个题，判断真假。

.. code-block:: python

    id(True), id(False)  # True/False 的内存地址；记录一下，稍后我们再看看变了没有

    1 == True
    2 == True
    0 == False

    1 is True
    0 is False

    True + True
    True + False
    True + True * False
    type(True)
    False * True

    id(True), id(False)  # 变了么？


None 究竟是什么？
-----------------
.. code-block:: python

    id(None)  # None 的内存地址；记录一下，稍后我们再看看变了没有

    a = ''
    a is None
    None is None
    None == None

    None is False
    None == False
    None is not False
    None is not True

    id(None)  # 变了么？
