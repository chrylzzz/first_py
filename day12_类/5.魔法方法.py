"""
魔法方法
    __init__(): 构造方法,初始化对象,在创建对象时被默认调用
    __str__():  类似于toString,类似于说明的方法,必须有return
    __del__():  删除对象的时候调用
    __lt__():   小于符号比较方法
    __le__():   小于等于符号比较方法
    __eq__():   比较运算符号

"""


# 不带入参数的 init ,也可以直接在构造方法中直接定义变量并且赋值
class Person():
    # init 模仿方法
    def __init__(self):
        # 设置成员属性
        self.width = 100
        self.height = 200

    def get(self):
        print(f'Person: height:{self.height} , width:{self.width}')

    # str 魔法方法
    def __str__(self):
        return '[ __str__方法就是 .toString() ]'

    # del 魔法方法
    def __del__(self):
        print(f'Person 对象{self}被删除了')

    # lt 魔法方法,self 为当前类对象,other 为另一个类对象
    def __lt__(self, other):
        # 这里比较width
        return self.width < other.width

    # le 魔法方法,self 为当前类对象,other 为另一个类对象
    def __le__(self, other):
        return self.width <= other.width

    # eq 魔法方法,self 为当前类对象,other 为另一个类对象
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


person = Person()
# 调用get方法
person.get()
# toString方法
print("person: ", person)


# 带入参数的 init ,构造对象的时候进行赋值
class User():
    def __init__(self, width, height):
        # 设置成员属性
        self.width = width
        self.height = height

    def get(self):
        print(f'User: height:{self.height} , width:{self.width}')


# 在初始化的时候直接传输局
user = User(100, 600)
user.get()

# 比较方法 lt
print("比较方法lt:", person < user)
# print("比较方法:", user < person)  # 此处报错,因为user没有lt方法
# 比较方法 le
print("比较方法le:", person <= user)
# 比较方法 eq
print("比较方法eq:", person == user)
