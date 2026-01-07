"""
date 2026/1/7
@author chryl

4. reversed()：反向迭代
核心功能
返回一个反向顺序的迭代器，适用于所有支持反向遍历的对象（如列表、元组、字符串）。
该函数不修改原对象，而是生成新的反向迭代器。

语法
reversed(seq)
"""
# 反向遍历列表
nums = [1, 2, 3, 4]
rev_iter = reversed(nums)
print(list(rev_iter))  # 输出: [4, 3, 2, 1]

# 反向遍历字符串
s = "hello"
print(''.join(reversed(s)))  # 输出: olleh