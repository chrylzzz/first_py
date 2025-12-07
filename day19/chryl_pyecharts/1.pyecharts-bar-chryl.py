from pyecharts.charts import Bar
from pyecharts import options as opts

"""
bar,柱状图数据样例
"""

# 准备数据
categories = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
data = [5, 20, 36, 10, 75, 90]

# 创建柱状图对象
bar = Bar()

# 添加 X 轴和 Y 轴数据
bar.add_xaxis(categories)
bar.add_yaxis("销量", data)

# 设置全局配置项
bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))

# 渲染图表到 HTML 文件
bar.render(path='../echarts_file/chryl_test_bar.html')
