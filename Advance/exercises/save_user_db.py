import re
import mysql.connector

def check_email(email):
    reg = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$"
    if re.match(reg, email):
        return True
    else:
        return False

def check_password(password):
    reg = r"^[a-zA-Z0-9]+$"
    if re.match(reg, password):
        return True
    else:
        return False

def save_to_db(email, password):
    cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='Learn')
    cursor = cnx.cursor()
    insert_query = "INSERT INTO Users (Email, Password) VALUES (%s, %s)"
    record = (email, password)
    cursor.execute(insert_query, record)
    cnx.commit()

    print("User created successfully")

email = input("Enter your email: ")
while not check_email(email):
    print("Invalid email, correct format is : expression@string.string")
    email = input("Enter your email: ")

password = input("Enter your password: ")
while not check_password(password):
    print("Invalid password, correct format is : string and numbers (only a-z, A-Z, 0-9), don't use special characters.")
    password = input("Enter your password: ")

save_to_db(email, password)