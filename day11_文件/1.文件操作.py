"""

文件操作:
    打开:
        open(name,mode):name是要打开目录文件名的字符串.mode是打开文件的模式(读写追加)
    写:
        对象.write('内容')
    读:
        对象.read(num):num为从文件读取的数据长度,单位字节,默认读取所有数据
        对象.readlines():把文件中的内容一次性读取,并且返回列表,每一行数据为一个元素
        对象.readline():一次读取一行内容

    关闭:
        对象.close()

访问模式:
    主访问模式:
        1: r 读 ,w  写 ,a 追加
        2: w,r的文件指针会放在开头
        3: a的文件指针都在结尾
        4.其他访问模式都遵循与主访问模式
    但凡是带 b 的都是二进制
    但凡是带 + 的都是可读可写

改变文件指针位置:
    对象.seek(偏移量,起始位置):移动文件指针
        第二个参数:
        0 文件开头
        1 当前位置
        2 文件结尾


注意: w和a模式,如果文件不存在则创建,存在,w模式先清空在写入,a直接末尾追加
    r模式:如果文件不存在报错
"""
#  w 只写,文件不存在创建,会覆盖
# f = open('test.c.txt', 'w')
# f.write('aaa')
# f.close()

# r 只读,不存在报错,表示只读
# f2 = open('test1.c.txt', 'r')
# r只读,不能写入
# f2.write('zz#')
# f2.close()

# a 追加 ,不存在创建,不覆盖,只追加
# f3 = open('testz.c.txt', 'a')
# f3.write('aaa')
# f3.close()

# 访问模式默认为 r


#####################读
# read:注意换行符
# print('---------read')
# f = open('test.c.txt', 'r')
# # 换行符(\n)也是算在内,也算一个字节
# print(f.read(10))
# f.close()

# readlines :包含换行
# f2 = open('test.c.txt', 'r')
# content = f2.readlines()
# print(content)
# f2.close()

# readline :一次读一行,第二次调用就读第二行
# f3 = open('test.c.txt', 'r')
# content3 = f3.readline()
# content4 = f3.readline()
# print(content3)
# print(content4)
# f3.close()

##########seek()
print('--------seek')

f = open('test.c.txt', 'a+')
f.seek(0, 0)
con = f.read()
print(con)
f.close()
