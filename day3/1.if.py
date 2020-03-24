"""
if 条件:
    条件成立...()只执行缩进的代码,下方不缩进的不执行

"""
age = input("输入年龄:")
age = int(age)
# if (age >= 18) and (age <= 60):
#     print("gogogo:%s" % age)
# elif age <= 3:
#     print("???:%s" % age)
# else:
#     print("nonono:%s" % age)

#
# 化简写法:
# if 18 <= age <= 60:
#     print("gogogo")
# elif age <= 3:
#     print("???")
# else:
#     print("zzz")

#
# 嵌套if
if 18 <= age:
    if age >= 60:
        print("nonono")
    elif age < 60:
        print("yeyeye")
else:
    print("???")
