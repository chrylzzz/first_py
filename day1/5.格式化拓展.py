name = "mac"
age = 13
wei = 65.63
# %s可以当做字符串连接
# %d可以当做整数链接
# %f可以当做浮点数链接
print("name:%s,age:%s,wei:%s" % (name, age, wei))
print("name:%s,age:%d,wei:%f" % (name, age, wei))
print("name:%s,age:%d,wei:%.2f" % (name, age, wei))

#
"""
f表达式:  f'{表达式}'
比%s简洁,高效,易读
"""
print(f'名字:{name},年龄{age}')
print(f'2 * 2 的结果是： {2 * 2}')
