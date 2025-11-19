# 格式化打印
from pprint import pprint

"""
列表+字典
list [
    dict {

    }
]
"""
data_list = [
    {
        'name': 'nancy',
        "age": 20,
        'gender': 'f',
        'year_td': '1',
        'quarter_td': '1'
    }, {
        'name': 'jack',
        "age": 23,
        'gender': 'f',
        'year_td': '0',
        'quarter_td': '1'
    }, {
        'name': 'mark',
        "age": 18,
        'gender': 'f',
        'year_td': '1',
        'quarter_td': '0'
    }, {
        'name': 'max',
        "age": 21,
        'gender': 'm',
        'year_td': '1',
        'quarter_td': '1'
    }, {
        'name': 'lucy',
        "age": 27,
        'gender': 'm',
        'year_td': '0',
        'quarter_td': '0'
    },
]

print("-----------------")
for item in data_list:
    if item['year_td'] == '1':
        item['year_ch'] = '是'
    else:
        item['year_ch'] = '否'
    if item['quarter_td'] == '1':
        item['quarter_ch'] = '是'
    else:
        item['quarter_ch'] = '否'
# print(data_list)
pprint(data_list, indent=2)
# item['name'] + '-' + item['']
print("-----------------取前1个")
list3 = data_list[:1]
print(list3)
