def list_obj_to_md_table(obj_list):
    # 空列表返回提示
    if not obj_list:
        return "⚠️ 输入列表为空"
    # 提取表头（取第一个对象的所有key）
    headers = list(obj_list[0].keys())
    # 构建表格：表头 + 分隔线 + 内容行
    md = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |"
    ]
    # 遍历列表，生成内容行（处理列表/字典类型的值）
    for obj in obj_list:
        row = []
        for key in headers:
            val = obj.get(key, "无")  # 键不存在时显示“无”
            # 格式化列表/字典值为字符串
            if isinstance(val, (list, dict)):
                val_str = str(val).replace("[", "").replace("]", "").replace("{", "").replace("}", "")
            else:
                val_str = str(val)
            row.append(val_str)
        md.append("| " + " | ".join(row) + " |")
    return "\n".join(md)

# ---------------------- 使用示例 ----------------------
if __name__ == "__main__":
    # 模拟 list<object>（字典列表，每个字典是一个对象）
    user_list = [
        {"姓名": "张三", "年龄": 25, "技能": ["Python", "Markdown"], "职业": "工程师"},
        {"姓名": "李四", "年龄": 30, "技能": ["Java", "SQL"], "职业": "产品经理"},
        {"姓名": "王五", "年龄": 28, "技能": ["AI", "数据分析"], "职业": "算法工程师"}
    ]
    # 转换并打印（直接给大模型输出）
    md_table = list_obj_to_md_table(user_list)
    print(md_table)
    print("\n" + "-" * 50 + "\n")
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
    data_table = list_obj_to_md_table(data_list)
    print(data_table)