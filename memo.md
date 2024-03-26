# Athena

### キャパシティ関係

* https://aws.amazon.com/jp/blogs/news/introducing-athena-provisioned-capacity/
* https://repost.aws/ja/knowledge-center/athena-service-quota-errors

# Glue

* RDS Connection がつながらない
  * https://repost.aws/questions/QUpkrhcfkYQtS2adbjpQ7quQ/cannot-connect-from-glue-to-rds-postgres
      ```
      set password_encryption = 'md5';   
      CREATE USER "read_only_user" WITH ENCRYPTED PASSWORD 'my_super_password';
      GRANT pg_read_all_data TO read_only_user;
      ```

# Lambda

* psycopg2
  * バイナリをレイヤーにするときは Windows で作業せず、CloudShell を使う
      * zip ファイル作成
         ```
         pip install psycopg2-binary
         mkdir psycopg2-binary
         cd psycopg2-binary
         export LAYER=python/lib/python3.9/site-packages
         pip install -t $LAYER psycopg2-binary==2.9.9
         zip -r psycopg2-binary.zip python
         ```
      * Lambda レイヤーに追加
