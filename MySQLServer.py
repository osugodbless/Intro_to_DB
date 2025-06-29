import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = connection.cursor()

    # Try creating the database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

except mysql.connector.Error as err:
    print("Error connecting to MySQL server:")
    print(err)

finally:
    # Clean up and close connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

