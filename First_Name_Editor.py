import json
import unicodedata

def is_ascii(s):
	return all(
	    65 <= ord(c) <= 122 and unicodedata.category(c) not in ('Mn', 'Mc')
	    for c in s if c.isalpha()
	)

def remove_combining_characters(s):
	return ''.join(char for char in unicodedata.normalize('NFKD', s) if ord(char) < 128 and not unicodedata.combining(char))

with open('first_names.json', 'r', encoding='utf-8') as file:
	data = json.load(file)

cleaned_data = {}
total_names = 0
final_names = 0

for name, attributes in data.items():
	total_names += 1
	cleaned_name = remove_combining_characters(name)

	if is_ascii(cleaned_name) and any(char.isalpha() for char in cleaned_name):
		if cleaned_name == "" or cleaned_name != cleaned_name.title() or not cleaned_name[0].isalpha() or len(cleaned_name) < 4 or len(cleaned_name) > 19:
			continue

		print(cleaned_name)
		attributes.pop('country', None)
		attributes.pop('rank', None)

		gender = attributes.get('gender')
		if gender is not None:
			if "M" not in gender:
				gender["M"] = 0.0
			if "F" not in gender:
				gender["F"] = 0.0
		else:
			attributes['gender'] = {"F": 0.0, "M": 1.0}

		cleaned_data[cleaned_name.strip()] = attributes
		final_names += 1

with open('first_names_modified.json', 'w') as file:
	json.dump(cleaned_data, file, indent=2)

print(f"\nProgram has completed. {total_names} in total, {final_names} used in file.")