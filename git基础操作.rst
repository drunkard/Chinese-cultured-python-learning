Git 基础操作
============
Git 是一个开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。
Git 是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。
Git 与常用的版本控制工具 CVS, Subversion 等不同，它采用了分布式版本库的方式，不必服务器端软件支持。

官网： https://git-scm.com/

安装 git::

        sudo apt install git

把我们的资料库克隆到本地 ::

        cd
        git clone https://gitee.com/drunkardee/python_teaching

然后就可以打开： 文件管理器 -> 主目录 -> python_teaching ，里面就是我们的学习资料。


更新
----
我改过内容，推送到服务器端以后，内容不会自动更新到你的电脑上，你得自己手动更新，用下面这个命令 ::

        cd python_teaching
        git pull

        # 或者这个命令
        git -C py_teach/ pull

