"""
@author Chr.yl

1.自己的模块不要与已有的模块名重复
2.上面的会被后倒入或者自定义的 的替代
"""

from time import sleep
import time

# 2. 例如
# def sleep():
#     print('1111')


# 这样就被替换了
# sleep(2)

################拓展,名字重复的严重
print(time)

time = 1
# time 被替换了 , 后面的覆盖前面的同名的
print(time)
