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

# 重写
per = Per()
per.make()
