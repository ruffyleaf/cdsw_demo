library(stringr)
library(sparklyr)
library(dplyr)

spark <- spark_connect(master = "yarn")

# load data from file in HDFS
casemix <- spark_read_csv(
  sc = spark,
  name = "casemix",
  path = "/data/casemix/casemix.csv"
)

#display 10 rows of the spark R dataframe
head(casemix, 10)