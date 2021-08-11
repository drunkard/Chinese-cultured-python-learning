Git 基础操作
============
Git 是一个开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。
Git 是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。
Git 与常用的版本控制工具 CVS, Subversion 等不同，它采用了分布式版本库的方式，不必服务器端软件支持。

官网： https://git-scm.com/
有 Windows 版，在家用电脑上可以自己安装。很多开发软件也嵌入了 git ， PyCharm 就支持git。

Deepin 深度Linux上安装 git::

    sudo apt install git

把我们上课的资料库克隆到本地 ::

    cd
    git clone https://gitee.com/drunkardee/python_teaching
    ls
    ls python_teaching

然后就可以打开： 文件管理器 -> 主目录 -> ``python_teaching`` ，里面就是我们上课的资料。


我改过内容、推送到服务器以后，内容不会自动更新到你的电脑上，你得自己手动更新，用下面这个命令 ::

    cd python_teaching && git pull

    # 或者这个命令
    git -C py_teach/ pull


简单工作流实例
--------------
一个简单的使用流程实例 ::

    cd ~
    git init my_program     # 新建项目， my_program 是个目录名

    cd my_program
    ls -a
    find .git/

登录 gitee.com ，注册帐号、登录。成功后再继续下面的步骤。
新建项目 ``my_program`` ，最好和本地项目同名。

本地 git 配置 ::

    git remote add gitee git@gitee.com:<用户名 drunkardee>/my_program.git
    git remote -v  # 查看配置好了没有

    # 设置自己的名字、邮箱地址
    git config user.name 'Drunkard Zhang'
    git config user.email gongfan193@gmail.com
    git config -l

测试本地源码库 ::

    git status

    vi README.rst  # 写一些项目介绍
    git status

    git add README.rst
    git status

    git commit -s README.rst
    git commit --amend -s
    git status

    find .git/

    git push --set-upstream gitee master  # 第一次 push 时
    git push

