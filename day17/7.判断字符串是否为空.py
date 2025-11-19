def is_string_empty(s, loose_mode=True):
    """
    判断字符串是否为空
    :param s: 待判断的变量（可任意类型）
    :param loose_mode: 宽松模式（True：空字符串/None/纯空白字符视为空；False：仅None/""视为空）
    :return: 布尔值（True=空，False=非空）
    """
    # 先处理 None 情况
    if s is None:
        return True
    # 非字符串类型直接返回非空
    if not isinstance(s, str):
        return False
    # 宽松模式：去除首尾空白后判断
    if loose_mode:
        return len(s.strip()) == 0
    # 严格模式：仅判断是否为 ""
    return s == ""


# ---------------------- 使用示例 ----------------------
# 测试不同场景
print(is_string_empty(None))  # True（None 视为空）
print(is_string_empty(""))  # True（空字符串）
print(is_string_empty("   "))  # True（宽松模式：纯空格视为空）
print(is_string_empty("   ", loose_mode=False))  # False（严格模式：纯空格不视为空）
print(is_string_empty("abc"))  # False（非空字符串）
print(is_string_empty(123))  # False（非字符串类型）
print(is_string_empty("\n\t"))  # True（宽松模式：换行/制表符视为空）
# ----------------------------------------------------------------------------------------
def remove_raw_empty_objects(obj_list):
    """
    删除字典列表（list<object>）中纯空的字典（{}）
    :param obj_list: 元素为字典的列表（可含非字典元素，会保留）
    :return: 移除纯空字典后的列表
    """
    # 过滤掉所有是字典且为空的元素，保留其他所有元素
    return [obj for obj in obj_list if not (isinstance(obj, dict) and len(obj) == 0)]
# ---------------------- 使用示例 ----------------------
# 原始列表（含纯空字典、非空字典、非字典元素）
obj_list = [
    {},  # 纯空字典（要删除）
    {"name": "张三", "age": 20},  # 非空字典（保留）
    {},  # 纯空字典（要删除）
    {"city": "北京"},  # 非空字典（保留）
    "这是字符串",  # 非字典元素（保留）
    {"name": "", "addr": None},  # 有key但值为空（保留，仅删纯空{}）
    123  # 非字典元素（保留）
]

# 直接调用方法，删除纯空{}
result_list = remove_raw_empty_objects(obj_list)

# 打印结果（纯空字典已被删除）
for item in result_list:
    print(item)
print(len(result_list))
# ----------------------------------------------------------------------------------------对象为空[{}]，不会删除对象
def filter_empty_values_in_obj_list(obj_list, loose_mode=True):
    """
    批量过滤字典列表（list<object>）中值为空的 key
    :param obj_list: 元素为字典的列表
    :param loose_mode: 字符串判空模式（同 is_string_empty 方法）
    :return: 处理后的字典列表（原列表实时修改）
    """
    for obj in obj_list:
        if not isinstance(obj, dict):
            continue  # 非字典元素跳过
        # 遍历字典副本的 key（避免实时删除导致遍历异常）
        for key in list(obj.keys()):
            if is_string_empty(obj[key], loose_mode):
                del obj[key]  # 删除值为空的 key
    # if json_loose_mode:
    #     return remove_raw_empty_objects(obj_list)
    return obj_list


# 原始字典列表
product_list = [
    {"name": "苹果", "desc": "", "price": 5.99, "tag": "   "},
    {"name": "香蕉", "desc": None, "price": 3.99, "tag": "水果"},
    {"name": "橙子", "desc": "酸甜", "price": 4.99, "tag": "\t"},
    {"name": "", "desc": "", "price": "", "tag": ""}
]

# 调用方法：批量过滤值为空的 key（宽松模式）
filter_empty_values_in_obj_list(product_list)

# 打印结果（值为空的 desc、tag 已被删除）
for item in product_list:
    print(item)
print(len(product_list))
print(remove_raw_empty_objects(product_list))
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