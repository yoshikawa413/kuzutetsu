# Athena

### capacity

* https://aws.amazon.com/jp/blogs/news/introducing-athena-provisioned-capacity/
* https://repost.aws/ja/knowledge-center/athena-service-quota-errors

# Glue

* RDS Connection
    
    https://repost.aws/questions/QUpkrhcfkYQtS2adbjpQ7quQ/cannot-connect-from-glue-to-rds-postgres
    ```
    set password_encryption = 'md5';   
    CREATE USER "read_only_user" WITH ENCRYPTED PASSWORD 'my_super_password';
    GRANT pg_read_all_data TO read_only_user;
    ```

# Lambda

* psycopg2
    ```
    pip install psycopg2-binary
    mkdir psycopg2-binary
    cd psycopg2-binary
    export LAYER=python/lib/python3.9/site-packages
    pip install -t $LAYER psycopg2-binary==2.9.9
    zip -r psycopg2-binary.zip python
    ```

# Docker

```
$ echo "From amd64/amazonlinux" > Dockerfile
$ docker build ./ -t amazonlinux-arm64
$ docker run --rm -it --entrypoint bash --name amznlinux-arm64 --mount type=bind,source="$(pwd)"/target,target=/repositories amazonlinux-arm64
# python3 -m ensurepip --upgrade
# pip3 install psycopg2-binary
# mkdir psycopg2-binary
# cd psycopg2-binary
# export LAYER=python/lib/python3.9/site-packages
# pip3 install -t $LAYER psycopg2-binary==2.9.9
# yum install -y zip
# zip -r psycopg2-binary.zip python
# mv psycopg2-binary.zip /repositories/
# exit
$ aws s3 cp target/psycopg2-binary.zip s3://hogehoge/
```

```
docker run --rm -it --entrypoint bash --name amznlinux-arm64 --mount type=bind,source="$(pwd)"/target,target=/repositories multiarch/qemu-user-static
```

# RDS

### rds-data

https://aws.amazon.com/jp/blogs/database/using-the-data-api-to-interact-with-an-amazon-aurora-serverless-mysql-database/

```
aws rds-data execute-statement --resource-arn "arn:aws:rds:ap-northeast-1::cluster:" --secret-arn "arn:aws:secretsmanager:::" --sql "select * from hogehoge where no = ANY(string_to_array(:no, ','))" --database "postgres" --parameters '[{"name": "no", "value": {"stringValue": "10, 20"}}]' --region ap-northeast-1
```