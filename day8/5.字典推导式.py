"""
字典推导式: 返回值往左边填写,for左边写
    两个列表->字典:可以使用for 或字典推导式

"""
list1 = ['name', 'age', 'gender']
list2 = ['tom', 20, 'f']

# 字典推导式,返回值放在 for前面
# 如果两个列表长度一样
# 如果两个列表不一样长,统计少的
dict12 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict12)

# value是key 的2此房
dict1 = {i: i ** 2 for i in range(1, 5)}
print(dict1)

# 提取字典中的目标数据
count1 = {key: value for key, value in dict12.items() if key == 'age' and value > 9}
print(count1)
