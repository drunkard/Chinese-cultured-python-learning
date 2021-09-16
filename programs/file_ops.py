# 需求：
# [a-z].mkv 重命名为 01.mp4 这样的；
# 对文件所有者只读，其余人不可以看；
# mtime 时间改为现在；
# 如果是目录、且目录为空就删掉它；
from datetime import datetime
import path

def rename(f):
    # print('doing', f)
    name, suffix = f.name.lower().split('.')
    if name.isalpha():
        n = str(ord(name) - 96)
    else:
        n = name
    if len(n) == 1:
        n = '0' + n
    new_name = p.joinpath(n + '.mp4')
    print(f.name, '->', new_name.name)
    f.rename(new_name)

    # chmod
    new_name.chmod(0o400)

    # change mtime
    new_name.utime(times=(new_name.atime, datetime.now().timestamp()))


def process_dir(d):
    if d.files() + d.dirs():
        print(f'目录不是空的 {d}')
    else:
        d.removedirs()

p = path.Path('/home/mj/py_teach/programs/file_ops')
for f in p.files():
    rename(f)
for d in p.dirs():
    process_dir(d)






'''
import path
debug = 0

def rename(f):
    print(f'processing {f}', end='')
    # 清理空目录
    if f.isdir():
        if f.files():
            print(f'目录非空： {f}')
        else:
            if debug:
                print(f'删除了 {f}')
            else:
                print(' , is directory, deleted')
                f.move(deleted)
        return
    # 改权限
    f.chmod(0o400)
    # 文件改名
    name, suffix = f.name.lower().split('.')
    if name.isdigit() and suffix == 'mp4':
        print(' , already right name')
        return  # already right name

    if name.isalpha():
        n = str(ord(name) - 96)
    else:
        n = name
    if len(n) == 1:
        n = '0' + n
    new_name = n + '.mp4'
    if debug:
        print('DEBUG', f.name, '->', new_name)
    else:
        print(' , renamed')
        f.copy2(done.joinpath(new_name))  # copy file and mode
        f.move(raw)
        # f.rename(p.joinpath(new_name))  # do not use relative name

p = path.Path('/home/mj/py_teach/programs/file_ops')
raw = p.joinpath('RAW').makedirs_p()
done = p.joinpath('DONE').makedirs_p()
deleted = p.joinpath('DEL').makedirs_p()

files = p.files()
for f in files:
    rename(f)
'''
