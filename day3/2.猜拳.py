# 导入模块
import random

print("0--石头,1--剪刀,2--布")

player = int(input("请输入:"))

computer = random.randint(0, 2)  # 从0到2的区间

if (player == 0) and (computer == 1) or (player == 1) and (computer == 2) or (player == 2) and (computer == 0):
    print("win")
elif player == computer:
    print("bal")
else:
    print("fail")
print(computer)
