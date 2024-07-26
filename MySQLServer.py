# MySQLServer.py

import mysql.connector

def create_database():
    try:
        # Establish a connection to the MySQL server
        cnx = mysql.connector.connect(
            user='your_username',
            password='your_password',
            host='your_host'
        )

        # Create a cursor object to execute SQL queries
        cursor = cnx.cursor()

        # Create the database if it doesn't exist
        query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        cursor.execute(query)

        # Print success message
        print("Database 'alx_book_store' created successfully!")

        # Close the cursor and connection
        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        # Print error message if connection fails
        print(f"Error: {err}")

if __name__ == "__main__":
    create_database()