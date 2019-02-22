library(stringr)
library(sparklyr)
library(dplyr)

spark <- spark_connect(master = "yarn")

start_time <- Sys.time()
# load data from file in HDFS
casemix <- spark_read_csv(
  sc = spark,
  app_name = "cdsw-demo",
  name = "casemix",
  path = "/data/casemix/casemix.csv"
)

#display 10 rows of the spark R dataframe
head(casemix, 10)

end_time <- Sys.time()

end_time - start_time

spark_disconnect(spark)