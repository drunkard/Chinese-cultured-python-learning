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

    ord('汉字')  # 能否执行？
    ord('汉')
    ord('漢')  # 繁体字：汉
    chr(27721), chr(28450)

    # 任意对象转字符串
    str(100)
    str([])
    str(tuple())

    # 字符串转字节
    s = "apple"
    bytes(s, encoding='utf-8')

    # 字符串方法
    chr(0).isascii()
    chr(127).isascii()
    chr(128).isascii()
    '\n'.isascii()
    '\t'.isascii()
    'aA'.isascii()
    '123'.isascii()
    '123到'.isascii()

    # 比较一下字符和数字占用的内存数量
    import sys
    sys.getsizeof('漢') == sys.getsizeof(ord('漢'))
    sys.getsizeof('为学日益，为道日损'), sum([sys.getsizeof(ord(c)) for c in '为学日益，为道日损'])
    sys.getsizeof('A'), sys.getsizeof('a'), sys.getsizeof('大'), sys.getsizeof('龘')

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

    # 字符串倒序
    s = 'heeeello'
    s.split()
    [c for c in s]
    [c for c in s][::-1]
    l = [c for c in s]; l.reverse(); print(l)
    ''.join([c for c in s][::-1])
    ''.join(l)
    ''.join([c for c in s][::-1]) == ''.join(l)


    'Hello!' * 5  # 结果是什么

    str(int()) * 2
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

    # 统计出现次数
    from collections import Counter
    Counter('banana')
    Counter('hello, hello, python')
    Counter(['hello', 'hello', 'python'])
    Counter('hello, hello, python'.split())


字符串格式化
------------
几种用法，比如：

#. ``'str is {}'.format()``
#. ``F'{str} is str'``
#. ``"str is %s" % str()``
#. string.Template

format
``````
.. code-block:: python

    print("i am {0},age{1}".format("tom",18))  # i am tom,age18

3.1415926	{:.2f}	3.14	保留小数点后两位
3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
-1      	{:+.2f}	-1.00	带符号保留小数点后两位
2.71828	    {:.0f}	3   	不带小数
5          	{:0>2d}	05	    数字补零 (填充左边, 宽度为2)
5	        {:x<4d}	5xxx	数字补x (填充右边, 宽度为4)
10      	{:x<4d}	10xx	数字补x (填充右边, 宽度为4)
1000000	    {:,}	1,000,000	以逗号分隔的数字格式
0.25	    {:.2%}	25.00%	百分比格式
1000000000	{:.2e}	1.00e+09	指数记法
18  	    {:>10d}	' 18'	右对齐 (默认, 宽度为10)
18	        {:<10d}	'18 '	左对齐 (宽度为10)
18      	{:^10d}	' 18 '	中间对齐 (宽度为10)


正则表达式 - re 模块
--------------------
匹配；

.. code-block:: python

    import re

    # 文本查找
    text = "The rain in spain"
    result = re.search("rain", text)
    print(True if result else False)


提取；

