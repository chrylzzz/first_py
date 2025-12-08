a = 'hello world'
b = "hello"
c = '''world'''
d = """owowow"""

############
f = 'u ' \
    'are see'
e = """i am 
chr"""
g = 'I\'m chr'  # 转义符号

print(a)
type(a)
print(b)
type(b)
print(c)
type(c)
print(d)
type(d)

print("------------")
###
print(f)  # 双引号换行会加 \ ,保持不换行的状态
print(e)  # 三引号换行了之后 ,输出也会换行
