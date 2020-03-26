"""
@author Chr.yl
什么是all列表:模块的变量名,列表数据,控制模块的导入行为
    如果一个模块中有 __all__变量,当使用from xxx import * 导入时,只能倒入这个列表中的元素
    就是只能倒入 __all__这个变量指向的列表的存储名字的功能

all列表存什么    :
    #注意 __all__指向的列表存的是方法名

注意事项: 只有使用 from xxx import *  才会有鞠璇

"""

# import my_model1
from my_model1 import *

# 报错 ,没有添加到 __all__列表
# testB()
# yes
# testA()
