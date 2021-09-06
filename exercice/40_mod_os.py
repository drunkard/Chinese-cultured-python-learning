# os 模块
# 操作系统相关的日常事务


# 路径
import os
p = os.path

d = os.getcwd()  # 当前程序在哪个目录
os.chdir('/usr/lib/python3.9')
'''
>>> p.dirname('/home/mj/py_teach/programs')
'/home/mj/py_teach'
>>> p.dirname('/home/mj/py_teach/programs/')
'/home/mj/py_teach/programs'

>>> p.exists('a')
True
>>> p.exists('/tmp/a')
True

>>> p.isdir('/tmp/a')
True
>>> p.isfile('/tmp/a')
False
>>> p.islink('/tmp/a')
False

>>> p.expanduser('~')
'/home/mj'
>>> p.expanduser('~/file')
'/home/mj/file'

>>> p.join('/tmp', 'a', 'b')
'/tmp/a/b'
>>> p.split('/data/pp_teaching/res_git/programs')
('/data/pp_teaching/res_git', 'programs')

>>> p.abspath('a')
'/tmp/a'
>>> p.realpath('a')
'/tmp/a'

>>> os.symlink('a', 'b')
>>> p.samefile('a', 'b')
True
>>> p.samefile('a', '/tmp/a')
True
'''


# 权限、所有者
os.chdir('/tmp')
os.mkdir('a')
os.stat('a')
os.chmod('a', 700)
os.chown('a', 0, 0)
