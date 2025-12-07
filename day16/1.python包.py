"""
@author Chr.yl
包:
    包就是一个文件夹,多个模块放在一个文件夹下,并且这个文件夹下包含创建一个名字为 __init__.py 文件,那么这个文件夹就成为包
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
# 1.引入包名,无别名
import day16.myPackage.first.my_mod1

# 1.使用包名全路径.方法
day16.myPackage.first.my_mod1.info_pri1()

############################################################
# 2.引入包名,使用别名
import day16.myPackage.first.my_mod1 as m1

# 2.别名调用
m1.info_pri1()
print('------')
## 这里调用 my_mod1里的方法,则无法调用,因为使用了m1别名
my_mod1.info_pri1()

############################################################
# 3.使用from 包名 import *,这种方式导入的时候,init文件中必须有all配置
from day16.myPackage.first import *

# 3.my_mod2使用import * 导入的,那么就必须在init中声明all列表
my_mod2.info_pri2()
