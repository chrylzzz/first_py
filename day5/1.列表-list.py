"""
列表: [ 数据1,数据2...]  ,可变类型
    可以同时为不同的数据类型!但是一般都存一个数据类型的,方便控制

列表的:增删查改
函数:
    .index(数据,开始下标,结束下标) ,返回指定数据的下标,数据不存在则报错
    .count(数据),统计指定数据在列表中出现的次数
    len(obj),列表的长度,公共函数,字符串和列表都可用
判断是否存在:
    in
    not in
增加数据:
    .append(序列或数据),结尾增加,如果追加的是一个序列,则把序列整个追加进去,不拆,带[]
    .extend(序列或数据),列表尾部追加数据,如果是序列,序列拆开(str会每个单独拆开),则逐个添加,不带[]
    .insert(下标位置,数据),指定位置新增数据,插入整个列表是也会带[],不拆
删除:
    del 目标: del name_list
        也可以删除指定下标的数据
    .pop(下标) ,指定下标删除,默认删除最后一个,无论如何都返回数据
    .remove(数据) , 删除指定的数据(只第一个匹配项)
    .clear() 清空列表,为空列表:None
查询:
    list[0]
    list[1]
修改:
    .reverse(),逆置
    .sort(key=None,reverse=False):reverse表示排序规则,=True为降序,=false为升序,key暂时用不到
    注意:这俩别Print(xxx.reverse()/xxx.sort()),建议分步执行,不要写在一行,
复制:
    list.copy():复制,数据进行修改的时候,一般都会复制一份数据
"""
from faker import Faker

print("============列表函数")
str1 = 'iiiooz'
name_list = ['tim', 'nancy', 'cc' 'pinkman', 'cc', 'yoyo']
name_nul_list = []
print(len(name_nul_list))
print(len(name_nul_list) == 0)
print(len(name_nul_list) != 0)
print(len(name_list))
print(name_list)  # 去重
print(name_list[0])
print(name_list.index('cc'))
print(name_list.count('cc'))
print(len(name_list))
print(len(str1))
print("============判断是否存在")
print('cc' in name_list)
print('ccz' not in name_list)

print("----测试")
# name = input("请输入名字:")
# if name in name_list:
#     print(f'您输入的名字 {name} 已经存在')
# else:
#     print(f"您的名字为{name}")

print("-------添加")
addLis = ['11', '22', '33']
name_list.append('azy')
name_list.append(addLis)
print(name_list)
name_list.extend('opz')
name_list.extend(addLis)
name_list.extend(['xiaom', 'xiaoh'])
print(name_list)
name_list.insert(1, 'ppo')
print(name_list)
name_list.insert(1, addLis)
print(name_list)
print("----------删除")
# del name_list
# del(name_list)
# print(name_list)  # is not defined 删除之后
del (name_list[0])  # 按下标删除
name_list.pop()
name_list.pop(1)
print(name_list)
name_list.remove('11')
print(name_list)
# print(name_list.clear())
print('---------修改')
sor_lis = [1, 2, 5, 0, 3, 6, 7]
sor_lis.reverse()
print(sor_lis)  # 逆置
# print(sor_lis.reverse())  # 直接使用还不行吗???
sor_lis.sort(key=None, reverse=False)
print(sor_lis)
print("---------复制")
cop_lis = sor_lis.copy()
print(cop_lis)
print("---------list截取")
# 初始化 Faker（默认英文数据，中文用 Faker('zh_CN')）
fake = Faker('zh_CN')  # 中文模拟数据
names = [fake.name() for _ in range(134)]
print(names[:5])
