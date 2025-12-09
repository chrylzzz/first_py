"""
date 2025/12/9
@author chryl

抽象类
    抽象类:含有抽象方法的类称之为抽象类抽象方法:方法体是空实现的(pass)称之为抽象方法

    这种设计的含义是:
        父类用来确定有哪些方法
        具体的方法实现，由子类自行决定
        这种写法，就叫做抽象类(也可以称之为接口)


抽象类就好比定义一个标准，包含了一些抽象的方法，要求子类必须实现。


"""


# 配合多态，完成抽象的父类设计(设计标准)具体的子类实现(实现标准)

# 父类
# 抽象类
class AC:
    # 抽象方法
    def cool_wind(self):
        """制冷"""
        pass

    # 抽象方法
    def cool_hot(self):
        """制热"""
        pass

    # 抽象方法
    def swing_lr(self):
        """左右摆风"""
        pass


# 子类
# 具体实现
class Midea_AC(AC):
    def cool_wind(self):
        print("Midea cool_wind")

    def cool_hot(self):
        print("Midea cool_hot")

    def swing_lr(self):
        print("Midea swing_lr")


# 子类
# 具体实现
class GREE_AC(AC):
    def cool_wind(self):
        print("GREE cool_wind")

    def cool_hot(self):
        print("GREE cool_hot")

    def swing_lr(self):
        print("GREE swing_lr")
