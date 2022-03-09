from helpers.file_reader import read_data_from_file


class Plans:
    def __init__(self):
        self.cursor = None

    def set_cursor(self, cursor):
        self.cursor = cursor

    def insert_plans(self):
        plans = read_data_from_file('./data/exercise_plans.csv')
        plans_data = [tuple(row) for row in plans.values]

        insert_plans_query = '''INSERT INTO plans(
        name,
        duration_minutes) VALUES(%s, %s)'''

        for plan in plans_data:
            try:
                self.cursor.execute(insert_plans_query, plan)
            except Exception as e:
                print(e)

        print('Exercise plans inserted successfully')

    def list_all_plans(self):
        list_all_plans_query = '''SELECT id, name, duration_minutes
                                FROM plans'''

        self.cursor.execute(list_all_plans_query)
        return self.cursor.fetchall()
