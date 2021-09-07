有趣有用的 Python 内置函数
==========================
.. code-block:: python

    # Python 内置变量、函数等；
    import builtins
    dir(builtins)

    input
    open
    print

    len

    str
    format

    list
    tuple
    dict
    set
    frozenset
    frozenset([1,1,3,2,3])
    frozenset({1, 2, 3})

    # max / min
    mylist = [1,1,2,3,4,5,6,6,2,2]
    max(set(list), key=list.count)  # 出现次数最多的元素

    all
    all([1,0,3,6])
    all([1,2,3])
    any
    any([0,0,0,[]])
    any([0,0,1])
    bool
    bool([0,0,0])
    bool([])
    bool([1,0,1])


    # filter / map
    num_list = list(range(10))
    filter(lambda x: x % 2!=0, num_list)
    filter(lambda x: x>10,[1,11,2,45,7,6,13])

    type
    id
    # hash 可变对象不能 hash
    hash(object)
    hash(dict())  # TypeError: unhashable type: 'dict'
    hash(list)
    hash(list())  # TypeError: unhashable type: 'list'
    hash(set())   # TypeError: unhashable type: 'set'
    hash(tuple())


数字
----
见 02_number.rst

.. code-block:: python

    bin
    oct
    int
    hex
    complex
    float
    bytes
    bytearray


数学运算： abs/divmod/pow/round
-------------------------------
.. code-block:: python

    # abs
    abs(-6)

    divmod
    pow
    round
    sum


可迭代对象
----------

enumerate, zip
``````````````
.. code-block:: python

    iter
    next
    range
    range(0, 10, 2)  # 偶数
    range(10, -1, -1)  # 逆序

    # slice 切片
    s = slice(1, 10, 2)  # 定义切片对象，稍后可以重复使用
    range(1, 5)[s]
    s = slice(5, 1, -1)
    range(1, 5)[s]
    list(range(1, 5)[s])

    # zip() 聚合迭代器
    alist, blist = range(3), ['石头', '剪刀', '布']
    list(zip(alist, blist))
    dict(zip(alist, blist))  # 两个列表转成字典

    dic = dict(zip(alist, blist))  # {0: '石头', 1: '剪刀', 2: '布'}
    list(zip(dic, range(3)))
    list(zip(dic, range(3))) == zip(dic.keys(), range(3))
    list(zip(dic, range(3))) == list(zip(dic.keys(), range(3)))

    list(zip(dic.items(), range(3)))

    for a, b in zip(dic.items(), range(5)): print(a, b)
    for a, b, c in zip(dic.items(), range(5)): print(a, b, c)  # won't work
    for (a, b), c in zip(dic.items(), range(5)): print(a, b, c)

    # 打印字母表
    for low, up in zip(range(97,123), range(65, 91)): print(chr(low) + chr(up), end='')

    lows, ups = '', ''
    for low, up in zip(range(97,123), range(65, 91)):
        lows += chr(low)
        ups += chr(up)
    print(F'{lows}\n{ups}')

    # sorted
    a = [1,4,2,3,1]
    sorted(a,reverse=True)
    a = [{'name':'xiaoming','age':18,'gender':'male'},{'name':'xiaohong','age':20,'gender':'female'}]
    sorted(a,key=lambda x: x['age'],reverse=False)
    # reversed


    global
    nonlocal
    globals
    locals
    vars

    # compile
    s  = "print('helloworld')"
    r = compile(s, "<string>", "exec")
    exec(r)

    exec  # 不返回结果
    eval  # 返回结果
    s = "1 + 3 +5"
    eval(s)

    def
    return
    yield


    object
    super

    # callable 有 __call__() 方法的类才能被调用
    callable(str)
    property
    classmethod
    staticmethod
    getattr / hasattr / setattr / delattr
    isinstance / issubclass
