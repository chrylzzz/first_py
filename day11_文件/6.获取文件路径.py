"""
date 12/6/25
@author chryl

"""
import os

# 1. 获取当前文件的绝对路径（含文件名）
current_file_path = os.path.abspath(__file__)
print("当前文件绝对路径：", current_file_path)

# 2. 获取当前文件所在目录的路径
current_dir_path = os.path.dirname(os.path.abspath(__file__))
print("当前文件所在目录：", current_dir_path)

# 3. 拼接其他文件路径（常用：在当前目录下找子文件/文件夹）
target_file = os.path.join(current_dir_path, "test.txt")
print("拼接后的目标文件路径：", target_file)

print("-" * 100)

# 获取当前文件路径地址
def get_current_file_info():
    """
    获取当前 py 文件的路径信息
    :return: 字典，包含文件绝对路径、所在目录路径
    """
    file_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(file_path)
    return {
        "file_path": file_path,
        "dir_path": dir_path
    }


# 调用函数
info = get_current_file_info()
print(f"文件路径：{info['file_path']}")
print(f"目录路径：{info['dir_path']}")
