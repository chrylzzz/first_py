"""
说明文档:
 help()方法 :help查看函数的说明文档,

"""

# 如何定义说明文档:
# def 函数名(参数):
#   """说明文档位置"""
#   代码...
#
#
#
# 查看说明文档: help(函数名)

help(len)


#
def add_num(a, b):
    """
    求和函数
    :param a:
    :param b:
    :return: a+b
    """
    return a + b


help(add_num)
