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
