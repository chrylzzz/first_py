from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

pie = Pie()

pie.add(
    "你好我是大饼图",
    [list(z) for z in zip(Faker.choose(), Faker.values())],
    center=["35%", "50%"],
)
pie.set_global_opts(
    title_opts=opts.TitleOpts(title="Pie-标题调整位置"),  # 标题
    legend_opts=opts.LegendOpts(pos_left="20%"),  # 类型展示位置
)
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# .render("pie_position（饼图）.html")
pie.render(path="./echarts_file/pie_position（饼图）.html")

# 一行代码创建pic
# c = (
#     Pie()
#         .add(
#         "你好我是大饼图",
#         [list(z) for z in zip(Faker.choose(), Faker.values())],
#         center=["35%", "50%"],
#     )
#         .set_global_opts(
#         title_opts=opts.TitleOpts(title="Pie-标题调整位置"),
#         legend_opts=opts.LegendOpts(pos_left="15%"),
#     )
#         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#         # .render("pie_position（饼图）.html")
#         .render(path="./echarts_file/pie_position（饼图）.html")
# )
