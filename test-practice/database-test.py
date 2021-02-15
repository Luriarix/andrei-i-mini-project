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

def print_to_screen():
    sql = "SELECT id, name, price FROM products"
    cursor.execute(sql)
    for i in cursor.fetchall():
        print(f'id: {i[0]}    Name: {i[1]}    Price: {i[2]}')

def delete():
    sql = "DELETE FROM products WHERE id = %s"
    decizie = int(input('choose mofo:'))
    cursor.execute(sql,decizie)
    connection.commit()



def fieldNames():
    sql_test = "show fields from products"
    cursor.execute(sql_test)
    x = cursor.fetchall()
    return x

def print_to_screen_specific_prod(prod_id):
    sql = f"SELECT * FROM products WHERE id = {prod_id}"
    cursor.execute(sql)
    i = cursor.fetchone()
    print(f'1 id: {i[0]}    2 Name: {i[1]}    3 Price: {i[2]}')
    return i

def update_prod():
    z= 0
    field_names = []

    id_prod = int(input('choose a prod by id: '))
    prod = print_to_screen_specific_prod(id_prod)

    for item in fieldNames():
        field_names.append(item[0])

    category_to_change = int(input('Number of selected category to change: '))
    new_information = input('New info: ')


    sql = f"UPDATE products SET {field_names[category_to_change - 1]} = '{new_information}' WHERE id = {id_prod}"
    print(sql + '\n')
    print(id_prod)
    print(prod)
    # cursor.execute(sql)

def delete_specific_prod():
    id_prod = int(input('choose a prod by id: '))
    sql = f"DELETE from products where id =  {id_prod}"
    cursor.execute(sql)

print_to_screen()

update_prod()


print_to_screen()


cursor.close()
connection.close()