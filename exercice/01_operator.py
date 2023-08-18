操作符
======


常规数学计算
------------
+
-
*
/
//
**

+=
-=
*=
/=
**=


位操作 Bitwise Operation
------------------------
x >> y  # 返回 x 向右移 y 位得到的结果
x << y  # 返回 x 向左移 y 位得到的结果
x & y   # 且操作，返回结果的每一位是 x 和 y 中对应位做 and 运算的结果，只有 1 and 1 = 1，其他情况位0
x | y   # 或操作，返回结果的每一位是 x 和 y 中对应位做 or 运算的结果，只有 0 or 0 = 0，其他情况位1
~x      # 反转操作，对 x 求的每一位求补，只需记住结果是 -x - 1
x ^ y   # 或非运算，如果 y 对应位是0，那么结果位取 x 的对应位，如果 y 对应位是1，取 x 对应位的补