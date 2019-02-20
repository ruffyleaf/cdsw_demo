# This script, we want you to test out importing the data from hdfs
# into a pyspark dataframe

from pyspark.sql import SparkSession
 
spark = SparkSession.builder \
          .appName("simple-spark") \
          .getOrCreate()
    
df = spark.read.csv('/data/casemix/casemix.csv')

df.show()