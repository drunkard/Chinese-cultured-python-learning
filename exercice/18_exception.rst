异常处理技巧
============

assert
raise

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
