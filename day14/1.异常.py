"""
异常:
语法:
    try:
        可能发生错误的代码
    except
        出现异常执行的代码

"""

try:
    f = open('test.txt', 'r')
except:
    f = open('testzzz.txt', 'w')

# 捕获指定异常捕获
try:
    print(1 / 0)
except ZeroDivisionError:
    print('有错误')

# 捕获多个指定异常
try:
    print(1 / 0)
except (ZeroDivisionError, NameError):
    print('有错误')

# 捕获异常描述信息
try:
    print(1 / 0)
except (ZeroDivisionError, NameError) as result:
    print(result)

# 捕获所有异常
try:
    print(1 / 0)
except Exception as result:
    print(result)

# 异常的else,没有异常要执行的代码
try:
    # print(1 / 0)
    print(1)
except Exception as result:
    print(result)
else:
    print('没有异常的代码...')

# 异常的finally:无论如何都执行,一般关闭文件
try:
    print(1 / 0)
    # print(1)
except Exception as result:
    print(result)
else:
    print('没有异常的代码...')
finally:
    print('这是finally')
