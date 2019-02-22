library(plyr)
library(doParallel)

numCores <- detectCores()
numCores

cl <- makeCluster(numCores)
registerDoParallel(cl)

# Use HDFS to import the file "casemix_procedure_part2.csv"
# This is the command - !hdfs dfs -get <path to hadoop>/<filename>

#create a dataframe
casemix <- read.csv("casemix_procedure_part2.csv")

system.time(ddply(casemix, .(proc_icd10), function(x) {
 Sys.sleep(2)
 nrow(x)
}))

system.time(ddply(casemix, .(proc_icd10), function(x) {
 Sys.sleep(2)
 nrow(x)
}, .parallel = TRUE))