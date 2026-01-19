"""
date 2026/1/19
@author chryl

"""
def list_json_to_markdown(json_list: list) -> str:
    """
    将 list<json> 数据转换为指定格式的 Markdown 字符串
    :param json_list: 包含 JSON 字典的列表
    :return: 格式化后的 Markdown 字符串
    """
    markdown_lines = []
    for item in json_list:
        # 遍历单个json字典，拼接key(加粗)和value
        for key, value in item.items():
            line = f"**{key}**：{value}"
            markdown_lines.append(line)
        # 不同json元素之间添加空行分隔，可根据需求调整
        markdown_lines.append("")
    # 拼接所有行，最后去除末尾多余空行
    return "\n".join(markdown_lines).rstrip()

# 测试示例
if __name__ == "__main__":
    # 模拟的 list<json> 数据
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
        }
    ]
    # 转换并打印结果
    md_str = list_json_to_markdown(test_data)
    print(md_str)