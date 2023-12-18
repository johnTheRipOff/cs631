import json
import unicodedata

def is_ascii_letters(s):
	return all(65 <= ord(c) <= 122 for c in s if c.isalpha())

with open('last_names.json', 'r', encoding='utf-8') as file:
	data = json.load(file)

last_names_set = set()
total_names = 0

for name in data.keys():
	total_names += 1
	cleaned_name = ''.join(char for char in unicodedata.normalize('NFKD', name) if ord(char) < 128 and not unicodedata.combining(char))
	
	if is_ascii_letters(cleaned_name) and any(char.isalpha() for char in cleaned_name):
		if cleaned_name == "" or cleaned_name != cleaned_name.title() or not cleaned_name[0].isalpha() or '.' in cleaned_name or ' ' in cleaned_name or '-' in cleaned_name or len(cleaned_name) < 4 or len(cleaned_name) > 19:
			continue
		print(cleaned_name)
		last_names_set.add(cleaned_name.strip())

with open('last_names_set.json', 'w') as file:
	json.dump(list(last_names_set), file, indent=2)

print(f"\nProgram has completed. {total_names} last names in total, {len(last_names_set)} used in file.")