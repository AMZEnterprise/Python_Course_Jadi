import mysql.connector

class Personnel:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

def print_personnels(personnels):
    for personnel in personnels:
        print("{} {} {}".format(personnel.name,
              personnel.weight, personnel.height))


cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='Learn')

cursor = cnx.cursor()

query = "SELECT * FROM Personnel ORDER BY Height DESC, Weight"
cursor.execute(query)

personnels = []

for (first_name, height, weight) in cursor:
    personnel = Personnel(first_name, weight, height)
    personnels.append(personnel)

print_personnels(personnels)