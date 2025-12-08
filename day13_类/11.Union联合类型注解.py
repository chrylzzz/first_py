"""
date 2025/12/8
@author chryl

Union联合类型
    使用Union进行混合类型注释
    1.导包
    2.Union注释
"""
# 示例数据,这种数据如何进行注释
# my_list = [1, 2, "马云", "张飞"]
# my_dict = {"name": "chryl", "age": 18}

# 使用Union必须先导包
from typing import Union

# 1.变量联合类型注释
my_list: list[Union[str, int]] = [1, 2, "马云", "张飞"]
my_dict: dict[str, Union[str, int]] = {"name": "chryl", "age": 18}


# 2.函数联合类型注释
def swapped_dict(data: Union[str, int]) -> Union[int, str]:
    pass


# 测试
swapped_dict("你好")
swapped_dict(123456)
