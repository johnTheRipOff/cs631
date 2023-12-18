import sqlite3
from pathlib import Path

def execute_create_table_statements(sql_file, conn):
	try:
		with open(sql_file, 'r') as file:
			sql_statements = file.read()

			# Execute all statements in the script
			cursor = conn.cursor()
			cursor.executescript(sql_statements)

			# Commit changes
			conn.commit()

			print("CREATE TABLE and INSERT statements executed successfully.")
	except sqlite3.IntegrityError as e:
		# Print the specific SQL statement causing the error
		print(f"Error executing CREATE TABLE and INSERT statements (Code {e.args[0]}): {e}")
		# If available, print the SQL statement causing the error
		statement_lines = sql_statements.split(';')
		for line in statement_lines:
			if e.args[0] in line:
				print(f"Problematic SQL statement: {line.strip()}")

# Connect to the SQLite database (creates a new database file if not exists)
conn = sqlite3.connect('HospitalDatabase.db')

# Specify the path to your SQL files
create_table_sql_file_path = Path('Database Design.sql')
insert_sql_file_path = Path('Database Insert Statements.sql')

# Execute CREATE TABLE and INSERT statements from the files
execute_create_table_statements(create_table_sql_file_path, conn)
execute_create_table_statements(insert_sql_file_path, conn)

# Close the connection
conn.close()
print("Done")
