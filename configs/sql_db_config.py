import mysql.connector
from mysql.connector import errorcode
from models.plans import create_plans_table
from models.exercises import create_exercises_table
from models.in_exercise_plan import create_in_exercise_plan_table
from repositories.exercises import Exercise
from repositories.in_exercise_plan import insert_in_exercise_plan_relation
from repositories.plans import insert_plans


class SqlDbConfig:
    def __init__(self):
        self.cursor = None
        self.cnx = None
        self.DB_NAME = 'workout_db'

    def connect_db(self):
        try:
            print("Connecting to MySQL database...")
            self.cnx = mysql.connector.connect(user='root', password='tamim123', host='localhost')
            self.cursor = self.cnx.cursor()
            self.cursor.execute("USE {}".format(self.DB_NAME))
            print("Database {} is in use".format(self.DB_NAME))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_db()
                create_plans_table(self.cursor)
                create_exercises_table(self.cursor)
                create_in_exercise_plan_table(self.cursor)
                insert_plans(self.cursor)
                insert_in_exercise_plan_relation(self.cursor)
                self.cnx.commit()
            else:
                print(err.msg)
        finally:
            return self.cursor

    def create_db(self):
        self.cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
        self.cnx.database = self.DB_NAME
        print("Database {} is created".format(self.DB_NAME))
