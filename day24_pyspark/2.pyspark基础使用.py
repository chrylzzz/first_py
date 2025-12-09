"""
date 2025/12/9
@author chryl

构建PySpark执行环境入口对象,SparkContext是pyspark的唯一入口
想要使用PySpark库完成数据处理，首先需要构建一个执行环境入口对象。PySpark的执行环境入口对象是:类SparkContext 的类对象

"""
# 导包
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("chryl_spark_app")

# 基于Sparkconf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

# 打印PySpark的运行版本
print(sc.version)

# 停止Sparkcontext对象的运行(停止PySpark程序)
sc.stop()
