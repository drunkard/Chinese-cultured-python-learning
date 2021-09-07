文件
====
.. code-block:: python

    from os import path
    path.exists('/tmp')  # 路径是否存在

    import path
    p = path.Path('/tmp')
    p.files()
    p.exists()


open
----
mode取值表：
字符	意义
'r'	    读取（默认）
'w'	    写入，并先截断文件
'x' 	排它性创建，如果文件已存在则失败
'a'	    写入，如果文件存在则在末尾追加
'b' 	二进制模式
't'	    文本模式（默认）
'+' 	打开用于更新（读取与写入）

.. code-block:: python

    fo = open('D:/a.txt', mode='r', encoding='utf-8')
    fo.read()

