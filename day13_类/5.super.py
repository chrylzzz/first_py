"""
调用父类的方法
"""


class Mas():
    def __init__(self):
        self.kf = 'kongfu'

    def make(self):
        print(f'Mas：{self.kf}')


class Per(Mas):
    def __init__(self):
        self.kf = '独创kongfu'

    def make(self):
        print(f'Per：{self.kf}')

    def make_sup(self):
        # 1.有参super :调用当前父类的方法
        ##注意规则:
        # super(当前类名,self).方法: 先init,以内要用父类的属性和方法,在调用方法
        # super(Per, self).__init__()
        # super(Per, self).make()

        # 2.无参数的super:也是当前父类
        super().__init__()
        super().make()


per = Per()
per.make_sup()
