import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

line = Line()

line.add_xaxis(Faker.choose())
line.add_yaxis("商家A", Faker.values())
line.add_yaxis("商家B", Faker.values())
line.set_global_opts(
    title_opts=opts.TitleOpts(title="Line-基本示例", pos_left="center", pos_bottom="1%"),  # 标题配置
    xaxis_opts=opts.AxisOpts(name="X轴名称"),  # X轴配置，这里可以设置X轴的名称
    yaxis_opts=opts.AxisOpts(name="Y轴名称"),  # Y轴配置，这里可以设置Y轴的名称
)
# .render("line_base（折线图）.html")
line.render(path="./echarts_file/line_base（折线图）.html")

# 一行代码创建line
# c = (
#     Line()
#         .add_xaxis(Faker.choose())
#         .add_yaxis("商家A", Faker.values())
#         .add_yaxis("商家B", Faker.values())
#         .set_global_opts(
#         title_opts=opts.TitleOpts(title="Line-基本示例", pos_left="center", pos_bottom="1%"),  # 标题配置
#         xaxis_opts=opts.AxisOpts(name="X轴名称"),  # X轴配置，这里可以设置X轴的名称
#         yaxis_opts=opts.AxisOpts(name="Y轴名称"),  # Y轴配置，这里可以设置Y轴的名称
#     )
#         # .render("line_base（折线图）.html")
#         .render(path="./echarts_file/line_base（折线图）.html")
# )
