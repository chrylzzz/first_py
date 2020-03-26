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


per = Per()
per.make()
