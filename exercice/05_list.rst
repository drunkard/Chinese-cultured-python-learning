列表操作技巧
============
读取，各种读法。
.. code-block:: python
    num_list = list(range(10))

    # 最后一个元素
    num_list[-1]
    num_list.pop()

    # 切片
    # 每3个元素一组
    [[x for x in range(1, 101)][i:i+3] for i in range(0, 100, 3)]


操作，各种操作方法。
.. code:: python
    # 指定位置插入元素
    num_list.insert(2, 'a')

    # 反转列表
    num_list[::-1]
    num_list.reverse()

    # 排序
    sorted([5, 2, 9, 1])
    sorted([5, 2, 9, 1], reverse=True)

    # 去重 - 删除重复元素
    list1 = [1, 2, 3, 3, 4, 'John', 'Ana', 'Mark', 'John']
    list(set(list1))
    # 是否有重复的元素
    len(lst) == len(set(lst))

    # 数组对称差, 两个数组中不同的元素，并合成为一个新的数组
    _a, _b = set(a), set(b)
    [item for item in a if item not in _b] + [item for item in b if item not in _a]



    # 列表推导式
    [c for c in 'Good good study, 天天向上']

    # 最大值的 index
    al = [5, 8, 9, 7, 10, 3, 0]
    al.index(max(al))

    # 最长的字符串元素
    words = ['This', 'is', 'a', 'list', 'of', 'words']
    max(words, key=len)

    # 出现最多的元素
    alist = [9, 4, 5, 4, 4, 5, 9, 5, 4]
    max(set(alist), key=alist.count)

    # 二维列表
    def initialize_2d_list(w, h, val=None):
        return [[val for x in range(w)] for y in range(h)]

    initialize_2d_list(2,2)
    initialize_2d_list(2,2,0)
    [[n] for n in range(10)]

    # 合并列表
    a = [2, 3, 4, 5]
    b = ['a', 'b', 'c']
    a + b
    a.extend(b)

    # 切割数组
    def bifurcate_by(lst, fn):
        return [
          [x for x in lst if fn(x)],
          [x for x in lst if not fn(x)]
        ]
    bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')

    # 推导式
    [x for x in range(10)]

    # 展开嵌套列表
    # eg1 创建递归函数
    def flatten(li):
        return sum(([x] if not isinstance(x, list) else flatten(x) for x in li), [])
    >>> list_1 = [1, 2, [3], [4, [5, 6]]]
    >>> print(flatten(list_1))
    [1, 2, 3, 4, 5, 6]

    # eg2 列表推导式
    >>> li = [[14], [215, 383, 87], [298], [374], [2, 3, 4, 5, 6, 7]]
    >>> flat_list = [item for sublist in li for item in sublist]
    >>> print(flat_list)
    [14, 215, 383, 87, 298, 374, 2, 3, 4, 5, 6, 7]


避免踩坑
--------
.. code-block:: python

    # 生成嵌套列表, 这种方法有问题
    >>> a= [[]] * 10
    >>> a
    [[], [], [], [], [], [], [], [], [], []]
    >>> a[0].append(10)
    >>> a[0]
    [10]
    >>> a[1]
    [10]
    >>> a
    [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10]]  # 并非期望结果
    >>> [id(lst) for lst in a]
    [140424525589504,
     140424525589504,
     140424525589504,
     140424525589504,
     140424525589504,
     140424525589504,
     140424525589504,
     140424525589504,
     140424525589504,
     140424525589504]

    a = [[] for _ in range(10)]
    [id(lst) for lst in a]
    [140424520281216,
     140424530218048,
     140424520279232,
     140424520279936,
     140424517294784,
     140424517249664,
     140424520280384,
     140424517371712,
     140424524018304,
     140424520280448]


    # 生成嵌套列表、阵列、 array
    header = ['a', 'b', 'c', 'd', ]  # 标题，以后可能会增减
    init_len = 10
    result = [[0 for _1 in header] for _2 in range(init_len)]
    result.insert(header)


在访问列表的时候，修改列表

.. code-block:: python

    >>> def modify_lst(lst):
    ...     for idx, elem in enumerate(lst):
    ...         if elem % 3 == 0:
    ...             del lst[idx]
    ...

    >>> lst = [1,2,3,4,5,6]
    >>> modify_lst(lst)
    >>> lst
    [1, 2, 4, 5]

    >>> lst = [1,2,3,6,5,4]
    >>> modify_lst(lst)
    >>> lst
    [1, 2, 6, 5, 4]
    # 出错原因： lst在变短，但idx是递增的
