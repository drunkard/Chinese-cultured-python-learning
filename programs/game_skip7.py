"""游戏 - 逢7拍腿、逢7过
规则： 遇到包含7或7的倍数的数字要拍腿，其余说出来
"""

# eg1
nums = filter(lambda x: x%7 == 0 or '7' in str(x), range(100))
print(list(nums))
