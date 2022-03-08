import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='learn')

cursor = cnx.cursor()

cursor.execute("INSERT INTO People VALUES ('Ali', 'M',20)")
cursor.execute("INSERT INTO People VALUES ('Mahdi', 'M',50)")
cursor.execute("INSERT INTO People VALUES ('Sara', 'F',10)")

cnx.commit()

query = "SELECT * FROM People"
cursor.execute(query)

for (first_name, last_name, age) in cursor:
    print("{} {} is {} years old".format(first_name, last_name, age))

cnx.close()