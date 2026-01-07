"""
date 2026/1/7
@author chryl

2. filter()：元素过滤
核心功能
根据一个判断函数筛选可迭代对象的元素，返回迭代器，仅包含判断结果为 True 的元素。
若判断函数为 None，则默认筛选真值元素（排除 False、0、''、[] 等）。

语法
filter(function, iterable)
"""
# 案例1：自定义判断函数（筛选偶数）
nums = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))  # 输出: [2, 4, 6]

# 案例2：函数为 None（筛选真值）
values = [0, 1, "", "hello", [], [1,2]]
result2 = filter(None, values)
print(list(result2))  # 输出: [1, 'hello', [1, 2]]