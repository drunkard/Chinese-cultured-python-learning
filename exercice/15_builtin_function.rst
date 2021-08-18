有趣有用的 Python 内置函数
==========================

.. code-block:: python

    # Python 内置变量、函数等；
    import builtins
    dir(builtins)

    max
    min

    all
    any

    filter
    map

    # zip()
    alist, blist = range(3), ['石头', '剪刀', '布']
    list(zip(alist, blist))
    dict(zip(alist, blist))

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

    input
