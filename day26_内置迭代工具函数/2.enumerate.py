"""
date 2026/1/7
@author chryl

二、enumerate() 方法
1. 核心功能
遍历一个可迭代对象时，同时获取元素的索引和值，返回一个 enumerate 对象（迭代器），每个元素是 (索引, 元素值) 的元组。
默认索引从 0 开始，可通过参数指定起始索引。

2. 语法
enumerate(iterable, start=0)
iterable：要遍历的可迭代对象。
start：索引起始值，默认 0。

4. 适用场景
遍历序列时需要索引标记（如统计元素位置、定位目标元素）。
替代手动维护索引变量（避免 i += 1 的冗余代码）。
"""
# 3. 实战案例
# 案例1：基础遍历（默认索引从0开始）
fruits = ["apple", "banana", "orange"]
for idx, fruit in enumerate(fruits):
    print(f"索引 {idx}: 水果 {fruit}")
# 输出:
# 索引 0: 水果 apple
# 索引 1: 水果 banana
# 索引 2: 水果 orange

print('-' * 20)

# 案例2：指定起始索引（从1开始）
for idx, fruit in enumerate(fruits, start=1):
    print(f"序号 {idx}: 水果 {fruit}")
# 输出:
# 序号 1: 水果 apple
# 序号 2: 水果 banana
# 序号 3: 水果 orange

print('-' * 20)

# 案例3：转换为列表查看 enumerate 对象
enum_list = list(enumerate(fruits, start=10))
print(enum_list)  # 输出: [(10, 'apple'), (11, 'banana'), (12, 'orange')]
