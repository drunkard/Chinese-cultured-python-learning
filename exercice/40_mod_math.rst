math
====

斐波那契
--------
.. code:: python

    # 非递归方式
    def fibonacci(length):
        if length <= 0:
            return [0]
        seq = [0, 1]
        while len(seq) <= length:
            nextv = (seq[len(seq) - 1] + seq[len(seq) - 2])
            seq.append(nextv)
        return seq
