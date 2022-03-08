class Student:
    def __init__(self, age, height, weight):
        self.age = age 
        self.height = height
        self.weight = weight

class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def get_students_age_mean(self):
        return sum(student.age for student in self.students) / len(self.students)

    def get_students_height_mean(self):
        return sum(student.height for student in self.students) / len(self.students)

    def get_students_weight_mean(self):
        return sum(student.weight for student in self.students) / len(self.students)



schools = []
    
ages = []
heights = []
weights = []


for i in range(0,2):
    students_count = int(input())

    students = []

    for j in range(0,3):
        if j == 0:
            ages = input().split(' ')
        elif j == 1:
            heights = input().split(' ')
        elif j == 2:
            weights = input().split(' ')

    for k in range(0,students_count):
        students.append(Student(int(ages[k]), float(heights[k]), float(weights[k])))

    if i == 0:
        schools.append(School("A", students))
    elif i == 1:
        schools.append(School("B", students))

for school in schools:
    print("{}".format(school.get_students_age_mean()))
    print("{}".format(school.get_students_height_mean()))
    print("{}".format(school.get_students_weight_mean()))

best_school = None
best_school_height_mean = 0
best_school_weight_mean = 0

for school in schools:
    if school.get_students_height_mean() > best_school_height_mean:
        best_school_height_mean = school.get_students_height_mean()
        best_school_weight_mean = school.get_students_weight_mean()
        best_school = school
    elif school.get_students_height_mean() == best_school_height_mean:
        if school.get_students_weight_mean() > best_school_weight_mean:
            best_school_weight_mean = school.get_students_weight_mean()
            best_school = school
        elif school.get_students_weight_mean() == best_school_weight_mean:
            best_school = None

if best_school is not None:
    print(best_school.name)
else:
    print("Same")