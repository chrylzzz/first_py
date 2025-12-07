from pyecharts.charts import Line
from pyecharts import options as opts

"""
pic,折线图数据样例
"""

# 准备数据
x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
y_data = [820, 932, 901, 934, 1290, 1330, 1320]

# 创建折线图对象并添加数据
line = (
    Line()
        .add_xaxis(x_data)  # 添加X轴数据
        .add_yaxis(
        "商家A",  # 系列名称，例如商家A的销售数据
        y_data,  # Y轴数据
        label_opts=opts.LabelOpts(is_show=False),  # 是否显示数据标签，这里选择不显示
    )
        .set_global_opts(  # 设置全局配置项
        title_opts=opts.TitleOpts(title="折线图示例"),  # 标题配置
        xaxis_opts=opts.AxisOpts(name="周"),  # X轴配置，这里可以设置X轴的名称
        yaxis_opts=opts.AxisOpts(name="数值"),  # Y轴配置，这里可以设置Y轴的名称
    )
)

# 渲染图表到文件
line.render(path="../echarts_file/chryl_test_line.html")
