有趣有用的 Python 内置函数
==========================
.. code:: python

    # Python 内置变量、函数等；
    import builtins
    dir(builtins)  # __dir__()

    __import__

    help

    input
    print
    print("hello", "world", sep="*", end="@")  # sep:打印出的内容用什么连接,end:以什么为结尾
    # 写入文件
    print('hello, python print', file=open('/tmp/bad', 'w'))
    open

    len

    str
    # format
    s = "hello world!"
    print(format(s, "^20"))  #居中
    print(format(s, "<20"))  #左对齐
    print(format(s, ">20"))  #右对齐
    print(format(3, 'b' ))    # 二进制:11
    print(format(97, 'c' ))   # 转换成unicode字符:a
    print(format(11, 'd' ))   # ⼗进制:11
    print(format(11, 'o' ))   # 八进制:13
    print(format(11, 'x' ))   # 十六进制(⼩写字母):b
    print(format(11, 'X' ))   # 十六进制(大写字母):B
    print(format(11, 'n' ))   # 和d⼀样:11
    print(format(11))         # 和d⼀样:11

    print(format(123456789, 'e' ))      # 科学计数法. 默认保留6位小数:1.234568e+08
    print(format(123456789, '0.2e' ))   # 科学计数法. 保留2位小数(小写):1.23e+08
    print(format(123456789, '0.2E' ))   # 科学计数法. 保留2位小数(大写):1.23E+08
    print(format(1.23456789, 'f' ))     # 小数点计数法. 保留6位小数:1.234568
    print(format(1.23456789, '0.2f' ))  # 小数点计数法. 保留2位小数:1.23
    print(format(1.23456789, '0.10f'))  # 小数点计数法. 保留10位小数:1.2345678900
    print(format(1.23456789e+3, 'F'))   # 小数点计数法. 很大的时候输出INF:1234.567890


    chr
    ord
    ascii
    print(ord('a'))  # 字母a在编码表中的码位:97
    print(ord('中'))  # '中'字在编码表中的位置:20013

    print(chr(65))  # 已知码位,求字符是什么:A
    print(chr(19999))  #丟
    for i in range(65536):  #打印出0到65535的字符
        print(chr(i), end=" ")

    print(ascii("@"))  #'@'


    list
    tuple
    dict
    set
    frozenset
    frozenset([1,1,3,2,3])
    frozenset({1, 2, 3})

    all
    all([1,0,3,6])
    all([1,2,3])
    all([1,'hello',True,9])
    any
    any([0,0,0,[]])
    any([0,0,1])
    any([0,0,0,False,1,'good'])
    bool


    # filter / map
    num_list = list(range(10))
    filter(lambda x: x % 2!=0, num_list)
    filter(lambda x: x>10,[1,11,2,45,7,6,13])

    list( map(lambda n: n**2, range(10, 20)) )


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
    bs = bytes("今天吃饭了吗", encoding="utf-8")
    print(bs)  #b'\xe4\xbb\x8a\xe5\xa4\xa9\xe5\x90\x83\xe9\xa5\xad\xe4\xba\x86\xe5\x90\x97'

    bytearray 返回一个新字节数组. 这个数字的元素是可变的, 并且每个元素的值得范围是[0,256)
    ret = bytearray("alex" ,encoding ='utf-8')
    print(ret[0])  #97
    print(ret)  #bytearray(b'alex')
    ret[0] = 65  #把65的位置A赋值给ret[0]
    print(str(ret))  #bytearray(b'Alex')

    bool
    bool([0,0,0])
    bool([])
    bool([1,0,1])


数学运算： abs/divmod/pow/round
-------------------------------
.. code-block:: python

    # abs
    abs(-6)

    divmod
    pow
    round
    sum

    # max / min
    mylist = [1,1,2,3,4,5,6,6,2,2]
    max(set(list), key=list.count)  # 出现次数最多的元素
    # 夹数, 如果 num 落在一段数字范围内，则返回num，否则返回离这个范围最近的边界
    max(min(num, max(a,b)),min(a,b))


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

    # enumerate
    lst = ['one', 'two', 'three', 'four', 'five']
    for index, el in enumerate(lst, 1):    # 把索引和元素一起获取,索引默认从0开始. 可以更改
        print(index)
        print(el)

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

    # sorted / reversed
    a = [1,4,2,3,1]
    sorted(a,reverse=True)
    a = [{'name':'xiaoming','age':18,'gender':'male'},{'name':'xiaohong','age':20,'gender':'female'}]
    sorted(a, key=lambda x: x['age'], reverse=False)


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
    repr
    s = "今天\n吃了%s顿\t饭" % 3
    print(s)  #今天# 吃了3顿    饭
    print(repr(s))  # 原样输出,过滤掉转义字符 \n \t \r 不管百分号%
    #'今天\n吃了3顿\t饭'


    # callable 有 __call__() 方法的类才能被调用
    callable(str)
    property
    classmethod
    staticmethod
    getattr / hasattr / setattr / delattr
    isinstance / issubclass
    isinstance(2, int)
    isinstance('2', str)
    isinstance('a', str)
    isinstance([2, 3, 4], list)
