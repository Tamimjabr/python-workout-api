from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from configs.sql_db_config import SqlDbConfig
from controllers.workout_controller import Plans as PlansController, ExercisesByPlanId
from repositories.plans import Plans
from repositories.exercises import Exercises
from repositories.in_exercise_plan import InExercisePlan

exercises_repo = Exercises()
plans_repo = Plans()
in_exercise_plan_repo = InExercisePlan()
sql_db_config = SqlDbConfig(plans_repo, exercises_repo, in_exercise_plan_repo)
sql_db_config.connect_db()

app = Flask(__name__)
api = Api(app)

# todo: to call from controller
print(in_exercise_plan_repo.list_exercises_in_plan(1))
print(in_exercise_plan_repo.list_equipments_needed_in_plan(1))
print(in_exercise_plan_repo.list_percentage_of_body_parts_in_plan(1))
print(plans_repo.list_all_plans())
print(in_exercise_plan_repo.list_exercises_in_plan_data_saver_view(2))
print('done')

api.add_resource(PlansController, '/plans', resource_class_kwargs={'plans_repo': plans_repo})
api.add_resource(ExercisesByPlanId, '/plans/<int:plan_id>/exercises', resource_class_kwargs={'in_exercise_plan_repo': in_exercise_plan_repo} )

if __name__ == '__main__':
    app.run(debug=True)
