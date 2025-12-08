# input()
# input接受的都是字符串,用变量接收
# password = input("请输出你的密码:")
# print(password)

# 数据转换
num = 1
str1 = '10'
# int() 数据转为整型,
print(type(int(str1)))
# float 转换为浮点数
print(float(num))
print(type(float(num)))

# str() 数据转为字符串
str(num)

# tuple() 将序列转为元组
list1 = [1, 2, 3, 4]
t = tuple(list1)
print(t)

# list() 将序列转为列表
t1 = (100, 200, 300)
print(list(t1))

# eval() 计算字符串中的 有效python表达式,并返回对象
# 把字符串里的数据转换为原本的类型
print(eval('100.1'))  # float
print(eval('[1,2,3,4]'))  # 列表
print(eval('{1,2,3,4}'))  # 集合
print(eval('(1,2,3,4)'))  # 元组

# python console:交互式开发,如果简单测试可以使用

# 多个变量赋值
num1, float1, str1 = 1, 2.4, 'abc'
# 多变量赋相同的值
a = b = 100
print(a)
print(b)

# 复合运算,注意
c = 10
c *= 1 + 3  # 先 1+3 在c*3:先算复合运算符右边的,再算复合运算
print(c)
