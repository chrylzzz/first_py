"""
创建集合用:{} 或者set{}   ,集合为可变类型
创建空集合必须set(),因为{}为创建空字典
    特点:去重,

操作:
    增加:
        .add(x):增加单一数据,不可以增加序列
        .update(x):增加序列,不可以增加单一数据,报错
    删除
        .remove(x) :删除指定数据,如果没有就报错
        .discard(x): 删除指定数据,不存在也不报错
        .pop():随即删除,并返回这个数据
    查找:
        in
        not in

"""

s1 = {1, 2, 3, 4}
s3 = {1, 2, 2, 1}
s2 = set()

print(s1)
print(s2)
print(s3)

# 增加
s2.add(89)
print(s2)
# 只能增加单一数据,报错
# s2.add([5,7,8])
# print(s2)

# update 可以增加序列 ,不可以增加单一数据,报错
s2.update([4, 1, 57, 0])
print(s2)

# 删除
print('======删除')

# remove
# s2.remove(10)# 删除,没有就报错
# print(s2)

# discard
s2.discard(10)
print(s2)

# pop
del_num = s2.pop()
print(del_num)
print(s2)

print('=======查找')
print(10 in s2)
print(10 not in s2)
