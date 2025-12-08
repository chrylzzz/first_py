from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
from pyecharts import options as opts
from pyecharts.globals import ThemeType

"""
地图可视化基本使用
"""
# 1. 创建地图实例（中国地图，深色主题）
map = Map(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="1600px", height="700px"))
# 注意:此处必须与地图的省和直辖市名字保持一致,包括省/市/自治区/特别行政区
covid_data = [
    ("北京市", 11263),
    ("天津市", 897),
    ("河北省", 1542),
    ("山西省", 789),
    ("内蒙古自治区", 632),
    ("辽宁省", 1105),
    ("吉林省", 946),
    ("黑龙江省", 1028),
    ("上海市", 11487),
    ("江苏省", 1356),
    ("浙江省", 1219),
    ("安徽省", 983),
    ("福建省", 876),
    ("江西省", 751),
    ("山东省", 1422),
    ("河南省", 1678),
    ("湖北省", 63890),  # 重点省份，数据略高
    ("湖南省", 11054),
    ("广东省", 1765),
    ("广西壮族自治区", 834),
    ("海南省", 421),
    ("重庆市", 968),
    ("四川省", 1392),
    ("贵州省", 678),
    ("云南省", 895),
    ("西藏自治区", 123),  # 数据较低，贴合真实情况
    ("陕西省", 1017),
    ("甘肃省", 724),
    ("青海省", 356),
    ("宁夏回族自治区", 489),
    ("新疆维吾尔自治区", 765),
    ("香港特别行政区", 2143),
    ("澳门特别行政区", 189),
    ("台湾省", 1567)
]
# 添加数据时指定系列名
map.add(
    "模拟新冠疫情",  # 对应 {a}
    covid_data,  # 每个元组对应 {b}:{c}
    "china")
# 全局选项
map.set_global_opts(
    # 热力图颜色配置（从浅到深，贴合疫情严重程度）
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
    ),
    # 图例配置（隐藏图例，热力图无需图例）
    legend_opts=opts.LegendOpts(is_show=False),
    # 设置全局配置（标题、图例、颜色）
    title_opts=opts.TitleOpts(
        title="中国新冠疫情确诊人数热力图",
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
map.render(path="./echarts_file/chryl_test_map.html")
print("热力图已生成，文件名为：中国新冠疫情热力图(echarts_file/chryl_test_map).html")
