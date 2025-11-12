from datetime import datetime

date_str = "202511"

# 解析字符串为日期对象（指定格式为%Y%m，即年月日各占4、2位）
date_obj = datetime.strptime(date_str, "%Y%m")

# 格式化为“年月份”格式
result = date_obj.strftime("%Y年%m月")
print(result)  # 输出：2025年11月