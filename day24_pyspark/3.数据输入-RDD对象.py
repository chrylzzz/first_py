"""
date 2025/12/9
@author chryl

RDD对象
如图可见,PySpark支持多种数据的输入,在输入完成后,都会得到一个:RDD类的对象
RDD全称为:弹性分布式数据集(Resilient Distributed Datasets)
PySpark针对数据的处理,都是以RDD对象作为载体,即:
    数据存储在RDD内
    各类数据的计算方法，也都是RDD的成员方法
    RDD的数据计算方法，返回值依旧是RDD对象

"""
