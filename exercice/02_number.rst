数字操作技巧
============

基本运算
--------
.. code-block:: python

    # 绝对值
    abs(-10)
    abs(10)

    # 计算商和余数
    divmod(10,3)

    # 次幂
    pow(3, 2)
    pow(3, 2, 4)  # 取余

    # 四舍五入
    round(10.0222222, 3)
    round(10.05, 1)

    # 求和
    a = [1,4,2,3,1]
    sum(a)
    sum(a, 10)


数字比较
--------
.. code-block:: python

    a = 5
    2 < a < 8
    2 < a <= 8
    1 == a < 3
    a >= 5


数字类型转换
------------
.. code-block:: python

    # 转浮点数
    float(3)
    float('a')

    # 转整数
    int('12', 16)


进制、进制转换
--------------
进制转换。

.. code-block:: python

    # 十进制、二进制
    bin(9)
    bin(10)
    int(0b111)

    # 十进制、八进制
    oct(7)
    oct(8)
    oct(10)
    int(0o111)
    int(0o8)  # work ?

    # 十进制、十六进制
    hex(15)
    hex(16)
    hex(255)
    int(0x111)
    int(0xff)


二进制
``````
.. code-block:: python

    len(bin(5))  # 值是多少？

    # Linux 下常见目录权限位
    0b111, 0b101, 0b101  # 755, 目录
    0b110, 0b100, 0b100  # 644, 普通文件

    0b111, 0b101, 0b000  # 750, /home 下的用户主目录
    0b100, 0b100, 0b100  # 444, 只读文件

    0b101, 0b101, 0b101  # 555, /bin 下的文件
    0b001, 0b111, 0b111, 0b111  # 1777, /tmp 的权限位


十进制
``````
.. code-block:: python

    -(-1) == 1

    int(-22.9)  # 值是多少？


复数
----
.. code-block:: python

    complex(1, 2) == complex('1+2j')  # 虚数


整数、字符串
------------
.. code-block:: python

    chr(65)
    ord('a')
    ord('天')
