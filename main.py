from configs.sql_db_config import SqlDbConfig
from repositories.plans import Plans


plans_repo = Plans()
sql_db_config = SqlDbConfig(plans_repo)
cursor = sql_db_config.connect_db()
print('done')
