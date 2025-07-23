import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
connection = None
cursor = None

# Connect to MySQL server
try:
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    # Create cursor object
    cursor = connection.cursor()
    print("Connection established")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied: incorrect username or password")
    else:
        print(err)

# Create a database called 'alx_book_store'
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS john_book_store")
    print("Database created successfully")

except mysql.connector.Error as err:
    print(f"Failed to create database: {err}")

# Close database connection
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected():
        connection.close()
        print("Database connection is now closed")
