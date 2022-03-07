def create_exercises_table(cursor):
    create_exercises_table_query = '''CREATE TABLE `exercises` (
            `id` INT PRIMARY KEY AUTO_INCREMENT,
            `name` VARCHAR(255) NOT NULL,
            `gifURL` VARCHAR(255) NOT NULL,
            `equipment_type` VARCHAR(255) NOT NULL,
            `body_part` VARCHAR(255) NOT NULL)'''
    cursor.execute(create_exercises_table_query)
    print('Created exercises table')
