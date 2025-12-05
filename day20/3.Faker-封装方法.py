from faker import Faker
from typing import List, Dict

"""
三、封装通用方法：批量生成模拟数据（类似 values() 效果）
"""


def generate_fake_data(
        field_map: Dict[str, str],
        count: int = 5,
        locale: str = 'zh_CN'
) -> List[Dict]:
    """
    批量生成模拟数据（字典列表）
    :param field_map: 字段映射 {字段名: Faker方法名}，如 {"姓名": "name", "手机号": "phone_number"}
    :param count: 生成数据条数
    :param locale: 语言区域（默认中文 'zh_CN'，英文 'en_US'）
    :return: 模拟数据字典列表
    """
    fake = Faker(locale)
    fake_data = []

    for _ in range(count):
        item = {}
        for field_name, method_name in field_map.items():
            # 获取 Faker 对应的方法并调用
            fake_method = getattr(fake, method_name, None)
            if fake_method:
                item[field_name] = fake_method()
            else:
                item[field_name] = f"无效方法：{method_name}"
        fake_data.append(item)

    return fake_data


# 调用示例：生成 3 条用户数据
field_map = {
    "用户ID": "random_int",
    "姓名": "name",
    "性别": "gender",
    "邮箱": "email",
    "地址": "address",
    "日期": "date",
    "手机号": "phone_number",
    "公司名": "company",
    "注册时间": "date_time_this_year",
    "文本": "text",
}
fake_users = generate_fake_data(field_map, count=3)

# 打印结果
for idx, user in enumerate(fake_users, 1):
    print(f"第{idx}条数据：{user}")
