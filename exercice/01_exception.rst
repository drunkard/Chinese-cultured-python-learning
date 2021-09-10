异常处理技巧
============

try ... except [...]... else ... finally
raise
assert

try: ...
--------
try:
    suite
finally:
    suite

try:
    suite
except [type [as value]]:
    suite
[except [type [as value]]:
    suite]*
[else:
    suite]
[finally:
    suite]


raise
-----
.. code-block:: python

    raise Exception
    raise Exception('说点什么')


assert
------
.. code-block:: python

    # assert <条件判断表达式>
    assert 2 > 1
    assert 2 > 1, '说点什么'


exception examples
------------------
ImportError
```````````
复现：在包内部使用相对导入
14:17:25 ~/py_teach/programs $ python3 import_tests.py
Traceback (most recent call last):
  File "/data/pp_teaching/res_git/programs/import_tests.py", line 14, in <module>
    from .turtle_flag_china import draw_flag
ImportError: attempted relative import with no known parent package


UnboundLocalError
`````````````````
>>> a=1
>>> def func():
...     a+=1
...     print a
...
>>> func()
traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<stdin>", line 2, in func
UnboundLocalError: local variable 'a' referenced before assignment

import random
def func(ok):
    if ok:
        a = random.random()
    else:
        import random
        a = random.randint(1, 10)
    return a
func(True)# UnboundLocalError: local variable 'random' referenced before assignment
