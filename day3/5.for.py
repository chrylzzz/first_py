"""
for 临时变量 in 序列:
    执行的代码


有基础字符串和临时变量
"""

# for i in 'iteh':
#     print(i)

# TypeError: 'int' object is not iterable
# for i in 10:
#     print(i)

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}\t", end="")
        # print(f"{j} * {i} = {j * i}", end="")
        # print(f"{j} * {i} = {j * i}\t")
        # print(f"{j} * {i} = {j * i}")

    print()
