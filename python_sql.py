import mysql.connector
from mysql.connector import errors, errorcode
import os
from dotenv import load_dotenv
from datetime import date

# Load environment variables from a .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Initialize connection and cursor
connection = None
cursor = None

# Connect to MySQL server and execute queries
try:
    # Create a MySQLConnection object
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    print(connection)
    
    try:
        # Create a cursor object
        cursor = connection.cursor()
        
        # Variable store for SQL query
        create_book_table = """
        CREATE TABLE IF NOT EXISTS Books (
            book_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(130) NOT NULL,
            price DOUBLE,
            publication_date DATE
        )
        """
        
        # Create the Books table
        cursor.execute(create_book_table)
        
        # Get Books table schema (columns define in the Books table)
        cursor.execute("DESCRIBE Books")
        result = cursor.fetchall()
        for row in result:
            print(row)
            
        # Insert a new book into Books table
        sql = """
            INSERT INTO Books (title, price, publication_date)
            VALUES (%s, %s, %s)
        """
        data = ("Integrating Python with MySQL", 100.00, date(2025, 7, 19))
        
        cursor.execute(sql, data)
        
        # commit the changes
        connection.commit()
        print("Data committed successfully")
        
        # Retrieve all records in the Books table
        cursor.execute("SELECT * FROM Books")
        result = cursor.fetchall()
        print(result)
        
    except mysql.connector.Error as err:
        print(err)

# Handle specific programming-related MySQL errors during connection
except errors.ProgrammingError as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied: incorrect username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
        
finally:
    # Safely close cursor and connection if they were created
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected():
        connection.close()
