# 类属性、实例属性
# 实例方法 __str__() 和 __repr__()
class Class:
    '一个班的定义'
    school = 'jingsheng'
    # students = []

    def __init__(self, name, students):
        self.name = name
        self.students = self.students # or []

    def start_work(self):
        pass

    # __str__
    # __repr__

'''
c1 = Class(1, [1, 2, 3])
c2 = Class(2, [4, 5, 6])
print(c1.school, c1.students)
print(c2.school, c2.students)

# c1.students = c1.students + [8]
# c2.students += [9, 19]
# c1.students += [10]
# print(c1.school, c1.students)
# print(c2.school, c2.students)

print(c1)  # __repr__
'''


# 空类，稍后填入数据
class Student:

    def study(self, something):
        return 'learned', something


'''
xiaoming = Student()
xiaoming.name = 'xiaoming'
xiaoming.age = 12
print(xiaoming)
print(dir(xiaoming))
'''

