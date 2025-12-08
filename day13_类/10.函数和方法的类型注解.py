"""
date 2025/12/8
@author chryl

函数和方法类型注解:
    def Function(形参名:类型, 形参名:类型, ......):
        pass

函数返回值类型注解
    def Function(形参名:类型, 形参名:类型, ......) -> 返回值类型:
            pass
"""


# 形参注释
def add(x: int, y: int):
    print(x + y)


# 形参注释
def list_print(data: list):
    print(data)


# 返回值注释
def return_data(data: list) -> list:
    return data


add(1, 2)
list_print(["你好", "马云", "张飞"])
return_data(["你好", "马云", "张飞"])
