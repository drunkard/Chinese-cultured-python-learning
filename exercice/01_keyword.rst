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

    True > False
    True > 1
    True >= 1
    False > 0
    False > -10

    id(True), id(False)  # 变了么？

    # 链式判断
    a = 2
    1 == a <= 3
    True == a <= 3
    3 > a > 2


批量判断真假
------------
.. code-block:: python

    # all() 全部为真返回真；any() 任一为真返回真；
    all([list(), tuple(), dict(), set(), '', None, False, 0])
    not all([list(), tuple(), dict(), set(), '', None, False, 0])
    any([list(), tuple(), dict(), set(), '', None, False, 0])
    not any([list(), tuple(), dict(), set(), '', None, False, 0])


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


import 导入模块
---------------
为了尽快启动、且快速运行， Python 默认情况下会 **轻装简行** ，不会加载用不到的模块，所有需要用的模块都需要 **手动** 加载。

.. code-block:: python

    import this  # Python 之禅：设计和编写 Python 程序的最佳守则
    >>> this
    <module 'this' from '/usr/lib/python3.9/this.py'>  # 自己看一下这个文件的内容

    # import 导入模块有多种用法，你可以选择最喜欢的、最合适的
    import turtle
    import turtle as t

    from turtle import *
    from turtle import forward, left
    from turtle import (forward, left)  # 导入太多、一行放不下的时候可以这样用

    from os.path import isdir
    from os.path import isdir as is_directory
    from os.path import (isdir as is_directory,
                         isabs as is_absolute_path,
                         isfile as is_file)
