"""
@author Chr.yl

"""
from stu_manger.student import *


class StudentManager(object):
    def __init__(self):
        # 存储 学员信息
        self.stus = []

    def run(self):
        # 自动加载:
        self.load_stu()
        while True:
            # 显示功能菜单
            self.show_menu()
            # 加载文件里的学院

            # 输入功能
            use_num = int(input('请输入功能: '))
            # 根据功能执行
            if use_num == 1:
                # 添加
                self.add_info()
            elif use_num == 2:
                # 删除
                self.del_info()
            elif use_num == 3:
                # 修改
                self.update_info()
            elif use_num == 4:
                # 查询名字
                self.find_info()
            elif use_num == 5:
                # 查所有
                self.show_infos()
            elif use_num == 7:
                # 保存学员信息
                self.save_stu()
            elif use_num == 8:
                # 加载存储的数据
                pass
                # self.load_stu()
            elif use_num == 6:
                flag = input('确定要退出吗? yes or no')
                if flag == 'yes':
                    break
            else:
                print('输入有误..')

    @staticmethod
    def show_menu():
        print('请选择功能:------------')
        print('1.添加')
        print('2.删除')
        print('3.修改')
        print('4.查询')
        print('5.显示所有')
        print('7.保存数据')
        print('8.手动加载数据')
        print('6.退出')
        print('-' * 20)

    # 添加 #pass为还没有写的时候,避免出错
    def add_info(self):
        """添加"""
        # pass
        new_id = input('输入学号:')
        new_name = input('输入姓名:')
        new_tel = input("输入手机号:")
        # 遍历 info
        for i in self.stus:
            # 用户名存在
            if new_name == i.name:
                print('用户已存在')
                return
        # 用户名不存在,添加
        student = Student(new_id, new_name, new_tel)
        self.stus.append(student)
        print(self.stus)

    # 删除
    def del_info(self):
        # 显示所有
        self.show_infos()
        this_id = str(input('请输入要删除的学生id:'))
        """删除"""
        for i in self.stus:
            if this_id == i.id:
                self.stus.remove(i)
                break
            else:
                print('查无此人')
        self.show_infos()

    # 修改
    def update_info(self):
        """修改"""
        self.show_infos()
        this_id = str(input('请输入要删除的学生id:'))

        for i in self.stus:
            if this_id == i.id:
                print(f'编号:{i.id},姓名:{i.name},电话:{i.tel}')
                this_name = input("请重新输入名字: ")
                this_tel = input("请重新输入手机号: ")
                i.name = this_name
                i.tel = this_tel
                break
        self.show_infos()

    # 查询
    def find_info(self):
        # 查询int或str
        this_name = input('请输入名字:')
        for i in self.stus:
            if this_name == i.name:
                print(f'编号:{i.id},姓名:{i.name},电话:{i.tel}')
                break
        else:
            print('您查询的名字不存在')

    # 显示所有
    def show_infos(self):
        """显示所有"""
        print(self.stus)
        for i in self.stus:
            print(f'编号:{i.id},姓名:{i.name},电话:{i.tel}')

    # 保存学员信息
    def save_stu(self):
        f = open('student.data', 'w')
        # 注意这里 列表推导式
        new_list = [i.__dict__ for i in self.stus]
        print(new_list)
        f.write(str(new_list))
        f.close()

    # 家在学员信息
    def load_stu(self):
        # 文件可能不存在
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # read 的为str
            data = f.read()
            # 转为列表[{},{}]
            new_list = eval(data)
            # 列表推导式
            self.stus = [Student(i["id"], i["name"], i["tel"]) for i in new_list]
        finally:
            f.close()
