with open('Street Names.txt', 'r') as file:
	lines = file.readlines()

cleaned_lines = sorted(list(set([line[:-5].strip() for line in lines])))

with open('Street Names.txt', 'w') as file:
	file.write('\n'.join(cleaned_lines))