import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

dynamicFrame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://glue-test/targets/hoge/"]},
    format="json",
    # format_options={
    #     "jsonPath": "$..*"
    #     # "multiline": True,
    #     # "optimizePerformance": True, -> not compatible with jsonPath, multiline
    # }
)

mongo_options = {
    "connectionName": "docdb-conn",
    "database": "test3",
    "collection": "test3",
    "retryWrites": "false",
}

glueContext.write_dynamic_frame.from_options(
    dynamicFrame, connection_type="mongodb", connection_options=mongo_options
)

# glueContext.write_dynamic_frame.from_options(
#     frame=dynamicFrame,
#     connection_type="s3",
#     connection_options={"path": "s3://glue-test/"},
#     format="json"
# )

job.commit()
