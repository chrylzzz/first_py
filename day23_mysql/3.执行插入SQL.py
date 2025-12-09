"""
date 2025/12/8
@author chryl

执行非查询性质的SQL语句
    新增/删除数据等
"""
# 执行非查询性质的SQL语句
from pymysql import Connection
from faker import Faker

# 初始化 Faker（默认英文数据，中文用 Faker('zh_CN')）
fake = Faker('zh_CN')  # 中文模拟数据

# 获取到MySQL数据库的链接对象
conn = Connection(
    # host='localhost',  # 主机名(或IP地址)
    host='127.0.0.1',  # 主机名(或IP地址)
    port=3306,  # 端口，默认3306
    user='root',  # 账户名
    password='chryl',  # 密码
    # autocommit=True,  # 自动提交

)
# 打印MySQL数据库软件信息
# print(conn.get_server_info())
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("chryl")

# insert into user(id, user_name, user_password, user_date, is_admin) values ("e15886", "hmma", "123", "2025-12-08", TRUE)
# 动态参数（按字段顺序整理为元组）
params = (
    fake.uuid4().replace("-", ""),
    fake.name(),
    fake.password(),
    fake.date(),
    fake.boolean()
)

# 用 %s 作为占位符，不需要手动加引号
sql = (
    "INSERT INTO user(id, user_name, user_password, user_date, is_admin) "
    "VALUES (%s, %s, %s, %s, %s)"
)

# print("SQL 模板:", sql)
# print("SQL 参数:", params)

# 生成带真实参数的完整 SQL（自动处理引号、转义）
full_sql = cursor.mogrify(sql, params)
print("SQL 执行语句:", full_sql)

# insert
cursor.execute(sql, params)

# 提交, 也可以通过autocommit进行配置
conn.commit()
# 关闭到数据库的链接
conn.close()
