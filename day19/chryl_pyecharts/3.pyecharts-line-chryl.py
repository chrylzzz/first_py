from pyecharts.charts import Line
from pyecharts import options as opts

"""
pic,折线图数据样例
"""

# 准备数据
x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
y_data_A = [820, 932, 901, 934, 1290, 1330, 1320]
y_data_B = [220, 532, 501, 934, 6290, 1130, 1620]
y_data_C = [520, 332, 201, 134, 9290, 1230, 820]

# 创建折线图对象并添加数据
line = Line()

# 设置X轴
line.add_xaxis(x_data)  # 添加X轴数据,X轴是共用的,一个数据就可以了

# 设置Y轴
line.add_yaxis(
    "商家A",  # 系列名称，例如商家A的销售数据
    y_data_A,  # Y轴数据
    label_opts=opts.LabelOpts(is_show=False),  # 是否显示数据标签，这里选择不显示
)
line.add_yaxis(
    "商家B",  # 系列名称，例如商家B的销售数据
    y_data_B,  # Y轴数据
    label_opts=opts.LabelOpts(is_show=False),  # 是否显示数据标签，这里选择不显示
)
line.add_yaxis(
    "商家C",  # 系列名称，例如商家C的销售数据
    y_data_C,  # Y轴数据
    label_opts=opts.LabelOpts(is_show=False),  # 是否显示数据标签，这里选择不显示
)

# 设置全局变量
line.set_global_opts(  # 设置全局配置项
    title_opts=opts.TitleOpts(title="折线图示例", pos_left="center", pos_bottom="1%"),  # 标题配置
    xaxis_opts=opts.AxisOpts(name="周"),  # X轴配置，这里可以设置X轴的名称
    yaxis_opts=opts.AxisOpts(name="数值"),  # Y轴配置，这里可以设置Y轴的名称
)

# 渲染图表到文件
line.render(path="../echarts_file/chryl_test_line.html")
