"""
 lambda:如果只有一个返回值,或者只有一句代码就可以用
语法:
    lambda 参数列表 : 表达式
        参数可有可无,
        能接受任何数量的参数, 但只返回一个表达式的值
调用:
    调用的时候为
        xx()
"""

# 无参
print((lambda: 100)())
# 一个参数
print((lambda a: a)('hello'))
# 默认参数
print((lambda a, b, c=100: a + b + c)(10, 20))
# 可变参数 **args
print((lambda *args: args)(10, 20, 30))
# 可变参数 **kwargs  ,关键字参数
print((lambda **kwargs: kwargs)(name='python', age=20))

######
print('-------应用')
print((lambda a, b: a if a > b else b)(1000, 500))

#
l_num = lambda: 100  # 返回的是函数
print(l_num)
print(l_num())  # 调用 ()
# 累加
sum = lambda a, b: a + b
print(sum(1, 2))  # 调用的时候传入参数

#####
print('--------带判断的lambda')

# 按key的值排序
stu = [
    {'name': 'tt', 'agr': 20},
    {'name': 'zz', 'agr': 18},
    {'name': 'cc', 'agr': 22}
]
# 按 name值升序排序
stu.sort(key=lambda x: x['name'])
print(stu)
# 按 name值降序排序
stu.sort(key=lambda x: x['name'], reverse=True)
print(stu)
