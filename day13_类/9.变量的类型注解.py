"""
date 2025/12/8
@author chryl

类型注解
    Python在3.5版本的时候引入了类型注解，以方便静态类型检查工具，IDE等第三方工具。类型注解:在代码中涉及数据交互的地方，提供数据类型的注解(显式的说明)。主要功能:
    帮助第三方IDE工具(如PyCharm)对代码进行类型推断，协助做代码提示
    帮助开发者自身对变量进行类型注释
支持:
    变量的类型注解
    函数(方法)形参列表和返回值的类型注解

语法一:
    1.变量类型注解/基础数据类型注解
        变量:类型
    2.类对象类型注解
    3.基础容器类型注解
    4.容器类型详细注解
        注意:
        元组类型设置类型详细注解，需要将每一个元素都标记出来
        字典类型设置类型详细注解，需要2个类型，第一个是key第二个是value
语法二:
    使用注释进行变量类型注释
        # type 类型
    如
        # type: int
        # type: dict[str,int]
        # type: Student
"""
import random

# 变量类型注解
var_1: int = 1
var_2: str = "2"
var_3: float = 3.14
var_4: bool = True


# 对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"name": "chryl"}
my_str: str = "hello"

# 容器类型详细注解,注意详细类型的顺序
chryl_list: list[str] = ["刘备", "马云", "Jordan"]
# 元组类型设置类型详细注解，需要将每一个元素都标记出来
chryl_tuple: tuple[str, int, bool] = ("nancy", 3, True)
chryl_set: set[int] = {1, 2, 3}
# 字典类型设置类型详细注解，需要2个类型，第一个是key第二个是value
chryl_dict: dict[str, int] = {"age": 23}

# 使用注释进行变量类型注释
randint = random.randint(1, 10)  # type: int
json_data = {"age": 23}  # type: dict[str,int]
student = Student()  # type: Student
