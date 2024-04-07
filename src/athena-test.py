import boto3
import json
import time
from botocore.client import Config


def get_query_results(client, query_execution_id):
    for i in range(10):
        print(f"{i=}, {query_execution_id=}")
        query_details = client.get_query_execution(QueryExecutionId=query_execution_id)
        state = query_details["QueryExecution"]["Status"]["State"]
        if state == "SUCCEEDED":
            response_query_result = client.get_query_results(
                QueryExecutionId=query_execution_id
            )
            print(response_query_result)
            return response_query_result
        else:
            print(state)
        time.sleep(1)


def lambda_handler(_, __):
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
    sql: str = "insert into iceberg_table (id) values (CAST(? AS varchar));"

    # client = boto3.client("athena", config=Config(parameter_validation=False))
    client = boto3.client("athena")

    response = client.start_query_execution(
        QueryString=sql,
        QueryExecutionContext={
            "Database": "glue-database",
            "Catalog": "AwsDataCatalog",
        },
        WorkGroup="athena-test",
        ExecutionParameters=["1"],
    )

    query_execution_id = response["QueryExecutionId"]

    query_results = get_query_results(client, query_execution_id)

    if not query_results:
        client.stop_query_execution(QueryExecutionId=query_execution_id)

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
