"""
date 2026/1/7
@author chryl

6. range()：数值序列迭代
核心功能
生成一个整数序列迭代器，常用于 for 循环指定次数，或生成连续数值。
Python 3 中 range() 返回迭代器对象，Python 2 中返回列表。

语法
range(start, stop, step=1)
"""
# 生成 0-4 的整数
for i in range(5):
    print(i, end=" ")  # 输出: 0 1 2 3 4

# 生成 2-8 的偶数
print(list(range(2, 9, 2)))  # 输出: [2, 4, 6, 8]