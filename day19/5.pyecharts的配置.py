"""
1、pyecharts全局配置
可以通过 .set_global_opts() 方法进行配置，主要针对通用配置进行设置，基本上是饼图、柱状图、折线图等都有的配置
例如：标题、图例、工具箱

"""
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Pie
# 引入标题
from pyecharts.options import TitleOpts
# 引入标题
from pyecharts.options import LegendOpts
# 引入标题
from pyecharts.options import ToolboxOpts
# 引入标题
from pyecharts.options import VisualMapOpts
# 引入标题
from pyecharts.options import TooltipOpts

Bar.set_global_opts(
    title_opts=TitleOpts("测试")
)
Line.set_global_opts()
Pie.set_global_opts()