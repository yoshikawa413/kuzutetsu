import json
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def lambda_handler(event, context):
    endpoint = "postgresql://xxx.ap-northeast-1.rds.amazonaws.com:5432"

    sql = "SELECT datname FROM pg_database WHERE datistemplate = false;"
    # sql = f"CREATE DATABASE test;"
    sql = """
    set password_encryption = 'md5';   
    CREATE USER "read_only_user" WITH ENCRYPTED PASSWORD '';  
    GRANT pg_read_all_data TO read_only_user;
    """

    conn = psycopg2.connect(endpoint)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql)
    # print(cur.fetchone())
    cur.close()
    conn.close()

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
