
def create_plans_table(cursor):
    create_plans_table_query = '''CREATE TABLE `plans` (
            `id` INT PRIMARY KEY AUTO_INCREMENT,
            `name` VARCHAR(255) NOT NULL,
            `duration_minutes` INT NOT NULL)'''
    cursor.execute(create_plans_table_query)
    print('Created plans table')






