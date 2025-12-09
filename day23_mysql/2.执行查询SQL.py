"""
date 2025/12/8
@author chryl

执行非查询性质的SQL语句
    新增/删除数据等
"""
# 执行非查询性质的SQL语句
from pymysql import Connection

# 获取到MySQL数据库的链接对象

conn = Connection(
    # host='localhost',  # 主机名(或IP地址)
    host='127.0.0.1',  # 主机名(或IP地址)
    port=3306,  # 端口，默认3306
    user='root',  # 账户名
    password='chryl',  # 密码

)
# 打印MySQL数据库软件信息
print(conn.get_server_info())
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("chryl")
# 查询数据
cursor.execute("select * from user")
# 查询结果
result: tuple = cursor.fetchall()
# 查看结果
for data in result:
    print(data)
# 关闭到数据库的链接
conn.close()
