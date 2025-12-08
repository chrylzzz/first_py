"""
重写:
    子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写。
    即:在子类中重新定义同名的属性或方法即可。
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
        # 构造方法,优先执行父类的init方法
        super().__init__()
        self.kf = '儿子独创kongfu'

    def make(self):
        print(f'Per：{self.kf}')


# 重写
per = Per()
per.make()
