# ----------------------------------------------------------------------------------------对象为空[{}]，删除对象
def process_empty_values_and_objects(obj_list, loose_mode=True):
    """
    批量处理 list<object>：1. 删除字典中空值key；2. 移除处理后为空的对象
    :param obj_list: 元素为字典的列表（list<object>）
    :param loose_mode: 宽松判空（True：空字符串/None/纯空格视为空；False：仅None/""视为空）
    :return: 处理后的纯净列表
    """

    # 内部辅助：判断值是否为空
    def is_empty(val):
        if val is None:
            return True
        if isinstance(val, str):
            return len(val.strip()) == 0 if loose_mode else val == ""
        return False  # 非字符串类型（如数字、列表）不视为空值

    valid_list = []
    for obj in obj_list:
        if not isinstance(obj, dict):
            valid_list.append(obj)  # 非字典元素直接保留
            continue

        # 第一步：删除当前字典中的空值key
        filtered_obj = {k: v for k, v in obj.items() if not is_empty(v)}

        # 第二步：仅保留处理后非空的字典（删除空对象）
        if filtered_obj:
            valid_list.append(filtered_obj)

    return valid_list

# 原始 list<object>（含空值key、处理后为空的对象、纯空{}、正常对象）
data_list = [
    {"name": "苹果", "price": 5.99, "desc": "", "stock": "   "},  # 空值key会被删，对象保留
    {"name": "", "price": None, "desc": "\t"},  # 处理后无有效key，会被删除
    {},  # 纯空对象，直接删除
    {},  # 纯空对象，直接删除
    {"name": "香蕉", "price": 3.99, "desc": "新鲜"},  # 无空值，完整保留
    "非字典元素",  # 非字典，保留
    {"name": "", "price": '', "stock": None}  # 空值key删除，对象保留
]
# ---------------------- 使用示例 ----------------------
# 调用方法，一键处理
cleaned_list = process_empty_values_and_objects(data_list)

# 打印结果（空值key已删，空对象已移除）
for item in cleaned_list:
    print(item)