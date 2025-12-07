"""
1、模块是什么:
python模块(model),是一个python文件,以.py结尾,模块能定义函数,类,变量,也可以包含执行的代码
模块就是python文件

2、导入模块:多种写法
(1)
    import 模块名1
    import 模块名2
(2)
    from 模块名 import 功能1,功能2,功能3
(3)
    from 模块名 import *
上面三个是基础:
(4) as别名 :使用自己喜欢的别名 ,注意,如果定义了别名,就不能使用模块名
    import 模块名 as 别名
    form 模块名 import 功能 as 别名字

3、调用方法
模块.功能()
"""
# (1) 需要调用
import math
# (2) 直接用
from math import sqrt
# (3) 直接用
from math import *
# (4)
import math as mymath
from math import sqrt as mymath2

print(math.sqrt(9))

print(sqrt(9))

print(sqrt(8))

print(mymath.sqrt(9))
print(mymath2(8))
