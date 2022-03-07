from configs.sql_db_config import SqlDbConfig

sql_db_config = SqlDbConfig()
cursor = sql_db_config.connect_db()
print('done')
