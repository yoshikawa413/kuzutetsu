import boto3
import json
import time
from botocore.client import Config


def lambda_handler(event, context):
    """

    CREATE TABLE iceberg_table (id bigint, data string)
    LOCATION 's3://your_bucket/data/'
    TBLPROPERTIES ( 'table_type' = 'ICEBERG' );

    Args:
        event (_type_): _description_
        context (_type_): _description_

    Returns:
        _type_: _description_
    """
    s3_bucket: str = "s3://your_bucket/"
    sql: str = "insert into iceberg_table (id) values (?);"

    # client = boto3.client("athena", config=Config(parameter_validation=False))
    client = boto3.client("athena")

    # ExecutionParameters は空文字を指定できないので、列指定から外す必要がある
    # string 型の場合、最小文字数が 1
    response = client.start_query_execution(
        QueryString=sql,
        QueryExecutionContext={"Database": "default"},
        ResultConfiguration={"OutputLocation": s3_bucket},
        ExecutionParameters=["1"],
    )

    query_execution_id = response["QueryExecutionId"]

    for i in range(10):
        print(f"{i=}, {query_execution_id=}")
        time.sleep(1)
        query_details = client.get_query_execution(QueryExecutionId=query_execution_id)
        state = query_details["QueryExecution"]["Status"]["State"]
        if state == "SUCCEEDED":
            response_query_result = client.get_query_results(
                QueryExecutionId=query_execution_id
            )
            print(response_query_result)
            break
        else:
            print(state)

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
