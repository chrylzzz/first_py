from faker import Faker
"""
1. 基础：生成单个类型的模拟数据列表
"""
# 初始化 Faker（默认英文数据，中文用 Faker('zh_CN')）
fake = Faker('zh_CN')  # 中文模拟数据

# 生成 5 个姓名，组成列表（类似 "values()" 批量返回值）
names = [fake.name() for _ in range(5)]
print("姓名列表：", names)

# 生成 3 个手机号
phones = [fake.phone_number() for _ in range(3)]
print("手机号列表：", phones)
