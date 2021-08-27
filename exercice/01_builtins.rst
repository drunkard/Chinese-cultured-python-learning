有趣有用的 Python 内置函数
==========================
.. code-block:: python

    # Python 内置变量、函数等；
    import builtins
    dir(builtins)

    input
    open
    print

    bin
    oct
    int
    hex
    complex
    float
    bytes
    bytearray

    abs
    divmod
    pow
    round

    str
    format

    len

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
    any
    bool

    # filter / map
    num_list = list(range(10))
    filter(lambda x: x % 2!=0, num_list)

    type
    id
    hash


可迭代对象
----------

enumerate, zip
``````````````
.. code-block:: python

    iter
    next

    # zip()
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

    sorted
    reversed


    global
    nonlocal
    globals
    locals
    vars

    compile
    exec  # 不返回结果
    eval  # 返回结果

    def
    return
    yield


    object
    super

    callable
    property
    classmethod
    staticmethod
    getattr / hasattr / setattr / delattr
    isinstance / issubclass
