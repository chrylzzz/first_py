"""

类方法:
    @classmethod来表示为类方法,第一个参数是类对象,一般用cls作为第一个参数
    类方法一般用作 私有类属性/类属性,定义类方法
静态方法:
    @staticmethod来修饰,可以通过类和对象访问
    当一个方法不需要参数传递(形参无self/cls),就可以定义为静态方法,减少参数传递,减少内存占用
"""


class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

    @staticmethod
    # 注意不传递任何形参
    def info_print():
        print('静态方法')


dog = Dog()
tooth = dog.get_tooth()
print(tooth)

Dog.info_print()
dog.info_print()
