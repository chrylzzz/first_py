from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

"""
地图可视化基本使用
"""

map = Map()

map_data = [
    ("北京", 99),
    ("山东", 299),
    ("湖南", 299),
    ("上海", 199),
    ("新疆", 499),
    ("台湾", 299),
    ("南京", 199),
    ("广东", 299),
    ("吉林", 999),
    ("黑龙江", 1299),
    ("辽宁", 899),
]

map.add("测试地图", map_data, "china")
# 全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 展示
        is_piecewise=True,  # 允许手动设置校准范围
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "100-499人", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "500-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000以上", "color": "#990033"},
        ]
    )
)

# 渲染图表到文件
map.render(path="./echarts_file/chryl_test_map.html")
