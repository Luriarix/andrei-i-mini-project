import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor()
sql = "SELECT first_name,last_name,age FROM person"
cursor.execute(sql)
for i in cursor.fetchall():
    print(i)


connection.commit()
cursor.close()
connection.close()