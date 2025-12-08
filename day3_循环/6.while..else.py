i = 0
while i <= 5:
    print("gogogo")
    i += 1
    print(i)
    if i == 3:
        # break  # 不执行else
        continue  # 执行else
else:
    print("nonono")  # 循环结束要执行的
