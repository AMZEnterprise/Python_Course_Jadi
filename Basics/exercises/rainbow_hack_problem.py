import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    data = []

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            password_hash = row[1]
            data.append((name, password_hash))
    
    hash_dict = {}

    for i in range(1000,10000):
        hash_dict[hashlib.sha256(str(i).encode('utf-8')).hexdigest()] = i

    result = []

    for value in data:
        if value[1] in hash_dict:
            result.append([value[0], hash_dict[value[1]]])

    writer = csv.writer(open(output_file_name, 'w', newline=''))
    writer.writerows(result)
