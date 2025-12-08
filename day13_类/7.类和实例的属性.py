"""
类属性 :就是类所拥有的属性,归属于类,可以使用类访问和类对象访问
有点:始终保持一直的类可以用,为类提供的
    设置,
    访问,
    修改, 只能通过类对象修改,实例对象不能修改

实例属性:
"""


class Dog(object):
    # 类属性
    tooth = 10


##类属性
#########访问
# 类访问
print(Dog.tooth)
dog = Dog()
# 对象访问
print(dog.tooth)

#########修改
Dog.tooth = 20
print(Dog.tooth)
print(dog.tooth)
