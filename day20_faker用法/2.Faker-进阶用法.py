from faker import Faker

"""
2. 进阶：生成字典列表（模拟 list<object> 数据）

适合模拟接口返回、数据库数据等场景，每个字典对应一个 “对象”：
"""

# 初始化 Faker（默认英文数据，中文用 Faker('zh_CN')）
fake = Faker('zh_CN')  # 中文模拟数据

# 生成 4 个用户对象（每个对象是字典）
users = [
    {
        # 随机整数（1-100）
        "数字": fake.random_int(min=1, max=100),
        "姓名": fake.name(),
        "手机号": fake.phone_number(),
        "邮箱": fake.email(),
        "地址": fake.address(),
        "生日": fake.date_of_birth(),
        "手机号": fake.phone_number(),
        # 年龄区间
        "年龄": fake.random_int(min=18, max=60),
        # 布尔类型
        "布尔类型": fake.boolean(),
        # str_id 生成 8 位字母+数字混合的字符串 ID
        "字符串ID": fake.pystr(min_chars=8, max_chars=8),
        # alpha_id 生成 12 位纯字母字符串（只包含大小写字母）
        # "数字字母字符串": fake.pystr(min_chars=8, max_chars=8,
        #                              chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        # 生成 10 位纯数字字符串（本质是字符串类型的数字）
        "数字字符串": fake.numerify(text="##########"),  # 代表数字
        # 生成标准 UUID 字符串（36位，含连字符）
        "UUID": fake.uuid4(),  # 带 -
        # 生成不带连字符的 UUID 字符串
        "uuid_simple": fake.uuid4().replace("-", ""),  # 不带 -
        # 大写UUID
        "大写UUID": fake.uuid4().upper(),
        # 生成带业务前缀的字符串ID
        "order_": f'order_{fake.pystr(min_chars=8, max_chars=8)}',

    }
    for _ in range(4)
]

# 打印结果（模拟 list<object>）
for user in users:
    print(user)
