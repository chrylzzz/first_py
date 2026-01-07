"""
date 2026/1/7
@author chryl

三、zip() 与 enumerate() 结合使用
在复杂遍历场景中，可结合两者同时获取索引和多序列对应元素：

特性	        zip()	                    enumerate()
输入	        多个可迭代对象	            单个可迭代对象
输出元素	    各可迭代对象对应元素的元组	    (索引, 元素值) 的元组
核心用途	    多序列元素匹配打包	            遍历元素时获取索引
长度规则	    以最短序列为准截断	            与输入可迭代对象长度一致
"""
names = ["Alice", "Bob", "Jack Chen", "Jet Li"]
ages = [25, 30, 71]
scores = [90, 85]

# 同时获取索引和多序列元素
for idx, (name, age, score) in enumerate(zip(names, ages, scores), start=1):
    print(f"第 {idx} 位用户: {name}, {age} 岁, 成绩 {score}")
# 输出:
# 第 1 位用户: Alice, 25 岁, 成绩 90
# 第 2 位用户: Bob, 30 岁, 成绩 85
