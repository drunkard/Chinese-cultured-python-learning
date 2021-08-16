random 模块 -- 随机变量生成器
=============================
随机的含义自己体会一下： 随机、随缘、随礼、随大流？

.. code-block:: python

    import random
    dir(random)

    vs = list(range(10))  # 列表 1-10
    random.shuffle(vs)  # 打乱顺序
    print(vs)  # 可能是 [9, 7, 4, 2, 8, 6, 3, 5, 0, 1]

    random.choices(vs)
    random.choice(vs)  # 随机挑出一个

    random.randint(1, 10)  # 随机整数
