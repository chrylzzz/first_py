age = 18
name = "chr"
weight = 65.5
stu_id = 1

# 基础符号
# %d 连接整型
print('今年 %d 岁' % age)  # 用%连接
# %s 连接字符串
print('名字 %s' % name)
# %.2f :浮点型保留两位小数
print('体重 %.2f' % weight)

# 高级符号,规范化
# 学号1变为001:%03d:显示三位数,不够用0补全,超出的原样输出
print('学号%03d' % stu_id)
# 多个符号连用:%()
print('名字 %s , 年龄 %d' % (name, age))
