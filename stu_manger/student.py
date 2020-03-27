"""
@author Chr.yl

"""


class Student(object):
    def __init__(self, id, name, tel):
        self.id = id
        self.name = name
        self.tel = tel

    def __str__(self):
        return f'{self.id},{self.name},{self.tel}'


