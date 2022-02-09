import csv
# For the average
from statistics import mean


def calculate_averages(input_file_name, output_file_name):

    result = []

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))

            result.append([name, float(mean(these_grades))])

    writer = csv.writer(open(output_file_name, 'w', newline=''))
    writer.writerows(result)


def calculate_sorted_averages(input_file_name, output_file_name):

    result = []

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))

            result.append([name, float(mean(these_grades))])

    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1])

    writer = csv.writer(open(output_file_name, 'w', newline=''))
    writer.writerows(result)


def calculate_three_best(input_file_name, output_file_name):

    result = []

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))

            result.append([name, float(mean(these_grades))])

    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)

    writer = csv.writer(open(output_file_name, 'w', newline=''))
    writer.writerows(result[:3])


def calculate_three_worst(input_file_name, output_file_name):

    result = []

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))

            result.append([name, float(mean(these_grades))])

    result.sort(key=lambda x: x[1])
    
    writer = csv.writer(open(output_file_name, 'w', newline=''))

    worsts_result = result[:3]
    worsts_result_scores = []
    for item in worsts_result:
        worsts_result_scores.append([item[1]])
    
    writer.writerows(worsts_result_scores)


def calculate_average_of_averages(input_file_name, output_file_name):

    result = []

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))

            result.append([name, float(mean(these_grades))])

    writer = csv.writer(open(output_file_name, 'w', newline=''))

    averages = []
    for item in result:
        averages.append(item[1])

    writer.writerow([float(mean(averages))])

