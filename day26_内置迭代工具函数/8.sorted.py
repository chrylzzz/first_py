"""
date 2026/1/7
@author chryl

5. sorted()：排序迭代
核心功能
对可迭代对象的元素进行排序，返回一个新的排序列表（注意：返回的是列表，不是迭代器，但常用于迭代场景）。
支持通过 key 指定排序依据，reverse 指定升序 / 降序。

语法
sorted(iterable, key=None, reverse=False)
"""
# 基础排序
nums = [3, 1, 4, 1, 5]
print(sorted(nums))  # 输出: [1, 1, 3, 4, 5]

# 按元素长度排序
words = ["apple", "banana", "cherry", "date"]
print(sorted(words, key=len))  # 输出: ['date', 'apple', 'banana', 'cherry']

# 降序排序
print(sorted(nums, reverse=True))  # 输出: [5, 4, 3, 1, 1]
