"""
date 2025/12/9
@author chryl

多态
    比如
        函数(方法)形参声明接收父类对象
        实际传入父类的子类对象进行工作
    即:
        以父类做定义声明
        以子类做实际工作
        用以获得同一行为，不同状态

"""


# 父类
class Animal:
    def say_hello(self):
        pass


# 子类继承父类
class Dog(Animal):
    def say_hello(self):
        print("wangwangwang")


# 子类继承父类
class Cat(Animal):
    def say_hello(self):
        print("miaomiaomiao")


# 传入父类对象
def make_noise(animal: Animal):
    animal.say_hello()


# 验证多态
if __name__ == '__main__':
    make_noise(Dog())
    make_noise(Cat())
