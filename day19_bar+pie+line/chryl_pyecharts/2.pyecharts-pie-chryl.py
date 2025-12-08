from pyecharts.charts import Pie
from pyecharts import options as opts

"""
pic,饼图数据样例
"""

# 创建饼图对象
pie = Pie()

pie_categories = ['苹果', '香蕉', '橙子', '葡萄', '梨', '桃子']
pie_data = [10, 20, 30, 40, 50, 30]
# 添加数据
pie.add("", [list(z) for z in zip(pie_categories, pie_data)])

# 设置全局配置项
pie.set_global_opts(title_opts=opts.TitleOpts(title="水果销量", subtitle="副标题"))

# 设置系列配置项（例如：标签显示、是否突出显示等）
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

# 渲染图表到文件
pie.render(path="../echarts_file/chryl_test_pic.html")
