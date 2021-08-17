字符串操作技巧
==============

了解字符串
----------
.. code-block:: python

    # 字符和数字互转
    chr(97)
    [chr(n) for n in range(97, 123)]
    [chr(n) for n in range(65, 91)]
    [chr(n) for n in range(97, 123) if n%2 == 1]
    [chr(n) for n in range(97, 123) if n%2 == 0]
    plus = [chr(n) for n in range(97, 123) if n%2 == 0] + [chr(n) for n in range(97, 123) if n%2 == 1]
    plus
    sorted(plus)
    sorted(plus) == plus

    ord('a')
    ord('z')
    ord('A')
    ord('Z')
    [ord(x) for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    [ord(x) for x in 'abcdefghijklmnopqrstuvwxyz']

    # 拼接、拆分
    plus = [chr(n) for n in range(97, 123) if n%2 == 0] + [chr(n) for n in range(97, 123) if n%2 == 1]
    print(plus)
    s = ''.join(plus)
    print(s)
    sorted(s)
    ''.join(sorted(s))
    s2 = ', '.join(sorted(s))

    s.split()
    [c for c in s]
    s2.split()
    s2.split(',')
    s2.split(', ')


    'Hello!' * 5  # 结果是什么

    str(float()) * 2  # 结果是什么？

    a = '天高地厚'
    b = '天高' + '地厚'
    id(a) == id(b)  # 内存地址是否相同，相同就说明是同一个对象，否则就只是内容相同的两个对象

    c, d = '天高地厚', '天高地厚'
    id(c) == id(d)
    id(c) == id(d) == id(a)  # 结果如何？
    # 所以，同时赋值和单个独立赋值有什么优势？
    print(c, d)
    d += '我知道'
    print(c, d)
    id(c) == id(d)  # d 变量已发生变化，所以不再共享同一个对象，新建了一个


字符串格式化
------------
几种用法，比如：

#. ``'str is {}'.format()``
#. ``F'{str} is str'``


正则表达式 - re 模块
--------------------
匹配；
提取；
