"""
类的里面和外面都可以添加属性
"""


class Person():
    def wash(self):
        print(self)

    def get(self):
        # 类里获取对象属性: self.属性名
        print(self.hei)


person = Person()
# 类外添加属性
person.width = 300
person.hei = 100

# 调用属性
print(person.hei)

# self 调用得到属性,先赋值再调用
person.get()
