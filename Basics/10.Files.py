from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'sample.txt'
file = file_location.open()

dd = open(file)

print(file.read())

print(file.readlines())