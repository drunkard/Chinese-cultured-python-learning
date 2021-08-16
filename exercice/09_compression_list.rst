compression list
================
.. code-block:: python

    # 生成列表
    [1 for x in range(10)]
    [x for x in range(10)]

    [x for x in range(10) if x % 2]  # 要干什么？
    [x for x in range(10) if not x % 2]  # 要干什么？

    # 过滤
    [x for x in range(10) if x % 2 == 0]
    [x for x in range(10) if x % 2 == 1]
    [x for x in range(10) if x % 2 != 0]
    [x for x in range(10) if x % 3 == 0]
    [x for x in range(10) if x % 3 != 0]
