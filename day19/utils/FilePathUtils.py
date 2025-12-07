"""
date 12/6/25
@author chryl

"""
import os
import sys


class FilePathUtils:
    """文件路径工具类，封装获取当前文件路径的方法"""

    @staticmethod
    def get_current_file_path():
        """获取当前 py 文件的绝对路径（含文件名）"""
        return os.path.abspath(__file__)

    @staticmethod
    def get_current_dir_path():
        """获取当前 py 文件所在目录的绝对路径"""
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def get_resource_path(relative_path):
        """
        获取资源文件路径（兼容 PyInstaller 打包后的 exe）
        :param relative_path: 相对当前文件的路径
        :return: 资源文件的绝对路径
        """
        if hasattr(sys, '_MEIPASS'):
            # 打包后使用临时目录
            return os.path.join(sys._MEIPASS, relative_path)
        # 未打包时使用当前文件目录
        return os.path.join(FilePathUtils.get_current_dir_path(), relative_path)


# -------------------------- 调用示例 --------------------------
if __name__ == '__main__':
    # 1. 直接通过类名调用，无需实例化
    file_path = FilePathUtils.get_current_file_path()
    dir_path = FilePathUtils.get_current_dir_path()
    # 拼接子文件路径（比如当前目录下的 test.txt）
    test_file_path = FilePathUtils.get_resource_path("test.txt")

    print(f"当前文件路径：{file_path}")
    print(f"当前目录路径：{dir_path}")
    print(f"测试文件路径：{test_file_path}")
