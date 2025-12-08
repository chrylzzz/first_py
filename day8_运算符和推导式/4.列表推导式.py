"""
推导式:减少代码量,及其功能
    注意:返回值往左边填写,for左边写
列表:
字典:
集合:
"""
print("-----------列表推导式")
# while
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# for
list2 = []
for i in range(10):
    list2.append(i)
print(list2)

# 带range 的列表推导式 [] 里的就是列表推导式
list3 = [i for i in range(10)]
print(list3)

# 带 if 的列表推导式:带有判断的
list4 = [i for i in range(10) if i % 2 == 0]
print(list4)
# 多个 for 实现列表推导式
# 多个for循环 等同于for循环推导式
list6 = []
for i in range(1, 3):
    for j in range(3):
        list6.append((i, j))
list5 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list5)
print(list6)
