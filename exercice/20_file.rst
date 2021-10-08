文件
====
.. code-block:: python

    import os
    import path
    import shutil

    # 路径是否存在
    os.path.exists('/tmp')

    p = path.Path('/tmp')
    p.exists()
    p.files()[0].exists()

    # 复制
    shutil.copyfile('source.txt', 'dest.txt')

    # 文件名
    # secure_filename 将字符串转化为安全的文件名
    from werkzeug import secure_filename
    secure_filename("My cool movie.mov") # output:My_cool_movie.mov
    secure_filename("../../../etc/passwd") # output:etc_passwd
    secure_filename(u'i contain cool \xfcml\xe4uts.txt') # output:i_contain_cool_umlauts.txt


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

    # 写入文件
    print('hello, python print', file=open('/tmp/bad', 'w'))
