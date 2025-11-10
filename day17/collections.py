# 定义包含字典的列表
data = [
    {"name": "张三", "age": 20},
    {"name": "李四", "age": 22},
    {"name": "王五", "age": 25}
]

# 提取所有"name"的值，用逗号拼接
names = [item["name"] for item in data]  # 列表推导式提取值
result = ",".join(names)  # 拼接成字符串

print(result)  # 输出：张三,李四,王五


#################################################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 定义包含对象的列表
people = [
    Person("张三", 20),
    Person("李四", 22),
    Person("王五", 25)
]

# 提取所有name属性，用逗号拼接
names = [p.name for p in people]
result = ",".join(names)

print(result)  # 输出：张三,李四,王五
#################################################
fruits = ["苹果", "香蕉", "橙子"]
result = ",".join(fruits)
print(result)  # 输出：苹果,香蕉,橙子