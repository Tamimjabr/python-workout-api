from helpers.file_reader import read_data_from_file


def insert_plans(cursor):
    plans = read_data_from_file('./data/exercise_plans.csv')
    plans_data = [tuple(row) for row in plans.values]

    insert_plans_query = '''INSERT INTO plans(
    name,
    duration_minutes) VALUES(%s, %s)'''

    for plan in plans_data:
        try:
            cursor.execute(insert_plans_query, plan)
        except Exception as e:
            print(e)

    print('Exercise plans inserted successfully')
