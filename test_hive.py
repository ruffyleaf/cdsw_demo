from __future__ import print_function
import sys
from random import random
from operator import add
from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName("hive-warehouse-connector-test")\
    .getOrCreate()

sc = spark.sparkContext
sc.addPyFile("/usr/hdp/current/hive_warehouse_connector/pyspark_hwc-1.0.0.3.1.0.0-78.zip")

from pyspark_llap import HiveWarehouseSession

hive = HiveWarehouseSession.session(spark).build()
hive.executeQuery("select * from moh_poc.drugs_orc limit 10").show()