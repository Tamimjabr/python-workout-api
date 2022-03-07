import mysql.connector
from mysql.connector import errorcode


class SQL_DB_Config:
    def __init__(self):
        self.cursor = None
        self.cnx = None
        self.DB_NAME = 'WORKOUT_DB'

    def connect_db(self):
        try:
            self.cnx = mysql.connector.connect(user='root', password='root', host='localhost')
            self.cursor = self.cnx.cursor()
            self.cursor.execute("USE {}".format(self.DB_NAME))
            print("Database {} is in use".format(self.DB_NAME))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                # todo create database
                print("Something is wrong with your user name or password")
        finally:
            return self.cursor
