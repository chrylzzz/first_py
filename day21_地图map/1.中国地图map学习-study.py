"""
date 2025/12/7
@author chryl

全国地图:china
"""
from pyecharts import options as opts
from pyecharts.charts import Map

# 最简测试数据，用无歧义的直辖市+大省全称
data = [("北京市", 100), ("上海市", 90), ("广东省", 120), ("四川省", 80)]
# 生成地图
map_china = (
    Map(init_opts=opts.InitOpts(width="800px", height="600px"))
    .add(series_name="测试数据", data_pair=data, maptype="china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Mac 地图测试"),
        visualmap_opts=opts.VisualMapOpts(is_show=True, min_=50, max_=150)
    )
)
# 保存到echarts_file，路径简单易找
map_china.render("./echarts_file/1chryl_study_map.html")
