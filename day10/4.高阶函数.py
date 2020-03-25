"""
高阶函数:把函数作为参数传入
内置高阶函数:
"""
import functools

# 绝对值
print(abs(-10))

# 四舍五入
print(round(1.2))


# f为函数
def sum_num(a, b, f):
    return f(a) + f(b)


res = sum_num(-1, -4, abs)
print(res)

#############
print('-------内置 高阶 函数')
# map(func,lst): 传入的函数 作用到每个元素中,并将结果组成新的 列表(py2)/迭代器(py3) 返回,可以用list(转换列表)
list1 = [1, 2, 3, 4]


def func(x):
    return x ** 2


re = map(func, list1)
print(re)
print(list(re))  # 直接用list函数转换

# reduce(func,lst):其中 func必须有连个参数,每次func计算的结果 继续和序列的下一个元素做累计计算
# 注意func 必须为两个参数
list2 = [1, 2, 3, 4]


def func(a, b):
    return a + b


# 注意必须导入functools才可以用reduce
resul = functools.reduce(func, list2)
print(resul)

# filter(func,lst):用于过滤序列,过滤掉不符合条件的元素,返回一个filter对象,如果要转换列表,可以使用list转换
list3 = [1, 2, 3, 4]


def func(x):
    return x % 2 == 0


resu = filter(func, list3)
print(resu)
print(list(resu))
