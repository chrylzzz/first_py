"""
字典遍历 keys,values,items
 for 遍历

"""
dict1 = {
    'name': 'nancy',
    "age": 20,
    'gender': 'f'
}

# 遍历key
for key in dict1.keys():
    print(key)

# 遍历value
for val in dict1.values():
    print(val)

# 遍历 item
for item in dict1.items():
    print(item)

# 遍历字典的键值对
for k, v in dict1.items():
    print(f'{k}={v}')


