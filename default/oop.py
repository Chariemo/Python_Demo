# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-05 11:06

class Student(object):

    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number

    @property
    def birth(self):
        return 2018 - 1995



stu1 = Student('chenjianlin', 12345)
print(stu1.get_name())
print(stu1._Student__name)
# print(stu1.__name)
stu1.__setattr__('phone', 3333333)
print(stu1.__getattribute__('phone'))
stu1.__add = '5555'
print(stu1.__add)

print(stu1.birth)
