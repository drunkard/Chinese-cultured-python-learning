日期、时间模块
==============

datetime
time
timeit


.. code:: python

    # 日期格式化
    from datetime import datetime
    datetime.now().strftime("%Y-%m-%d")

    # 这里只有localtime可以被格式化，time是不能格式化的
    import time
    time.strftime("%Y-%m-%d", time.localtime())


time
----
.. code-block:: python

    import time

    # 时间戳
    time.time()
    time.ctime()
    time.ctime(time.time())
    time.localtime()
    time.localtime(time.time())

    # 计算程序执行时长
    start_time = time.time()
    total = 0
    for i in range(10):
        total += i
    print("Sum:", total)
    end_time = time.time()
    time_taken = end_time - start_time
    print("Time: ", time_taken)
