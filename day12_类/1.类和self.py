"""
self:指调用该函数的对象
"""


# 类语法
class Person():
    # 方法
    def wash(self):
        print('mixi')
        print(self)


# 创建对象
p = Person()
# self 和 p对象 的地址一样
print(p)
p.wash()

#### 两个类的self不同
p2 = Person()
print(p2)
