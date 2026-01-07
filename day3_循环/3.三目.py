"""
    语法：value_if_true if condition else value_if_false
"""
a = 1
b = 2
# 条件成立 if 条件 else 条件不成立
c = a if a > b else b
print(c)

# 条件成立 if 条件 else 条件不成立
c = a if a < b else b
print(c)

# 条件成立 if 条件 else 条件不成立
c = a if a == b else b
print(c)

# 语法：value_if_true if condition else value_if_false
a = 10
result = "大于5" if a > 5 else "小于等于5"
print(result)  # 输出: 大于5