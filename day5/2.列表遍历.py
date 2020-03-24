import random

sor_lis = [1, 2, 5, 0, 3, 6, 7]
# 列表嵌套
name_list = [
    ['aa', 'ss', 'za'],
    ['11', '55', '88'],
    ['mc', 'op', 'lc']

]
"""
列表遍历: 一般用for
    while
    for
    
列表嵌套:
    就是多维的
"""
i = 0
while i < len(sor_lis):
    print(sor_lis[i])
    i += 1

print("=======")

for i in sor_lis:
    print(i)

print('-------嵌套列表')
print(name_list[1])
print(name_list[0][1])

print("----小练习")
tecs = [1, 2, 3, 4, 5, 6, 7, 8]
offices = [[], [], []]

for name in tecs:
    num = random.randint(0, 2)
    offices[num].append(name)

print(offices)

# 验证
i = 1
for office in offices:
    print(f'办公室{i},人数{len(office)},名字为:')
    for name in office:
        print(name)
    i += 1
