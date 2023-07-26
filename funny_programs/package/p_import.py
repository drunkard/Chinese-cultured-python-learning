# 不能导入顶级目录（包）里的，对它不可见
'''
from ..import_tests import show_env
show_env()
16:29:40 ~/py_teach/programs $ ./import_tests.py
['/data/pp_teaching/res_git/programs', '/usr/lib/python39.zip', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', '/usr/lib/python3.9/site-packages']
Traceback (most recent call last):
  File "/data/pp_teaching/res_git/programs/./import_tests.py", line 29, in <module>
    from package.p_import import it
  File "/data/pp_teaching/res_git/programs/package/p_import.py", line 15, in <module>
    from ..import_tests import show_env
ImportError: attempted relative import beyond top-level package
'''


# 不能导入顶级目录（包）里的，对它不可见
'''
from .. import turtle_flag_china
turtle_flag_china.draw_flag()
16:30:12 ~/py_teach/programs $ ./import_tests.py
['/data/pp_teaching/res_git/programs', '/usr/lib/python39.zip', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', '/usr/lib/python3.9/site-packages']
Traceback (most recent call last):
  File "/data/pp_teaching/res_git/programs/./import_tests.py", line 29, in <module>
    from package.p_import import it
  File "/data/pp_teaching/res_git/programs/package/p_import.py", line 30, in <module>
    from .. import turtle_flag_china
ImportError: attempted relative import beyond top-level package
'''

# print(f'\n__file__ = {__file__}')
def it():
    print('\n这是测试函数 it() 开始运行了')

    from .mod2 import DAM
    print('测试从 package/i2.py 导入变量:\n\t DAM =', DAM)
