import os

flag = 2
# 批量文件重命名
os.chdir('bb/zz')
file_list = os.listdir()
print(file_list)

for name in file_list:
    # 添加指定字符
    if flag == 1:
        new_name = 'py_' + name
    # 删除指定字符
    elif flag == 2:
        num = len('py_')
        new_name = name[num:]
    else:
        break
    print(new_name)
    os.rename(name, new_name)
