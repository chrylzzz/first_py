def reorder_dict_keys(obj_list, target_order, fill_missing=True):
    """
    批量重新排序字典列表（list<object>）中每个字典的key顺序
    :param obj_list: 元素为字典的列表（必填）
    :param target_order: key的目标顺序列表，如 ["key1", "key2", "key3"]（必填）
    :param fill_missing: 字典缺少目标key时是否保留原key（True保留，False丢弃）
    :return: 按目标顺序排序后的字典列表
    """
    ordered_list = []
    for obj in obj_list:
        if not isinstance(obj, dict):
            ordered_list.append(obj)  # 非字典元素直接保留
            continue
        # 按目标顺序重建字典
        ordered_dict = {}
        # 先添加目标顺序中的key
        for key in target_order:
            if key in obj:
                ordered_dict[key] = obj.pop(key)
        # 处理剩余未在目标顺序中的key（保留或丢弃）
        if fill_missing:
            ordered_dict.update(obj)  # 追加剩余key（顺序在目标key之后）
        ordered_list.append(ordered_dict)
    return ordered_list


# ---------------------- 使用示例 ----------------------
# 1. 你的原始 list<object>（字典列表）
data_list = [
    {
        'name': 'nancy',
        "age": 20,
        'gender': 'f',
        'year_td': '1',
        'quarter_td': '1',
        '12个月停电4次': '1'
    }, {
        'name': 'jack',
        "age": 23,
        'gender': 'f',
        'year_td': '0',
        'quarter_td': '1',
        '12个月停电4次': '1'
    }, {
        'name': 'mark',
        "age": 18,
        'gender': 'f',
        'year_td': '1',
        'quarter_td': '0',
        '12个月停电4次': '1'
    }, {
        'name': 'max',
        "age": 21,
        'gender': 'm',
        'year_td': '1',
        'quarter_td': '1',
        '12个月停电4次': '1'
    }, {
        'name': 'lucy',
        "age": 27,
        'gender': 'm',
        'year_td': '0',
        'quarter_td': '0',
        '12个月停电4次': '1'
    },
]

# 2. 定义key的目标顺序（按需求调整）
target_key_order = ["age", "name", "gender", "year_td", "quarter_td","12个月停电4次"]

# 3. 直接调用方法，得到排序后的结果
sorted_list = reorder_dict_keys(data_list, target_key_order)

# 打印结果（每个字典key顺序一致）
for item in sorted_list:
    print(item)
