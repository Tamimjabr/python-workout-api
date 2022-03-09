import json
from flask_restful import Resource


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
        exercises = self.in_exercise_plan_repo.list_exercises_in_plan(plan_id)
        return exercises, 200