"""
Chr.yl的第一个自定义模块
"""


# 两个数字的假发
def test_add(a, b):
    print(a + b)


# 注意测试的 不保留 ,否则重复调用
# test_add(1, 2)  #

# '__main__' 是系统变量,是模块的标识符,
# 如果__name__在本模块中使用,他的值就是'__main__' ,否则就是模块名
if __name__ == '__main__':
    print(__name__)
    test_add(1, 2)
# print(__name__)
