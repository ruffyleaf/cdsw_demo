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