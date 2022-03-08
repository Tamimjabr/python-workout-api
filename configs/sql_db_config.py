import mysql.connector
from mysql.connector import errorcode
from models.plans import create_plans_table
from models.exercises import create_exercises_table
from models.in_exercise_plan import create_in_exercise_plan_table


class SqlDbConfig:
    def __init__(self, plans_repo, exercises_repo, in_exercise_plan_repo):
        self.plans_repo = plans_repo
        self.exercises_repo = exercises_repo
        self.in_exercise_plan_repo = in_exercise_plan_repo
        self.cnx = self.create_connection()
        self.cursor = self.create_cursor()
        self.DB_NAME = 'workout_db'

    def connect_db(self):
        try:
            self.cursor.execute("USE {}".format(self.DB_NAME))
            print("Database {} is in use".format(self.DB_NAME))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_db()
                create_plans_table(self.cursor)
                create_exercises_table(self.cursor)
                create_in_exercise_plan_table(self.cursor)
                self.exercises_repo.insert_exercises()
                self.plans_repo.insert_plans()
                self.in_exercise_plan_repo.insert_in_exercise_plan_relation()
                self.cnx.commit()
            else:
                print(err.msg)
        finally:
            return self.cursor

    def create_connection(self):
        try:
            print("Connecting to MySQL database...")
            return mysql.connector.connect(user='root', password='root', host='localhost')
        except Exception as err:
            print(err)
            exit(1)

    def create_cursor(self):
        cursor = self.cnx.cursor()
        self.plans_repo.set_cursor(cursor)
        self.exercises_repo.set_cursor(cursor)
        self.in_exercise_plan_repo.set_cursor(cursor)
        return cursor

    def create_db(self):
        self.cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
        self.cnx.database = self.DB_NAME
        print("Database {} is created".format(self.DB_NAME))
