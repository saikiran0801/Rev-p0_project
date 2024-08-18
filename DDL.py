def create_table(cursor, table_name, queries):
    """
    Creates a table with the specified name and SQL queries.
    """
    try:
        cursor.execute(queries)
        print(f"Table '{table_name}' created successfully.")
    except Error as err:
        print(f"Error: {err}")

def view_tables(cursor):
    """
    Retrieves and prints all tables in the current database.
    """
    try:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Tables:")
        for table in tables:
            print(table[0])
    except Error as err:
        print(f"Error: {err}")

def describe_table(cursor, table_name):
    """
    Retrieves and prints the structure of the specified table.
    """
    try:
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        print(f"Structure of table '{table_name}':")
        for column in columns:
            print(column)
    except Error as err:
        print(f"Error: {err}")

def alter_table(cursor, table_name, alter_query):
    try:
        cursor.execute(alter_query)
        print(f"Table '{table_name}' altered successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def drop_table(cursor, table_name):
    """
    Drops the specified table if it exists.
    """
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"Table '{table_name}' dropped successfully.")
    except Error as err:
        print(f"Error: {err}")

def truncate_table(cursor, table_name):
    """
    Truncates the specified table, removing all rows.
    """
    try:
        cursor.execute(f"TRUNCATE TABLE {table_name}")
        print(f"Table '{table_name}' truncated successfully.")
    except Error as err:
        print(f"Error: {err}")