"""
._mro_() : 查看 该类的继承关系


"""


class Mas():
    def __init__(self):
        self.kf = 'kongfu'

    def make(self):
        print(f'{self.kf}')


class Per(Mas):
    def __init__(self):
        self.kf = '独创kongfu'

    def make(self):
        print(f'{self.kf}')


print(Per.mro())
# [<class '__main__.Per'>, <class '__main__.Mas'>, <class 'object'>]


