vim 编辑器
==========

模式
----


Python 开发环境
---------------
vim 可以作为 IDE 环境使用，“配置得当，可抵十万雄兵”。

在深度 Linux 上需要安装 vim 的 Python 环境，否则 vim 不能运行Python IDE配置文件 ::

    vim --version  # 查看是否支持 Python
    sudo apt install vim-python-jedi

    vim --version

    VIM - Vi IMproved 8.2 (2019 Dec 12, compiled Jun 16 2021 19:30:33)
    Included patches: 1-814
    Modified by Gentoo-8.2.0814-r100
    Compiled by mj@localhost
    Huge version without GUI.  Features included (+) or not (-):
    +acl               -farsi             +mouse_sgr         +tag_binary
    +arabic            +file_in_path      -mouse_sysmouse    -tag_old_static
    +autocmd           +find_in_path      +mouse_urxvt       -tag_any_white
    +autochdir         +float             +mouse_xterm       -tcl
    -autoservername    +folding           +multi_byte        +termguicolors
    -balloon_eval      -footer            +multi_lang        +terminal
    +balloon_eval_term +fork()            -mzscheme          +terminfo
    -browse            +gettext           +netbeans_intg     +termresponse
    ++builtin_terms    -hangul_input      +num64             +textobjects
    +byte_offset       +iconv             +packages          +textprop
    +channel           +insert_expand     +path_extra        +timers
    +cindent           +ipv6              -perl              +title
    +clientserver      +job               +persistent_undo   -toolbar
    +clipboard         +jumplist          +popupwin          +user_commands
    +cmdline_compl     +keymap            +postscript        +vartabs
    +cmdline_hist      +lambda            +printer           +vertsplit
    +cmdline_info      +langmap           +profile           +virtualedit
    +comments          +libcall           -python            +visual
    +conceal           +linebreak         +python3           +visualextra
    +cryptv            +lispindent        +quickfix          +viminfo
    +cscope            +listcmds          +reltime           +vreplace
    +cursorbind        +localmap          +rightleft         +wildignore
    +cursorshape       -lua               -ruby              +wildmenu
    +dialog_con        +menu              +scrollbind        +windows
    +diff              +mksession         +signs             +writebackup
    +digraphs          +modify_fname      +smartindent       +X11
    -dnd               +mouse             -sound             +xfontset
    -ebcdic            -mouseshape        +spell             -xim
    +emacs_tags        +mouse_dec         +startuptime       -xpm
    +eval              +mouse_gpm         +statusline        +xsmp_interact
    +ex_extra          -mouse_jsbterm     -sun_workshop      +xterm_clipboard
    +extra_search      +mouse_netterm     +syntax            -xterm_save
       system vimrc file: "/etc/vim/vimrc"
         user vimrc file: "$HOME/.vimrc"
     2nd user vimrc file: "~/.vim/vimrc"
      user exrc file: "$HOME/.exrc"
       defaults file: "$VIMRUNTIME/defaults.vim"
      fall-back for $VIM: "/usr/share/vim"
    Compilation: x86_64-pc-linux-gnu-gcc -c -I. -Iproto -DHAVE_CONFIG_H     -O2 -march=haswell -pipe -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1       
    Linking: x86_64-pc-linux-gnu-gcc   -Wl,-O1 -L/usr/local/lib -Wl,--as-needed -o vim    -lSM -lICE -lXpm -lXt -lX11 -lXdmcp -lSM -lICE  -lm -ltinfo -lelf   -lacl -lattr -lgpm -ldl     -lpython3.9 -lcrypt -lpthread -ldl -lutil -lm -lm      

``python3`` 前面是减号 ``-`` 说明不支持，加号 ``+`` 说明支持；
