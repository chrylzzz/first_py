"""
文件和文件夹:
    os
"""
import os

# 文件/文件夹 重命名
# os.rename('1.c.txt', '10.c.txt')

# 文件/文件夹 删除
# os.remove('10.c.txt')

# 创建文件夹, 文件和文件夹不能重名
# os.mkdir('aa')

# 删除文件夹
# os.rmdir('aa')

# 获取当前目录:返回当前文件所在的目录
# getcwd = os.getcwd()
# print(getcwd)

# 改变默认目录:进入目录
# os.mkdir('bb')
# os.chdir('bb')
# os.mkdir('zz')

# 获取目录列表:获取文件夹下的所有文件,返回列表
listdir = os.listdir()
listdir2 = os.listdir('bb')
print(listdir)
print(listdir2)
