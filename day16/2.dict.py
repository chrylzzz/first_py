"""
@author Chr.yl
    __dict__: 收集属性,方法:返回字典
"""


class A(object):
    a = 0

    def __init__(self):
        self.b = 1


a = A()
# 对象属性
print(a.__dict__)
#
print(A.__dict__)
