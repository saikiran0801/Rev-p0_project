from mysql.connector import Error

def execute_query(cursor, query, data=None):
    """
    Executes a given SQL query with optional data.
    """
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        print("Query executed successfully.")
    except Error as err:
        print(f"Error: {err}")

def insert_data(cursor, table_name, columns, values):
    """
    Inserts data into the specified table.
    """
    placeholders = ', '.join(['%s'] * len(values))
    columns_str = ', '.join(columns)
    query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
    execute_query(cursor, query, values)

def update_data(cursor, table_name, set_clause, condition):
    """
    Updates data in the specified table.
    """
    query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
    execute_query(cursor, query)

def delete_data(cursor, table_name, condition):
    """
    Deletes data from the specified table based on the condition.
    """
    query = f"DELETE FROM {table_name} WHERE {condition}"
    execute_query(cursor, query)

def select_data(cursor, table_name, columns='*', condition=None):
    """
    Selects and retrieves data from the specified table.
    """
    query = f"SELECT {columns} FROM {table_name}"
    if condition:
        query += f" WHERE {condition}"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as err:
        print(f"Error: {err}")
