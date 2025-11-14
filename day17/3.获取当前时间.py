import datetime

# 获取当前日期时间对象
now = datetime.datetime.now()

# 格式化成年份+中文“年”+月份+中文“月”的形式
current_ym = now.strftime("%Y年%m月")

print(current_ym)  # 输出示例：2025年11月