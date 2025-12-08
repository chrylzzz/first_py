"""
    pyecharts全局配置
可以通过 .set_global_opts() 方法进行配置，主要针对通用配置进行设置，基本上是饼图、柱状图、折线图等都有的配置
例如：标题、图例、工具箱

"""
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Pie

"""
    pyecharts.options
为(pyecharts)中的可配置选项(options),使用时需要引入options
"""
# 标题    配置项
from pyecharts.options import TitleOpts
# 图例    配置项
from pyecharts.options import LegendOpts
# 工具箱   配置项
from pyecharts.options import ToolboxOpts
# 视觉映射   配置项
from pyecharts.options import VisualMapOpts
# 提示框   配置项
from pyecharts.options import TooltipOpts

"""
    Bar/Pie/Line 三种常用全局配置项
设置全局配置项
"""
# Bar.set_global_opts()
# Pie.set_global_opts()
# Line.set_global_opts()

line = Line()
# x轴
line.add_xaxis(["CN", "USA", "UK"])
# y轴
line.add_yaxis("GDP", [30, 35, 20])
# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True)
)
# 通过render()方法,生成图像
line.render(path="./echarts_file/chryl_global_opts.html")
