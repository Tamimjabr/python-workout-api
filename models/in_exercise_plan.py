def create_in_exercise_plan_table(cursor):
    create_in_exercise_plan_table_query = '''CREATE TABLE `in_exercise_plan` (
            `plan_id` INT,
            `exercise_id` INT,
            PRIMARY KEY(plan_id, exercise_id),
            FOREIGN KEY(plan_id) REFERENCES plans(id) ON DELETE CASCADE,
            FOREIGN KEY(exercise_id) REFERENCES exercises(id) ON DELETE CASCADE)'''
    cursor.execute(create_in_exercise_plan_table_query)
    print('Created in_exercise_plan table')
