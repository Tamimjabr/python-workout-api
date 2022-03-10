import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import errorcode
from models.plans import create_plans_table
from models.exercises import create_exercises_table, create_data_saver_view
from models.in_exercise_plan import create_in_exercise_plan_table

load_dotenv()


class SqlDbConfig:
    def __init__(self, plans_repo, exercises_repo, in_exercise_plan_repo):
        self.plans_repo = plans_repo
        self.exercises_repo = exercises_repo
        self.in_exercise_plan_repo = in_exercise_plan_repo
        self.cnx = self.create_connection()
        self.cursor = self.create_cursor()

        self.DB_NAME = os.getenv('DB_NAME')

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
                create_data_saver_view(self.cursor)
                self.exercises_repo.insert_exercises()
                self.plans_repo.insert_plans()
                self.in_exercise_plan_repo.insert_in_exercise_plan_relation()
                self.cnx.commit()
            else:
                print(err.msg)


    def create_connection(self):
        try:
            print("Connecting to MySQL database...")
            return mysql.connector.connect(user=os.getenv('DB_USER'),
                                           password=os.getenv('DB_PASSWORD'),
                                           host=os.getenv('DB_HOST'))
        except Exception as err:
            print(err)
            exit(1)

    def create_cursor(self):
        cursor = self.cnx.cursor(dictionary=True)
        self.plans_repo.set_cursor(cursor)
        self.exercises_repo.set_cursor(cursor)
        self.in_exercise_plan_repo.set_cursor(cursor)
        return cursor

    def create_db(self):
        self.cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
        self.cnx.database = self.DB_NAME
        print("Database {} is created".format(self.DB_NAME))

    def close_database(self):
        self.cnx.close()
        self.cursor.close()
