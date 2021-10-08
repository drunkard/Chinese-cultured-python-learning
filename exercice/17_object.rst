类和对象
========
类把数据与功能绑定在一起。创建新类就是创建新的对象 *类型* ，从而创建该类型的新 *实例* 。

什么关系？

智能手机就是一个类（class），它是某类对象的统称，而你手上的这部iPhone7就是从属于智能手机这个类的一个具体实例／对象（object）。

智能手机都会有个电池容量的参数（智能手机这个类的域或类变量），智能手机的电池容量除以充电功率可得充满电需要的时长（这一行为称为智能手机这个类的方法）


哪个是 Python 对象？不能这么问， Python 里一切皆对象
====================================================
面向对象编程。
objective 目标、物体、对象。


玩转对象
--------
.. code-block:: python

    # 以常见的 True 为例
    True
    dir(True)

    True.__doc__
    print(True.__doc__)

    # 特殊对象
    # Ellipsis对象，代码中出现...省略号的现象
    >>> L = [1, 2, 3,]
    >>> L.append(L)
    >>> L
    [1, 2, 3, [...]]


定义对象
--------
.. code-block:: python

    # callable
    class Student():
        def __init__(self, id, name):
            self.id = id
            self.name = name
        def __repr__(self):
            return 'id = '+self.id +', name = '+self.name
    xiaoming = Student('001','xiaoming')
    callable(xiaoming)  # False

    class Student2(Student):
        # 重写 __call__ 方法后就能调用了
        def __call__(self):
            print('I can be called')
            print(f'my name is {self.name}')
    t = Student('001','xiaoming')
    callable(t)  # True
    t()

    delattr(xiaoming, 'name')
    hasattr(xiaoming, 'name')
    dir(xiaoming)
    getattr(xiaoming, 'name')
    id(xiaoming)
    issubclass(xiaoming, Student)  # 出错
    issubclass(xiaoming, Student2)  # 出错
    issubclass(Student2, Student)
    isinstance(xiaoming, Student)
    isinstance(xiaoming, Student2)
    isinstance(xiaoming, object)

    issubclass(int, (int, float))

    o = object()
    type(o)

    # 对象序列化
    import json
    with open('json.txt', 'w') as f:
        json.dump([xiaoming, xiaohong], f, default=lambda obj: obj.__dict__, ensure_ascii=False, indent=2, sort_keys=True)

    # 元类
    # Tim Peters: 元类就是深度的魔法，99%的用户应该根本不必为此操心。
    xiaoming.__class__  # __main__.Student
    xiaoming.__class__.__class__  # type
    Student = type('Student',(),{})  # 创建元类
    Student  # __main__.Student


.. code-block:: python

    # 对象属性
    # 创建属性的两种方式
    class C:
        def __init__(self):
            self._x = None

        def getx(self):
            return self._x

        def setx(self, value):
            self._x = value

        def delx(self):
            del self._x
        # 使用property类创建 property 属性
        x = property(getx, setx, delx, "I'm the 'x' property.")
    # 使用装饰器
    class C:
        def __init__(self):
            self._x = None

        @property
        def x(self):
            return self._x

        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self):
            del self._x



定义方法 - 运算方法
-------------------
狗1 + 狗2 = 二狗


对象怎么用？
------------


好几个对象怎么扯上关系
----------------------


自定义异常
----------


MetaClass 神奇？
----------------

