"""
date 2025/12/8
@author chryl

"""
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

# 关闭到数据库的链接
conn.close()
