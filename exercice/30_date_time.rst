日期、时间模块
==============

datetime
time
timeit

time
----
.. code-block:: python

    import time

    # 计算程序执行时长
    start_time = time.time()
    total = 0
    for i in range(10):
        total += i
    print("Sum:", total)
    end_time = time.time()
    time_taken = end_time - start_time
    print("Time: ", time_taken)
