"""
date 2026/1/7
@author chryl

一、zip() 方法
1. 核心功能
将 多个可迭代对象（如列表、元组、字符串）按索引打包，返回一个 zip 对象（迭代器），其中每个元素是一个元组，包含各可迭代对象对应位置的元素。
若可迭代对象长度不一致，zip() 会以最短的可迭代对象长度为准，截断多余元素。
可通过 list()、dict() 等函数将 zip 对象转换为列表、字典等数据结构。

2. 语法
zip(*iterables)
*iterables：一个或多个可迭代对象（如 list, tuple, str）。

4. 适用场景
同时遍历多个序列的对应元素（如姓名 - 年龄 - 成绩的匹配）。
快速构建字典（键值对分别来自两个序列）。
"""
# 3. 实战案例
# 案例1：基础打包（等长可迭代对象）
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
# 打包为 zip 对象，转换为列表查看
zipped = list(zip(names, ages))
print(zipped)  # 输出: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

print('-' * 20)

# 案例2：不等长可迭代对象（按最短截断）
scores = [90, 85]
zipped_short = list(zip(names, ages, scores))
print(zipped_short)  # 输出: [('Alice', 25, 90), ('Bob', 30, 85)]

print('-' * 20)

# 案例3：打包为字典（需两个等长可迭代对象）
person_dict = dict(zip(names, ages))
print(person_dict)  # 输出: {'Alice': 25, 'Bob': 30, 'Charlie': 35}

print('-' * 20)

# 案例4：解包 zip 对象（使用 * 操作符）
zipped_data = zip(names, ages)
unzip_names, unzip_ages = zip(*zipped_data)
print(unzip_names)  # 输出: ('Alice', 'Bob', 'Charlie')
print(unzip_ages)  # 输出: (25, 30, 35)
