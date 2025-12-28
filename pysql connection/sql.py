import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

def get_db():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "springboard",
            port = 3306
        )
        
        if connection.is_connected():
            print("connection sucessful")
            return connection
    except Error as e:
        print("Error", e)
        return None
get_db()