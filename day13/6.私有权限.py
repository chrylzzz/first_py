"""
私有权限:
私有属性和方法:不能被继承给子类:


定义私有: __Xx
获取私有:
    属性
        get_Xx :获取私有属性
        set_Xx :修改私有熟悉

"""


class User():
    def __init__(self):
        self.kf = 'kf'
        # 私有属性
        self.__myKf = 'myKf'

    # 私有方法
    def __myKf(self):
        print('私有')

    # ###获取私有属性,注意这是属性,没有()
    def get_Kf(self):
        return self.__myKf

    # 设置私有属性的值
    def set_Kf(self, kf):
        self.__myKf = kf


class Man(User):
    pass


man = Man()
man.kf

user = User()
user.set_Kf('300')
print(user.get_Kf())
