from configs.sql_db_config import SqlDbConfig
from repositories.plans import Plans
from repositories.exercises import Exercises

exercises_repo = Exercises()
plans_repo = Plans()
sql_db_config = SqlDbConfig(plans_repo, exercises_repo)
cursor = sql_db_config.connect_db()
print('done')
