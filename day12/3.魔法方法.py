"""
魔法方法
    _init_(): 初始化对象,在创建对象时被默认调用
    _str_():类似于toString,类似于说明的方法,必须有return
    _del_():删除对象的时候调用
"""


# 不带参数的init
class Person():
    def __init__(self):
        # 设置属性
        self.wid = 100
        self.hei = 200

    def get(self):
        print(f'{self.hei}')
        print(f'{self.wid}')

    # str 魔法方法
    def __str__(self):
        return '说明'

    def __del__(self):
        print(f'对象{self}被删除了')


person = Person()
person.get()
print(person)


# 带参数的 init
class User():
    def __init__(self, wi, hi):
        self.wi = wi
        self.hi = hi

    def get(self):
        print(f'{self.wi},{self.hi}')


# 在初始化的时候直接传输局
user = User(100, 20)
user.get()
