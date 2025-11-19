def batch_rename_keys(obj_list, rename_map):
    """
    批量修改字典列表（list<object>）的多个key
    :param obj_list: 元素为字典的列表（必填）
    :param rename_map: 批量重命名映射，格式 {原key: 新key}（必填）
    :return: 修改后的字典列表
    """
    # 遍历每个字典，按映射批量重命名
    for obj in obj_list:
        if isinstance(obj, dict):  # 仅处理字典元素
            for old_k, new_k in rename_map.items():
                if old_k in obj:
                    obj[new_k] = obj.pop(old_k)  # 赋值新key并删除原key
    return obj_list

# ---------------------- 使用示例 ----------------------
# 1. 你的原始 list<object>（字典列表）
obj_list = [
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
# 2. 定义要修改的key映射（{原key: 新key}）
rename_map = {
    'name': '项目',
    "age": '年龄',
    'gender': '性别',
    'year_td': '年度',
    'quarter_td': '季度'
}
# for obj in obj_list:
#     # 遍历映射，逐个重命名
#     for old_k, new_k in rename_map.items():
#         if old_k in obj:
#             obj[new_k] = obj.pop(old_k)

# 3. 直接调用方法，得到修改后的结果
modified_list = batch_rename_keys(obj_list, rename_map)

# 打印结果
for item in modified_list:
    print(item)