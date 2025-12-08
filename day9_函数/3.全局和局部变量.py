a = 100


# 相当于声明了一个a=200的局部变量
def testA():
    a = 200


# global 为声明了全局变量a=200
def testB():
    global a
    a = 200


testA()
print(a)  # 100
testB()
print(a)  # 200
