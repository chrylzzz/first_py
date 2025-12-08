"""
很重要:

定义:
    def 函数名(参数):
        ...
        ...
        ...
调用:
    函数名(参数)
"""


# 函数有一个返回值
def add_num(a, b):
    res = a + b
    return res


num = add_num(1, 2)
print(num)


# 打印图案
def print_line():
    print('-' * 20)


def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(5)


############
# 如果函数有多个返回值,默认是元组类型(1, 2)  ,可以写列表,元组,字典,来返回多个返回值
def return_num():
    # return 1, 2
    return [1, 2, 3]
    # return {"a": 1, 'v': 3}


print(return_num())
