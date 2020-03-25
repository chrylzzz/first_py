"""


"""


def user_info(name, age, gender):
    print(f'{name},{age},{gender}')


# 1.位置参数:和类型/数量/顺序等对应


# 2.关键字参数:可以指定数据的参数,不存在顺序的要求
user_info('Jms', gender='f', age=20)


# 并且 位置参数必须在关键字参数前面
# user_info(gender='f', age=20, 'Jms') #错误

def user_info2(name, age, gender='f'):
    print(f'{name},{age},{gender}')


# 3.缺省参数,函数定义时,给一个默认的数据,就可以不传或覆盖
user_info2('tom', 20)
user_info2('tom', 20, 'm')


# 4.不定长参数/可变参 ,返回的是元组
def user_info(*args):
    print(args)


user_info('tt', '22', "09ja")


# 5.包裹关键字参数 , 返回一个字典,组包的过程
def user_infoz(**kwargs):
    print(kwargs)


user_infoz(name='tt', age=20, id=110)
