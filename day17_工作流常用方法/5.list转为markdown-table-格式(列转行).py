"""
date 2026/1/19
@author chryl

"""
def list_json_to_markdown_transposed_table(json_list: list) -> str:
    """
    将 list<json> 数据转换为 列转行 的 Markdown 表格，key 加粗
    :param json_list: 包含 JSON 字典的列表
    :return: 格式化后的转置 Markdown 表格
    """
    if not json_list:
        return "无数据"

    # 提取所有唯一的 key，作为表格第一列
    all_keys = list({k for item in json_list for k in item.keys()})
    # 表格表头：第一列是属性，后续列是数据序号
    header = ["**属性**"] + [f"数据{i + 1}" for i in range(len(json_list))]
    header_line = f"| {' | '.join(header)} |"

    # 表格分隔行
    separator_line = f"| {' | '.join(['---'] * len(header))} |"

    # 生成每一行数据：第一列是加粗的key，后续是对应每个json的value
    data_lines = []
    for key in all_keys:
        row = [f"**{key}**"]  # 第一列key加粗
        for item in json_list:
            # 缺失key则填充"无"
            row.append(str(item.get(key, "无")))
        data_line = f"| {' | '.join(row)} |"
        data_lines.append(data_line)

    # 拼接所有部分
    return "\n".join([header_line, separator_line] + data_lines)


# 测试示例
if __name__ == "__main__":
    test_data = [
        {
            "姓名": "岩峰",
            "类别": "居民",
            "地址": "山东省烟台市芝罘区XX街道XX小区"
        },
        {
            "姓名": "李明",
            "类别": "商户",
            "地址": "山东省烟台市莱山区XX路XX号商铺"
        },
        {
            "姓名": "王华",
            "类别": "企业"
            # 故意缺失 address 字段，测试填充
        }
    ]
    transposed_table = list_json_to_markdown_transposed_table(test_data)
    print(transposed_table)