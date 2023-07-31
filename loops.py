# Create SparkSession from builder
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType

spark = SparkSession.builder.master("local[1]") \
                    .appName('SparkByExamples.com') \
                    .getOrCreate()
                    

schema = StructType([
  StructField('firstname', StringType(), True),
  StructField('middlename', StringType(), True),
  StructField('lastname', StringType(), True)
  ])

# df = spark.createDataFrame([], schema)
# df.printSchema()
print(spark.sparkContext)
print("Spark App Name : "+ spark.sparkContext.appName)