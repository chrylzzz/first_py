"""
date 2026/1/7
@author chryl

3. iter() & next()：手动迭代控制
核心功能
iter()：将一个可迭代对象（如列表、字符串）转换为迭代器。
next()：手动获取迭代器的下一个元素，无元素时抛出 StopIteration 异常，可指定默认值避免报错。

语法
iter(iterable)
next(iterator, default=None)
"""
# 转换为迭代器
fruits = ["apple", "banana", "orange"]
fruit_iter = iter(fruits)

# 手动获取元素
print(next(fruit_iter))  # 输出: apple
print(next(fruit_iter))  # 输出: banana
# 无元素时返回默认值
print(next(fruit_iter, "no more"))  # 输出: orange
print(next(fruit_iter, "no more"))  # 输出: no more
