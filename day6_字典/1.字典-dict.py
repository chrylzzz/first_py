"""
字典:可变类型,应用场景
    类似于map,键值对,无序,无效标,键名查询,创建空字典为{}

获取:
    .get(key,默认值):查找的key不存在返回默认值,如果无第二个参数返回none
    xxx[key]:可以获取,可以赋值,不存在报错
    .keys():查找所有的key,返回可迭代对象
    .values():查找所有的值,返回可迭代对象
    .items():返回的一个对象中有多个元组,
删除:
    del(字典) :未定义
    del(xxx['']):指定删除
    .clear() :置为空
修改:
    dict1['id'] = 10  #有值修改,无值增加
"""
print("------查找")
dict1 = {
    'name': 'nancy',
    "age": 20,
    'gender': 'f'
}
print(dict1.get('name'))
print(dict1['name'])
dict1['id'] = 10  # 可以直接添加,如果有数据就修改
print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())
print("=======新增")
dict1["birth"] = '2020-05-27'
print(dict1)
print("=======删除")
# 清空
# dict1.clear()
# print(dict1)

# 删除到未定义
# del dict1
# print(dict1)

# 指定删除,不存在就报错
del dict1['id']
print(dict1)
