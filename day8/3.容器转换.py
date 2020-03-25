"""
容器转换:
    tuple():将序列转换为元组

"""
l1 = [1, 2, 3, 5]  # 列表
s1 = {1, 2, 3, 5}  # 集合
t1 = ('b', 'c', '1', 's')  # 元组
# 将序列转换为元组()
print(tuple(l1))
print(tuple(s1))
# 将序列转换为列表[]
print(list(s1))
print(list(t1))
# 将序列转换为集合{}
print(set(l1))
print(set(t1))
