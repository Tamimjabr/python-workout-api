from flask_restful import Resource
from flask import request


class Plans(Resource):
    def __init__(self, plans_repo):
        self.plans_repo = plans_repo

    def get(self):
        plans = self.plans_repo.list_all_plans()
        return plans, 200


class ExercisesByPlanId(Resource):
    def __init__(self, in_exercise_plan_repo):
        self.in_exercise_plan_repo = in_exercise_plan_repo

    def get(self, plan_id):
        exercises = []
        if request.args.get('datasaver') == 'true':
            exercises = self.in_exercise_plan_repo.list_exercises_in_plan_data_saver_view(plan_id)
        else:
            exercises = self.in_exercise_plan_repo.list_exercises_in_plan(plan_id)

        return exercises, 200


class EquipmentsByPlanId(Resource):
    def __init__(self, in_exercise_plan_repo):
        self.in_exercise_plan_repo = in_exercise_plan_repo

    def get(self, plan_id):
        exercises = self.in_exercise_plan_repo.list_equipments_needed_in_plan(plan_id)

        return exercises, 200
