字典操作技巧
============
.. code-block:: python

    # 创建字典
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    f = dict({'one': 1, 'three': 3}, two=2)
    a == b == c == d == e == f

    # 转为字典
    dict(a='a', b='b')
    dict(zip(['a','b'], [1,2]))
    dict([('a',1), ('b',2)])

    # 排序
    d = {'one': 1, 'four': 4, 'eight': 8}
    {k: d[k] for k in sorted(d.keys())}
    {k: v for k, v in sorted(d.items(), key=lambda x: x[1])}

    # 两个字典
    dict1 = {"name": "Joy", "age": 25}
    dict2 = {"name": "Joy", "city": "New York"}

    # 合并字典有多种方法
    {**dict1, **dict2}
    dict1.update(**dict2)  # 用 dict2 更新 dict1
    dict1 | dict2  # python 3.9 才支持
    dict2 | dict1  # python 3.9 才支持, 谁覆盖谁？
    dict1 |= dict2  # 用dict2更新dict1
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

    # __missing__
    class Mydict(dict):
        def __missing__(self, key):  # 当 Mydict 使用切片访问属性不存在的时候返回的值
            return key


    # 字典重新映射
    users = {
        'fred': { 'user': 'fred', 'age': 40 },
        'pebbles': { 'user': 'pebbles', 'age': 1 }
    }
    new = {}
    for k, v in users.items():
        new[k] = v['age']

    # 字典推导式
    {x: x**x for x in range(10)}
    {x: chr(x) for x in range(256)}


字典方法
--------
.. code:: python

    In [76]: [x for x in dir(dict) if not x.startswith('__')]
    Out[76]: 
    ['clear',
     'copy',
     'fromkeys',
     'get',
     'items',
     'keys',
     'pop',
     'popitem',
     'setdefault',
     'update',
     'values']


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

