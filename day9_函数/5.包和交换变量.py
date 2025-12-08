"""
组包:
拆包:
交换变量:
"""


# 元组拆包
def re_num():
    return 100, 200


num1, num2 = re_num()
print(num1)
print(num2)

# 字典拆包 ,拆的是字典的key
dict1 = {'name': 'tt', 'age': 20}
# 拆出来的是 字典的key
a, v = dict1
print(a)
print(dict1[a])
print(v)
print(dict1[v])

print('----------交换变量的值')
a, b = 10, 20
a, b = b, a
print(a)
print(b)
