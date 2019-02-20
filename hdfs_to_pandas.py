# This simple python file

# Imports the pandas package as "pd"
import pandas as pd

# run the following HDFS command to bring in the data from HDFS
# into the Workbench Session
# This brings data from hadoop into your local /tmp folder.
# Once you close the session, the datafile will be deleted from /tmp
!hdfs dfs -get /data/casemix/casemix.csv /tmp

# read in the file from tmp and create the pandas dataframe
file_path = "/tmp/casemix.csv"

df = pd.read_csv(file_path)

df.head()
