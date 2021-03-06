from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from configs.sql_db_config import SqlDbConfig
from controllers.workout_controller import Plans as PlansController, ExercisesByPlanId, EquipmentsByPlanId, BodyPartsByPlanId
from repositories.plans import Plans
from repositories.exercises import Exercises
from repositories.in_exercise_plan import InExercisePlan
import os


exercises_repo = Exercises()
plans_repo = Plans()
in_exercise_plan_repo = InExercisePlan()
sql_db_config = SqlDbConfig(plans_repo, exercises_repo, in_exercise_plan_repo)
sql_db_config.connect_db()

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


api.add_resource(PlansController, '/plans', resource_class_kwargs={'plans_repo': plans_repo})
api.add_resource(ExercisesByPlanId, '/plans/<int:plan_id>/exercises', resource_class_kwargs={'in_exercise_plan_repo': in_exercise_plan_repo})
api.add_resource(EquipmentsByPlanId, '/plans/<int:plan_id>/equipments', resource_class_kwargs={'in_exercise_plan_repo': in_exercise_plan_repo})
api.add_resource(BodyPartsByPlanId, '/plans/<int:plan_id>/body-parts', resource_class_kwargs={'in_exercise_plan_repo': in_exercise_plan_repo})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", 5000), host='0.0.0.0')


sql_db_config.close_database()
