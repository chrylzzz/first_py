str1 = 'aa'
str2 = 'aba'
list1 = [1, 2]
list2 = [5, 2]

"""

len()
del /del()

max(xx)
min(xx)
下边这俩一般用在 for循环里::::
range(start,end,step):不包含end,生成从start到end的数组,步长为step,供for循环使用
enumerate():将一个可遍历的数据对象组合为一个索引序列,同时标出数据和下标,一般在 for 中用
    用法:enumerate(可遍历,start=0):start参数为设置遍历数据的下标起始值,默认为0
"""
list_3 = list1 + list2

# range:不包含end
# 0-8
for i in range(0, 9, 1):
    print(i)

# 0-9
for i in range(10):
    print(i)
print('========')
# enumerate
# (下标,数据)
for i in enumerate(list_3):
    print(i)
# 下标,数据
for index, char in enumerate(list_3, start=0):
    print(f'index:{index}={char}')
