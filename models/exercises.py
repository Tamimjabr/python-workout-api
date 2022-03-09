def create_exercises_table(cursor):
    create_exercises_table_query = '''CREATE TABLE `exercises` (
            `id` INT PRIMARY KEY AUTO_INCREMENT,
            `name` VARCHAR(255) NOT NULL,
            `gif_url` VARCHAR(255) NOT NULL,
            `equipment_type` VARCHAR(255) NOT NULL,
            `body_part` VARCHAR(255) NOT NULL)'''
    cursor.execute(create_exercises_table_query)
    print('Created exercises table')


def create_data_saver_view(cursor):
    # Remove gif url from exercises to save bandwidth
    create_data_saver_view_query = '''CREATE VIEW DataSaver
                                    AS SELECT id, name, equipment_type, body_part
                                    FROM exercises'''
    cursor.execute(create_data_saver_view_query)
    print('Created DataSaver view')
