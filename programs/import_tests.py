#!/usr/bin/python3
# import sys, os, wcwidth  # 内置库、标准库、第三方库

def show_env():
    import sys
    print(f'sys.path = {sys.path}')

    attrs = ['__package__', '__name__', ]
    for a in attrs:
        print('{} = {}'.format(a, eval(a)))


# import sys
# print(sys.path)

# show_env()  # debug
# from turtle_flag_china import draw_flag  # right
# from .turtle_flag_china import draw_flag  # wrong
# if __name__ == '__main__':
#     draw_flag()

# 删除本路径也不能在当前路径下（包内部）做相对导入
'''
import sys
sys.path.remove('/data/pp_teaching/res_git/programs')
show_env()  # debug

from . import top
if __name__ == '__main__':
    print(f'value of top is: {top}')
'''


'''
from .package import var
print(var)

16:11:55 ~/py_teach/programs $ python3 import_tests.py
__package__ = None
__name__ = __main__
['/data/pp_teaching/res_git/programs', '/usr/lib/python39.zip', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', '/usr/lib/python3.9/site-packages']
Traceback (most recent call last):
  File "/data/pp_teaching/res_git/programs/import_tests.py", line 12, in <module>
    from .package import var
ImportError: attempted relative import with no known parent package
'''


from package import var
print(var)


from package.p_import import it
it()


from package import sub_packageA
print(sub_packageA)
