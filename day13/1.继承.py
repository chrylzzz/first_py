"""
经典类和旧式类:
    class 类名:
        ...

    class 类名(Object):
        ...


括号(Object) 就是继承的类

单继承,多继承:
    如果继承多个父类,只继承第一个父类的同名方法
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

# 单继承
per = Per()
per.make()

# 多继承
per2 = Per2()
per2.make()
