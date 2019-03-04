# This script, we want you to test out importing the data from hdfs
# into a pyspark dataframe

from pyspark.sql import SparkSession
 
spark = SparkSession.builder \
          .appName("simple-spark") \
          .getOrCreate()

start=datetime.now()
df = spark.read.csv('/data/casemix/casemix.csv')

df.show()
print (datetime.now()-start)

# Save the dataframe to csv on hdfs
# df.write.csv('/data/tmp_out/casemix.csv')

#####################################
# Save the dataframe to a Hive table

# Load the pyspark_hwc package into the env
# sc = spark.sparkContext
# sc.addPyFile("/usr/hdp/current/hive_warehouse_connector/pyspark_hwc-1.0.0.3.1.0.0-78.zip")

# from pyspark_llap import HiveWarehouseSession
# df.write.format(HiveWarehouseSession().HIVE_WAREHOUSE_CONNECTOR).option("table", 'moh_poc.test').save()
