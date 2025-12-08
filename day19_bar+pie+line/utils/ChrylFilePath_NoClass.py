"""
date 12/7/25
@author chryl

"""
"""
date 12/6/25
@author chryl

"""
import os


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


if __name__ == '__main__':
    # 调用函数
    info = get_current_file_info()
    print(f"文件路径 file_path：{info['file_path']}")
    print(f"目录路径 dir_path：{info['dir_path']}")
