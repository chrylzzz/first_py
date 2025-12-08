"""
date 2025/12/8
@author chryl

构造方法:
    __init__
"""


# 类
class Student():
    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("chryl", 23)
print(student.name)
print(student.age)
