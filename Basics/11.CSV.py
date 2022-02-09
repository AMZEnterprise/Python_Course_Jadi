import csv
from pathlib import Path
from statistics import mean

script_location = Path(__file__).absolute().parent
file_location = script_location / 'grades.csv'

with open(file_location) as f:
    reader = csv.reader(f)
    for row in reader:
        print(type(row))
        # print(row)

        # for grade in row[1:]:
        #     print(f'{name} got {grade}')

        name = row[0]
        these_grades = row[0]
        these_grades = list()
        for grade in row[1:]:
            these_grades.append(int(grade))
        # print(name,grade,these_grades)
        
        print("average of %s is %f" % (name, mean(these_grades)))