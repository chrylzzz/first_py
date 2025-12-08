"""
经典类和旧式类:
    class 类名:
        ...

    class 类名(Object):
        ...

    class 类名(Object1,Object2...ObjectN):
        ...

括号(Object) 就是继承的类,Object就是父类

单继承,多继承:
    如果继承多个父类,只继承第一个父类的同名方法

pass关键字:
    语法不报错,进行补全

super关键字:
    使用父类的属性和方法
"""


# 父
class Mas():
    def __init__(self):
        self.kf = 'kongfu'

    def make(self):
        print(f'Mas：{self.kf}')


# 父
class Sch():
    def __init__(self):
        self.shuijiao = 'shuijiao'

    def make(self):
        print(f'Sch：{self.shuijiao}')


# 单继承
class Per(Mas):
    pass


# 多继承 :如果继承多个父类,只继承第一个父类的同名方法
class Per2(Mas, Sch):
    pass


# 多继承 :如果继承多个父类,只继承第一个父类的同名方法
class Per3(Sch, Mas):
    pass


# 单继承
per = Per()
per.make()

# 多继承
per2 = Per2()
per2.make()

# 多继承
per3 = Per3()
per3.make()


# 测试继承属性,使用构造方法
class Per1(Sch, Mas):
    def __init__(self, name, age):
        # 注意这里,子类使用构造方法时,必须先进行父类构造方法,否则会报错: AttributeError: 'Per1' object has no attribute 'shuijiao'
        super().__init__()
        self.name = name
        self.age = age
    # pass


per1 = Per1("chryl", 21)
# per1 = Per1()
per1.make()
