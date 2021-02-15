import os
import pymysql
from dotenv import load_dotenv


load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()
