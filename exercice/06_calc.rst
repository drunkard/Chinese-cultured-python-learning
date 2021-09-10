计算
====

x += y 和 x = x + y
-------------------
.. code-block:: python

    >>> x=1;x += 1;print x
    2
    >>> x=1;x = x+1;print x
    2
    >>> x=[1];x+=[2];print x
    [1, 2]
    >>> x=[1];x=x+[2];print x
    [1, 2]

    >>> x=[1];print id(x);x=x+[2];print id(x)
    4357132800
    4357132728
    >>> x=[1];print id(x);x+=[2];print id(x)
    4357132800
    4357132800
