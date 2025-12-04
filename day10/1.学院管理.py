"""

"""


# 添加 #pass为还没有写的时候,避免出错
def add_info():
    """添加"""
    # pass
    new_id = input('输入学号:')
    new_name = input('输入姓名:')
    new_tel = input("输入手机号:")
    global info
    # 遍历 info
    for i in info:
        # 用户名存在
        if new_name == i['name']:
            print('用户已存在')
            return
    # 用户名不存在,添加
    info_dict = {}
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    info.append(info_dict)
    print(info)


# 删除
def del_info():
    # 显示所有
    show_infos()
    this_id = str(input('请输入要删除的学生id:'))
    """删除"""
    global info
    for i in info:
        if this_id == i['id']:
            info.remove(i)
            break
    show_infos()


# 修改
def update_info():
    """修改"""
    show_infos()
    this_id = str(input('请输入要删除的学生id:'))
    global info
    for i in info:
        if this_id == i['id']:
            print(f'编号:{i["id"]},姓名:{i["name"]},电话:{i["tel"]}')
            this_name = input("请重新输入名字: ")
            this_tel = input("请重新输入手机号: ")
            i['name'] = this_name
            i['tel'] = this_tel
            break
    show_infos()


# 查询
def find_info():
    this_name = input('请输入名字:')
    # 找到则为 true
    get_flag = False
    for i in info:
        if this_name in i['name']:
            print(f'编号:{i["id"]},姓名:{i["name"]},电话:{i["tel"]}')
            get_flag = True
            break
    if get_flag is False:
        print('您查询的名字不存在')


# 显示所有
def show_infos():
    """显示所有"""
    for i in info:
        print(f'编号:{i["id"]},姓名:{i["name"]},电话:{i["tel"]}')


def info_print():
    print('请选择功能:------------')
    print('1.添加')
    print('2.删除')
    print('3.修改')
    print('4.查询')
    print('5.显示所有')
    print('6.退出')
    print('-' * 20)


info = []

while True:
    # 显示功能
    info_print()
    # 输入
    use_num = int(input('输入功能: '))
    if use_num == 1:
        # 添加
        add_info()
    elif use_num == 2:
        # 删除
        del_info()
    elif use_num == 3:
        # 修改
        update_info()
    elif use_num == 4:
        # 查询名字
        find_info()
    elif use_num == 5:
        # 查所有
        show_infos()
    elif use_num == 6:
        flag = input('确定要退出吗? yes or no')
        if flag == 'yes':
            break
    else:
        print('输入有误..')
