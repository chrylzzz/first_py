from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

"""
地图可视化基本使用
"""

map = Map()
# 注意:此处必须与地图的省和直辖市名字保持一致
map_data = [
    ("北京市", 99),
    ("山东省", 299),
    ("湖南省", 299),
    ("上海市", 199),
    ("新疆维吾尔自治区", 499),
    ("台湾省", 299),
    ("南京市", 199),
    ("广东省", 299),
    ("吉林省", 399),
    ("黑龙江省", 1299),
    ("辽宁省", 499),
    ("青海省", 679),
    ("西藏自治区", 389),
    ("重庆市", 589),
    ("四川省", 389),
    ("云南省", 89),
]

map.add("模拟新冠疫情", map_data, "china")
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
