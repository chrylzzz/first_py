"""
1.私有权限:
私有属性和方法:不能被继承给子类:


2.定义私有: __Xx
私有成员变量:变量名以__开头(2个下划线)
私有成员方法:方法名以__开头(2个下划线)

3.获取私有属性和方法的方式, 通过定义方法来进行获取:
    属性
        get_Xx :获取私有属性
        set_Xx :修改私有属性

"""


# 父
class User():
    # 私有成员变量
    __chryl = "chryl"

    def __init__(self):
        # 公有变量
        self.score = '公有变量 score'
        # 私有属性
        self.__myScore = '私有变量 myScore'

    # 私有成员方法
    def __myScore(self):
        print('我的私有方法')  # 私有成员方法

    # 公有成员方法
    def pubScore(self):
        print('我的公有方法')

    # 获取私有属性, 注意这是属性,没有()
    def get_Score(self):
        return self.__myScore

    # 设置私有属性的值
    def set_Score(self, score):
        self.__myScore = score


# 子
class XiaoMing(User):
    pass


# 子类
xiaoming = XiaoMing()
#######################################################变量
# 获取公有变量, 可直接获取
print(f"公有变量：{xiaoming.score}")
# 获取私有变量, 无法直接获取私有变量, 直接获取时报错: 'XiaoMing' object has no attribute '__myScore'
# print(f"私有属性：{xiaoming.__myScore}")
# 获取私有变量, 可通过方法获取私有变量
print(f"调用方法,获取公有变量：{xiaoming.get_Score()}")
# 赋值私有属性, 通过方法进行赋值
xiaoming.set_Score("200")
print(f"调用方法,获取私有变量：{xiaoming.get_Score()}")

#######################################################方法
# 调用公有方法
xiaoming.pubScore()
# 调用私有方法, 无法直接调用私有方法, 直接调用时报错: 'XiaoMing' object has no attribute '__myScore'
# xiaoming.__myScore()

#######################################################方法
# 父类
user = User()
user.set_Score('300')
print(f"调用方法,父获取私有变量：{user.get_Score()}")
