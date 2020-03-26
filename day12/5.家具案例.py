class Fur():
    def __init__(self, name, area):
        self.name = name
        self.area = area

    # def __str__(self):
    #     return f'家具名字:{self.name},家具面积:{self.area}'


class Home():
    # 这是构造方法,构造的时候传入参数
    def __init__(self, address, area):
        self.area = area
        self.address = address
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furs = []

    def __str__(self):
        return f'家具地址:{self.address},还剩下:{self.free_area},有那些家具:{self.furs}'

    def add_fur(self, item):
        # 该家具的面积  <=剩余的面积 ,可以添置
        if item.area <= self.free_area:
            # 这里注意为name,如果直接传入 item这个对象,好像item对象有_str_()方法也不toString
            self.furs.append(item.name)
            self.free_area -= item.area
        else:
            print('没地方啊')


fur = Fur('椅子', 10)
fur2 = Fur('桌子', 2)

home = Home('beij', 1000)
home.add_fur(fur)
home.add_fur(fur2)
print(home)
