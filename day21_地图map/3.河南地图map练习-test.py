from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
from pyecharts import options as opts
from pyecharts.globals import ThemeType

"""
地图可视化基本使用
河南地图:河南
"""
# 1. 创建地图实例（中国地图，深色主题）
map = Map(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="1600px", height="700px"))
# 注意:此处必须与地图的省和直辖市名字保持一致,包括省/市/自治区/特别行政区
# 格式：[(城市名, 确诊人数), ...]  河南省17个地级市全覆盖
henan_covid_data = [
    ("郑州市", 18560),
    ("洛阳市", 12430),
    ("南阳市", 10890),
    ("商丘市", 9570),
    ("周口市", 9250),
    ("驻马店市", 8980),
    ("信阳市", 8640),
    ("新乡市", 8230),
    ("安阳市", 7890),
    ("平顶山市", 7560),
    ("开封市", 7230),
    ("许昌市", 6980),
    ("濮阳市", 5870),
    ("三门峡市", 5230),
    ("漯河市", 4560),
    ("鹤壁市", 3890),
    ("济源市", 2150),
    ("焦作市", 3150)
]
# 添加数据时指定系列名
map.add(
    "模拟河南省新冠疫情",  # 对应 {a}
    henan_covid_data,  # 每个元组对应 {b}:{c}
    "河南")
# 全局选项
map.set_global_opts(
    # 热力图颜色配置（从浅到深，贴合疫情严重程度）
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 展示
        is_piecewise=True,  # 允许手动设置校准范围,分段
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "10-99人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "100-499人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "500-999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "1000-9999人", "color": "#CC3333"},
            {"min": 100000, "label": "10000以上", "color": "#990033"},
        ]
    ),
    # 图例配置（隐藏图例，热力图无需图例）
    legend_opts=opts.LegendOpts(is_show=False),
    # 设置全局配置（标题、图例、颜色）
    title_opts=opts.TitleOpts(
        title="河南省新冠疫情确诊人数热力图",
        subtitle="数据为模拟数据，仅作可视化演示",
        title_textstyle_opts=opts.TextStyleOpts(font_size=20, color="#fff")

    )
)

# 设置系列配置（鼠标悬浮显示详情）
map.set_series_opts(
    label_opts=opts.LabelOpts(is_show=True, color="#fff"),  # 显示省份名称（白色字体）
    tooltip_opts=opts.TooltipOpts(
        # 格式化提示框：自动匹配占位符
        # 1.占位符与数据的对应关系
        #     pyecharts 中，Map 图表的 data_pair 参数要求格式为 [(名称, 数值), ...]（也就是你传入的省份 - 确诊人数元组列表）。
        #     当你在 formatter 中写 {b} {c} 时，pyecharts 会按固定规则解析：
        # 2.占位符	含义	对应 data_pair 中的内容
        #     {b}	名称（name）	元组的第 0 位（如 "湖北" "广东"）
        #     {c}	数值（value）	元组的第 1 位（如 68320 23480）
        #     {a}	系列名（series name）	add() 方法中 series_name 的值（如 "新冠确诊人数"）
        formatter="省份：{b}<br/>确诊人数：{c}"  # 悬浮提示格式
    )
)

# 渲染图表到文件
map.render(path="./echarts_file/3chryl_test_map_henan.html")
print("热力图已生成，文件名为：河南省新冠疫情热力图(echarts_file/chryl_test_map_henan).html")
