"""
集合推导式:使用不多,有去重性质

"""

list1 = [1, 1, 2]
# 返回数据的2次方
set1 = {i ** 2 for i in list1}
print(set1)
