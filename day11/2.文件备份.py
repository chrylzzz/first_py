"""
文件备份:
    组织备份的文件名
    数据写入

"""
old_name = input('输入文件名: ')
# 文件后缀下标
index = old_name.rfind('.')
# 判断文件是否有效
if index > 0:
    # 获得文件名 --切片
    file_old_name = old_name[:index]
    # 获得文件的后缀名
    file_old_type = old_name[index:]
# 新文件名字
new_name = file_old_name + '[备份]' + file_old_type

# 操作文件
# 打开旧文件  2进制打开
old_file = open(old_name, 'rb')
# 新建文件,写入新文件 ,注意循环,直到读完
new_file = open(new_name, 'wb')
while True:
    # 读
    con = old_file.read()
    # 是否读取结束
    if len(con) == 0:
        break
    # 写
    new_file.write(con)
# 关闭
old_file.close()
new_file.close()
