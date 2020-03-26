"""
@author Chr.yl
包:
    多个模块放在一个文件夹下,并且这个文件夹创建一个名字为 __init__.py 文件,name这个文件夹就成为包
    __init__.py 会自动创建
制作包:
    new -> python package

导入包:
    1.方法一
    import 包名.模块名
    调用:(1)包名.模块名.目标
        (2)as 起别名调用
    2.方法二
    from 包名 import *
    调用:(1)模块名.目标
    注意:必须在 __init__.py 文件中添加 __all__=[] 列表,来表示允许导入的模块列表,这里注意是模块列表
    步骤:1.在__init__.py设置all列表
        2.再from 包名 import *
"""
import myPackage.first.my_mod1 as m1
from myPackage.first import *

m1.info_pri1()
print('------')
my_mod2.info_pri2()
##################注意为什么是:1212??????
