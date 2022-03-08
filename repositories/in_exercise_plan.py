from helpers.file_reader import read_data_from_file


class InExercisePlan:
    def __init__(self):
        self.cursor = None

    def set_cursor(self, cursor):
        self.cursor = cursor

    def insert_in_exercise_plan_relation(self):
        in_exercise_plan = read_data_from_file('./data/exercises_plans_relations.csv')
        in_exercise_plan_data = [tuple(row) for row in in_exercise_plan.values]
        insert_in_exercise_plan_query = '''INSERT INTO in_exercise_plan(plan_id, exercise_id) VALUES(%s, %s)'''

        for relation in in_exercise_plan_data:
            try:
                self.cursor.execute(insert_in_exercise_plan_query, (int(relation[0]), int(relation[1])))
            except Exception as e:
                print(e)

        print('Plans were connected to their exercises successfully')
