from faker import Faker

"""
2. 进阶：生成字典列表（模拟 list<object> 数据）

适合模拟接口返回、数据库数据等场景，每个字典对应一个 “对象”：
"""

fake = Faker('zh_CN')

# 生成 4 个用户对象（每个对象是字典）
users = [
    {
        "id": fake.random_int(min=1, max=100),  # 随机整数（1-100）
        "name": fake.name(),
        "phone": fake.phone_number(),
        "email": fake.email(),
        "address": fake.address(),
        "生日": fake.date_of_birth(),
        "手机号": fake.phone_number(),
        "年龄": fake.random_int(min=18, max=60)  # 或通过生日计算真实年龄
    }
    for _ in range(4)
]

# 打印结果（模拟 list<object>）
for user in users:
    print(user)
