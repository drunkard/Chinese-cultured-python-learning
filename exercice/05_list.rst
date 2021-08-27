列表操作技巧
============
.. code-block:: python

    num_list = list(range(10))

    # 最后一个元素
    num_list[-1]
    num_list.pop()

    # 去重 - 删除重复元素
    list1 = [1, 2, 3, 3, 4, 'John', 'Ana', 'Mark', 'John']
    list(set(list1))

    # 列表推导式
    [c for c in 'Good good study, 天天向上']
