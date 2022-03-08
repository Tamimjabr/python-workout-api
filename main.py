from configs.sql_db_config import SqlDbConfig
from repositories.plans import Plans
from repositories.exercises import Exercises
from repositories.in_exercise_plan import InExercisePlan

exercises_repo = Exercises()
plans_repo = Plans()
in_exercise_plan_repo = InExercisePlan()
sql_db_config = SqlDbConfig(plans_repo, exercises_repo, in_exercise_plan_repo)
cursor = sql_db_config.connect_db()

# todo: to call from controller
print(in_exercise_plan_repo.list_exercises_in_plan(1))
print(in_exercise_plan_repo.list_equipments_needed_in_plan(1) )
print(in_exercise_plan_repo.list_percentage_of_body_parts_in_plan(1))
print('done')

