import mysql.connector
from mysql.connector import Error
import os

def create_database_connection():
    """
    Establishes a connection to the MySQL server and returns the connection and cursor.
    Uses environment variables for sensitive data.
    """
    try:
        # Connect to MySQL server
        db = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),  # Use environment variables with default fallback
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'jaishreeram')  # Ideally, use an environment variable
        )
        
        # Create a cursor object
        cursor = db.cursor(buffered=True)
        
        print("Connection to MySQL server established.")
        return db, cursor
    
    except Error as err:
        print(f"Error: {err}")
        return None, None

def create_database(cursor, database_name):
    """
    Creates a database with the given name if it doesn't exist.
    """
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created or already exists.")
    except Error as err:
        print(f"Error: {err}")

def view_databases(cursor):
    """
    Retrieves and prints all databases.
    """
    try:
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("Databases:")
        for db in databases:
            print(db[0])
    except Error as err:
        print(f"Error: {err}")

def use_database(cursor, database_name):
    """
    Selects the specified database to be used.
    """
    try:
        cursor.execute(f"USE {database_name}")
        print(f"Using database '{database_name}'.")
    except Error as err:
        print(f"Error: {err}")

def delete_database(cursor, database_name):
    """
    Drops the specified database.
    """
    try:
        cursor.execute(f"DROP DATABASE IF EXISTS {database_name}")
        print(f"Database '{database_name}' deleted.")
    except Error as err:
        print(f"Error: {err}")

def close_connection(db, cursor):
    """
    Closes the cursor and database connection.
    """
    if cursor:
        cursor.close()
        print("Cursor closed.")
    if db:
        db.close()
        print("Database connection closed.")

