import json
from flask_restful import Resource


class Workout(Resource):
    def __init__(self, plans_repo):
        self.plans_repo = plans_repo

    def get(self):
        plans = self.plans_repo.list_all_plans()
        return plans, 200
