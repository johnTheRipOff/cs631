import json

with open('Surgery Types.txt', 'r') as file:
	lines = file.readlines()

surgery_types = {}

for line in lines:
	# Split the line at the first period
	parts = line.split('.', 1)

	key = parts[0].strip()
	value = parts[1].strip()
	surgery_types[key] = [value, "Eyes"]

with open('surgery_types.json', 'w') as json_file:
	json.dump(surgery_types, json_file, indent=2)
