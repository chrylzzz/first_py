
# 原始字典
data = {"name": "李四", "age": 30, "city": "北京", "skill": ["Python", "JSON"]}

# 定义重命名映射：{旧 key: 新 key}
rename_map = {
    "name": "姓名",
    "age": "年龄",
    "city": "城市",
    "skill": "技能"
}

# 方法1：字典推导式（一行完成批量重命名）
data_renamed = {rename_map.get(k, k): v for k, v in data.items()}

# 方法2：循环处理（适合需要额外逻辑的场景）
for old_key, new_key in rename_map.items():
    if old_key in data:
        data[new_key] = data.pop(old_key)  # pop() 取旧值并删除

print(data_renamed)  # 输出：{'姓名': '李四', '年龄': 30, '城市': '北京', '技能': ['Python', 'JSON']}
