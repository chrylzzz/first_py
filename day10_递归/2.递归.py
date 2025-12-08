"""
递归

"""


# 累加 ,秒啊,必须有出口,否则超出最大递归深度
def sum_numbers(num):
    # RecursionError: maximum recursion depth exceeded
    if num == 1:
        return 1
    return num + sum_numbers(num - 1)


print(sum_numbers(3))
