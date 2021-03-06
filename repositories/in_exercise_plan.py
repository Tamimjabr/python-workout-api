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

    def list_exercises_in_plan(self, plan_id):
        list_exercises_in_plan_query = '''SELECT exercises.*
                                        FROM in_exercise_plan
                                        JOIN exercises ON in_exercise_plan.exercise_id = exercises.id
                                        WHERE in_exercise_plan.plan_id = {}'''.format(plan_id)
        self.cursor.execute(list_exercises_in_plan_query)
        return self.cursor.fetchall()

    def list_exercises_in_plan_data_saver_view(self, plan_id):
        list_exercises_in_plan_data_saver_view_query = '''SELECT DataSaver.* FROM DataSaver
                                                        JOIN in_exercise_plan ON in_exercise_plan.exercise_id = DataSaver.id
                                                        WHERE in_exercise_plan.plan_id = {}'''.format(plan_id)
        self.cursor.execute(list_exercises_in_plan_data_saver_view_query)
        return self.cursor.fetchall()

    def list_equipments_needed_in_plan(self, plan_id):
        list_equipments_needed_in_plan_query = '''SELECT DISTINCT exercises.equipment_type
                                                FROM in_exercise_plan
                                                JOIN exercises ON in_exercise_plan.exercise_id = exercises.id
                                                WHERE in_exercise_plan.plan_id = {}'''.format(plan_id)
        self.cursor.execute(list_equipments_needed_in_plan_query)
        equipments = self.cursor.fetchall()
        return equipments

    def list_percentage_of_body_parts_in_plan(self, plan_id):

        sum_of_exercises_in_plan_query = '''SELECT COUNT(exercises.id) AS total_exercises
                                            FROM exercises, in_exercise_plan
                                            WHERE in_exercise_plan.exercise_id = exercises.id
                                            AND in_exercise_plan.plan_id = {}'''.format(plan_id)

        list_percentage_of_body_parts_in_plan_query = '''SELECT separate_body_parts.part as body_part, separate_body_parts.Number_of_exercises,
                                                        ROUND((separate_body_parts.Number_of_exercises*100)/({}),2)as percentage
                                                        FROM( SELECT exercises.body_part as part,  COUNT(exercises.id) AS Number_of_exercises
                                                        FROM in_exercise_plan
                                                        JOIN exercises ON in_exercise_plan.exercise_id = exercises.id
                                                        WHERE in_exercise_plan.plan_id = {}
                                                        GROUP BY exercises.body_part) AS separate_body_parts'''.format(sum_of_exercises_in_plan_query, plan_id)

        self.cursor.execute(list_percentage_of_body_parts_in_plan_query)
        return self.cursor.fetchall()
