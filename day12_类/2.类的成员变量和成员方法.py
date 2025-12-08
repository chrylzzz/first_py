"""
date 2025/12/8
@author chryl
self 关键字是成员方法定义的时候，**必须填写的**。
它用来表示类对象自身的意思
当我们使用类对象调用方法的是，self会自动被python传入在方法内部，**想要访问类的成员变量**，**必须使用self**.(注意这里只针对访问成员变量,访问方法形参则不需要)
self关键字，尽管在参数列表中，但是传参的时候可以忽略它。

语法:
def 方法名(self,形参1...形参N):
    方法体
"""


# 类
class Student():
    # 成员变量/属性
    name = ''
    age = 0
    gender = ''

    # 成员方法,无形参
    def say_hi(self):
        # 访问成员变量时,使用self进行调用
        print(f'hi, 我是{self.name}')

    # 成员方法,有形参
    def say_hi_chryl(self, msg):
        # 访问方法形参时,不需要使用self
        print(f'hi, 我是{self.name}:{msg}')


student = Student()
student.name = 'chryl'
student.age = 2
student.gender = 'm'

print(student.name)
student.say_hi()
student.say_hi_chryl("你在干嘛")
