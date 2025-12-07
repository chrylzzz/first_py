"""
@author Chr.yl

"""
# 注意 __all__指向的列表存的是方法名
__all__ = ['testA']


def testA():
    print("AAAAAA")


def testB():
    print("BBBBBB")


if __name__ == '__main__':
    testA()
    testB()
