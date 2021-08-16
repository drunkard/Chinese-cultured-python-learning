字典操作技巧
============
.. code-block:: python

   # 两个字典
   dict1 = {"name": "Joy", "age": 25}
   dict2 = {"name": "Joy", "city": "New York"}

   # 合并字典有多种方法
   {**dict1, **dict2}
   dict1 | dict2  # python 3.9 才支持
