字典操作技巧
============
.. code-block:: python

    # 转为字典
    dict(a='a',b='b')
    dict(zip(['a','b'],[1,2]))
    dict([('a',1),('b',2)])

    # 两个字典
    dict1 = {"name": "Joy", "age": 25}
    dict2 = {"name": "Joy", "city": "New York"}

    # 合并字典有多种方法
    {**dict1, **dict2}
    dict1.update(**dict2)  # 用 dict2 更新 dict1
    dict1 | dict2  # python 3.9 才支持
    dict2 | dict1  # python 3.9 才支持, 谁覆盖谁？
    # 合并的原始方法
    newd = {}
    for k, v in dict1:
        newd[k] = v
    for k, v in dict2:
        newd[k] = v

    # 字典默认值
    d = {1: 'one', 2: 'two', 4: 'four'}
    d.get(3)
    d.get(3, '这里是默认值')


避免踩坑
--------
.. code-block:: python

    In [404]: a = dict.fromkeys(range(10), [])  # {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    In [405]: [id(v) for v in a.values()]
    Out[405]: 
    [140424521789824,
     140424521789824,
     140424521789824,
     140424521789824,
     140424521789824,
     140424521789824,
     140424521789824,
     140424521789824,
     140424521789824,
     140424521789824]

