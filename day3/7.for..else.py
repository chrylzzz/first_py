"""
for 临时变量 in 序列:
    代码执行...
else:
    执行..        #循环结束之后要执行的代码
"""

for i in "cmcc":
    print("zzzzz")
    if i == 'm':
        break  # break时 else不执行
        continue  # else执行
else:
    print("???")
