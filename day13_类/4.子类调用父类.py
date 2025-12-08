"""
继承之后,调用本类和父类的

"""

# 父类
class Mas():
    def __init__(self):
        self.kf = 'kongfu'

    def make(self):
        print(f'Mas：{self.kf}')

# 子类
class Per(Mas):
    def __init__(self):
        self.kf = '独创kongfu'

    def make(self):
        ############################这里注意,子类一旦使用了父类的同名方法,
        ############################就必须把自己的init 执行一下
        # 因为要用子类的方法和属性
        self.__init__()
        print(f'Per：{self.kf}')

    # 注意传入self
    def make_mas(self):
        # 注意这里必须初始化,因为要用父类的方法和属性
        Mas.__init__(self)
        Mas.make(self)

    def make_per(self):
        Per.__init__(self)
        Per.make(self)


per = Per()
per.make()
per.make_mas()
per.make_per()
