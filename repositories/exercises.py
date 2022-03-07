from helpers.file_reader import read_data_from_file


def insert_exercises(cursor):
    exercises = read_data_from_file('./data/fitness_exercises.csv')
    exercises_data = [tuple(row) for row in exercises.values]

    insert_exercise_query = '''INSERT INTO exercises(
    body_part,
    equipment_type,
    gif_url,
    name) VALUES(%s, %s, %s, %s)'''

    for exercise in exercises_data:
        try:
            cursor.execute(insert_exercise_query, exercise)
        except Exception as e:
            print(e)

    print('Exercises inserted successfully')
