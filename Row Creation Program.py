'''
Program to generate the tables for the group project. This is written in Python to
make it easy to generate some random numbers, names, IDs, salaries, etc and export
all of these to a text file for an easy copy paste. I could make this a SQL file,
but I chose to keep it as a text file so that I can make easy edits where needed.
'''
import random
import string
import json

class Date():
	def __init__(self, year=1922, month=1, day=1):
		self.year = year
		self.month = month
		self.day = day

	def to_str(self):
		return f"{self.year}-{self.month:02d}-{self.day:02d}"

def GenerateGrade():
	return random.choice(["CNA", "LVN", "RN", "NP", "APRN"])

def GenerateSpecializations():
	specializations = ["Allergy and immunology", "Dermatology", "Diagnostic radiology", "Emergency medicine", "Internal medicine", "Neurology",
	                   "OBGYN", "Oncology", "Ophthalmology", "Pathology", "Pediatrics", "Rehabilitation", "Preventive medicine", "Psychiatry",
	                       "Urology"]
	return random.choices(specializations, k=random.randint(1,3))

def GenerateName():
	fname = random.choice(list(first_names.keys()))
	gender = 'F'
	if random.random() > first_names[fname]['gender']['F']:
		gender = 'M'
	lname = random.choice(last_names)
	return fname + " " + lname, gender

def GenerateAddress():
	street = random.choice(street_names)
	number = random.randint(1, 999)
	city = random.choice(cities)
	return f"{number} {street}, {city}, NJ"

def generate_random_int(length):
	return int(''.join(random.choices(string.digits, k=length)))

def GenerateEmployment(ENs):
	EN = generate_random_int(8)
	while EN in ENs:
		EN = generate_random_int(8)
	return EN

def GeneratePatientNumber(PNs):
	PN = generate_random_int(12)
	while PN in PNs:
		PN = generate_random_int(12)
	return PN

def GenerateSSN(SSNs):
	SSN = generate_random_int(9)
	while SSN in SSNs:
		SSN = generate_random_int(9)
	return SSN

def GeneratePhone():
	return generate_random_int(10)

def GenerateIllnesses():
	ret = []
	ills = []
	if random.random() < 0.3:
		ills.append(random.choice(list(illnesses.keys())))
	for ill in ills:
		ret.append(illnesses[ill])
	return list(set(ret))

def GenerateMedicineInfo():
	# quantity stored, quantity ordered, ytd usage
	return random.randint(1, 2000), random.randint(0, 1000), random.randint(0, 3000)

def GenerateOR():
	return random.randint(1, 100)

def GenerateRoom():
	return GenerateOR()

def GenerateDate(date=Date(), year=-1):
	if year == -1:
		year = random.randint(date.year, 2025)
	else:
		year = random.randint(year, 2025)
	month = random.randint(1, 12)
	if year == date.year and month < date.month:
		month = random.randint(date.month, 12)
	day = 1
	if year == date.year and month == date.month:
		day = date.day
	if month == 2:
		day = random.randint(day, 28)
	elif month in [4, 6, 9, 11]:
		day = random.randint(day, 30)
	else:
		day = random.randint(day, 31)
	return Date(year, month, day)

def GenerateTime(time=''):
	if time == '':
		return f"{random.randint(0,22):02d}:{random.randint(0,3)*15:02d}"
	hour = time.split(':')
	return f"{int(hour[0])+1:02d}:{random.randint(0,3)*15:02d}"

def GenerateSalary():
	return random.randint(25000, 300000)

def GenerateSurgeryID():
	return generate_random_int(10)

def GenerateBloodType():
	bts = ["A", "B", "AB", "O"]
	if random.random() > 0.5:
		return random.choice(bts) + "+"
	return random.choice(bts) + "-"

def GenerateBloodSugar():
	return random.randint(54, 300)

def GenerateHDL():
	return random.randint(30, 280)

def GenerateLDL():
	return random.randint(40, 220)

def GenerateTriglycerides():
	return int(random.normalvariate(150, 50))

def GenerateCorpCode(corp_codes):
	cc = generate_random_int(4)
	while cc in corp_codes:
		cc = generate_random_int(4)
	return cc

def GenerateHeadquarters():
	return random.choice(cities)

def GenerateSurgeryType(num_types=3):
	selected_surgeries = random.sample(surgery_types.items(), num_types)
	return selected_surgeries

def GenerateContracts(employment_number):
	specialization = GenerateSurgeryType(num_types=1)
	contract_type = "Surgery"
	contract_length = random.randint(5, 10)
	contract_start = GenerateDate(year=2020)

	return specialization, contract_type, contract_start, contract_length

def FindSurgeon(surgery_code, surgeons):
	spec = ''
	for surgery in surgery_types.keys():
		if surgery_types[surgery][2] == surgery_code:
			spec = surgery
			break
	possible_surgeons = []
	for surgeon in surgeons:
		if spec == surgeon.specialization:
			possible_surgeons.append(surgeon)

	return random.choice(possible_surgeons)

def FindNurses(surgery_code, nurses, clinic):
	spec = ''
	for surgery in surgery_types.keys():
		if surgery_types[surgery][2] == surgery_code:
			spec = surgery
			break
	possible_nurses = []
	for nurse in nurses:
		if spec in nurse.specializations:
			possible_nurses.append(nurse)

	return random.choices(possible_nurses, 2)

# ########################################################

class Personnel:
	def __init__(self, employment_numbers, SSNs, clinic):
		self.employment_number = GenerateEmployment(employment_numbers)
		self.name, self.gender = GenerateName()
		self.clinic = clinic
		self.address = GenerateAddress()
		self.phone = GeneratePhone()
		self.SSN = GenerateSSN(SSNs)
		self.salary = GenerateSalary()

	def to_sql_insert(self):
		salary = self.salary
		if salary == None:
			salary = "NULL"
		insert_statement = f"INSERT INTO Personnel (Employment_Number, Salary, Clinic, Name, Gender, Address, Phone, SSN) VALUES ({self.employment_number}, {salary}, '{self.clinic}', '{self.name}', '{self.gender}', '{self.address}', '{self.phone}', {self.SSN});"
		return insert_statement

class Nurse():
	def __init__(self, nurse):
		self.employment_number = nurse.employment_number
		self.grade = GenerateGrade()
		self.experience = random.randint(0, 40)
		self.clinic = nurse.clinic

		self.surgery_codes = GenerateSurgeryType()

	def to_sql_insert(self):
		insert_statement = f"INSERT INTO Nurse (Employment_Number, Grade, Years_Experience) VALUES ({self.employment_number}, '{self.grade}', {self.experience});"
		return insert_statement

class Physician():
	def __init__(self, physician):
		self.employment_number = physician.employment_number
		self.specializations = GenerateSpecializations()
		self.clinic = physician.clinic

	def to_sql_insert(self):
		insert_statement = f"INSERT INTO Physician (Employment_Number) VALUES ({self.employment_number});"
		return insert_statement

class Support_Staff():
	def __init__(self, support):
		self.employment_number = support.employment_number
		self.clinic = support.clinic

	def to_sql_insert(self):
		insert_statement = f"INSERT INTO Support_Staff (Employment_Number) VALUES ({self.employment_number});"
		return insert_statement

class Surgeon():
	def __init__(self, surgeon):
		self.employment_number = surgeon.employment_number
		surgeon.salary = None
		self.specialization, self.contract_type, self.contract_start, self.contract_length = GenerateContracts(self.employment_number)
		self.specialization = [item[0] for item in self.specialization][0]

	def to_sql_insert(self):
		insert_statement = f"INSERT INTO Surgeon (Employment_Number) VALUES ({self.employment_number});"
		insert_statement += f"\nINSERT INTO Surgeon_Contract (Employment_Number, Surgeon_Specialization, Contract_Type, Contract_Start_Date, Contract_Length) VALUES ({self.employment_number}, '{self.specialization}', '{self.contract_type}', '{self.contract_start.to_str()}', {self.contract_length});"
		return insert_statement

class Surgery_Schedule():
	def __init__(self, nurses, surgeons, clinic):
		self.surgery_ID = GenerateSurgeryID()
		self.OR = GenerateOR()
		self.surgery_code = GenerateSurgeryType(1)
		self.date = GenerateDate()
		self.time = GenerateTime()
		self.room_number = GenerateRoom()
		self.surgeon = FindSurgeon(self.surgery_code, surgeons)
		self.nurses = FindNurses(self.surgery_code, nurses, clinic)
		self.clinic = clinic

	def to_sql_insert(self):
		insert_statement = f"INSERT INTO Surgery_Schedule (Surgery_ID, Operating_Room, Surgery_Type_Code, Scheduled_Date, Scheduled_Time, Room_Number, Surgeon, Clinic) VALUES ({self.surgery_ID}, {self.OR}, {self.surgery_code}, '{self.date.to_str()}', '{self.time}', {self.room_number}, {self.surgeon.employment_number}, '{self.clinic}');"
		return insert_statement

class Patient():
	def __init__(self, patient_numbers, SSNs, clinic):
		self.patient_number = GeneratePatientNumber(patient_numbers)
		self.name, self.gender = GenerateName()
		self.address = GenerateAddress()
		self.dob = GenerateDate()
		self.phone = GeneratePhone()
		self.SSN = GenerateSSN(SSNs)
		self.blood_type = GenerateBloodType()
		self.blood_sugar = GenerateBloodSugar()
		self.HDL = GenerateHDL()
		self.LDL = GenerateLDL()
		self.triglycerides = GenerateTriglycerides()
		self.heart_disease_risk = self.HeartDiseaseRisk()
		self.admittances = []
		while random.random() < 0.2:
			self.admittances.append(Patient_Admittance(self.patient_number, clinic))
		patient_numbers.append(self.patient_number)
		self.illness = GenerateIllnesses()
		self.allergies = []
		while random.random() < 0.1:
			if len(self.allergies) == len(allergies):
				break			
			allergy = random.choice(allergies)
			while allergy in self.allergies:
				allergy = random.choice(allergies)
			self.allergies.append(allergy)

	def HeartDiseaseRisk(self):
		HDR = (self.HDL + self.LDL + self.triglycerides / 5) / self.HDL
		self.CR = HDR
		if HDR < 4:
			return 'N'
		elif HDR < 5:
			return 'L'
		return 'M'

	def to_sql_insert(self):
		# Prepare the SQL INSERT statement for the Patient table
		sql_insert1 = f"INSERT INTO Patient (Patient_Number, Name, Gender, Address, Date_of_Birth, Phone, SSN, Blood_Type, Blood_Sugar, HDL, LDL, Triglycerides, Heart_Disease_Risk) VALUES ({self.patient_number}, '{self.name}', '{self.gender}', '{self.address}', '{self.dob.to_str()}', '{self.phone}', {self.SSN}, '{self.blood_type}', {self.blood_sugar}, {self.HDL}, {self.LDL}, {self.triglycerides}, '{self.heart_disease_risk}');"

		# Include INSERT statements for Patient_Admittance
		sql_insert2 = []
		for admittance in self.admittances:
			sql_insert2.append(f"{admittance.to_sql_insert()}")
		sql_insert2 = "\n".join(sql_insert2)

		# Include INSERT statements for Patient_Illness
		sql_insert3 = []
		for illness_code in self.illness:
			sql_insert3.append(f"INSERT INTO Patient_Illness (Patient_Number, Illness_Code) VALUES ({self.patient_number}, {illness_code});")
		sql_insert3 = "\n".join(sql_insert3)

		# Include INSERT statements for Patient_Allergy
		allergy_codes = {allergy: idx for idx, allergy in enumerate(allergies)}
		sql_insert4 = []
		for allergy in self.allergies:
			allergy_code = allergy_codes[allergy]
			sql_insert4.append(f"INSERT INTO Patient_Allergy (Patient_Number, Allergy_Code) VALUES ({self.patient_number}, {allergy_code});")
		sql_insert4 = "\n".join(sql_insert4)

		return sql_insert1, sql_insert2, sql_insert3, sql_insert4

class Patient_Admittance():
	def __init__(self, patient_number, clinic):
		self.patient_number = patient_number
		self.DOA = GenerateDate(year=2010)
		self.check_out = GenerateDate(date=self.DOA)
		self.clinic = clinic
		self.nursing_unit = random.choice([1, 2, 3, 4, 5, 6, 7])
		self.wing = random.choice(["Blue", "Green"])
		self.room = GenerateRoom()
		self.bed = random.choice(['A', 'B'])

	def to_sql_insert(self):
		sql_insert = f"INSERT INTO Patient_Admittance (Patient_Number, Date_of_Admittance, Check_Out, Clinic, Nursing_Unit, Wing, Room_Number, Bed) VALUES ({self.patient_number}, '{self.DOA.to_str()}', '{self.check_out.to_str()}', '{self.clinic}', {self.nursing_unit}, '{self.wing}', {self.room}, '{self.bed}');"
		return sql_insert

class Medications():
	def __init__(self, medicines, medicine, med_code, clinics):
		self.name = medicine
		self.code = med_code
		self.cost = random.randint(1, 1000)

		self.clinic_info = {}
		for clinic in clinics:
			self.clinic_info[clinic] = {}
			stored, ordered, ytd = GenerateMedicineInfo()
			self.clinic_info[clinic]["stored"] = stored
			self.clinic_info[clinic]["ordered"] = ordered
			self.clinic_info[clinic]["ytd"] = ytd

		self.medicine_reactions = dict()
		for med in medicines:
			if medicine >= med:
				continue
			self.medicine_reactions[med] = random.choice(["N", "L", "M", "S"])

	def to_sql_insert(self, clinics):
		ret = []
		for clinic in clinics:
			ret.append(f"INSERT INTO Medication (Medication_Code, Clinic, Medication_Name, Quantity_Stored, Quantity_Ordered, Cost, YTD_Usage) VALUES ({self.code}, '{clinic}', '{self.name}', {self.clinic_info[clinic]['stored']}, {self.clinic_info[clinic]['ordered']}, {self.cost}, {self.clinic_info[clinic]['ytd']});")
		return "\n".join(ret)

class Corporation():
	def __init__(self, corp, corp_codes):
		self.name = corp
		self.code = GenerateCorpCode(corp_codes)
		self.hq = GenerateHeadquarters()

	def to_sql_insert(self):
		insert_statement = f"INSERT INTO Corporation (Corporation_Name, Corporation_Code, Headquarters) VALUES ('{self.name}', {self.code}, '{self.hq}');"
		return insert_statement

with open('first_names_modified.json', 'r') as file:
	first_names = json.load(file)

with open('last_names_set.json', 'r') as file:
	last_names = json.load(file)

with open('surgery_types.json', 'r') as file:
	surgery_types = json.load(file)

with open('Street Names.txt', 'r') as file:
	street_names = [line.strip() for line in file.readlines()]

with open('NJ Towns.txt', 'r') as file:
	cities = [line.strip() for line in file.readlines()]

with open('Medical Corporations.txt', 'r') as file:
	corps = [line.strip() for line in file.readlines()]

with open('Medicines.txt', 'r') as file:
	medicines = [line.strip() for line in file.readlines()]

with open('Allergies.txt', 'r') as file:
	allergies = [line.strip() for line in file.readlines()]

def Create_Personnel(clinics):
	ssns = []
	employment_numbers = []
	nurses = dict()
	physicians = dict()
	support = dict()
	surgeons = dict()
	personnel = dict()
	chiefs = dict()
	for clinic in clinics:
		nurses[clinic] = []
		personnel[clinic] = []
		for _ in range(200):
			nurse = Personnel(employment_numbers, ssns, clinic)
			ssns.append(nurse.SSN)
			employment_numbers.append(nurse.employment_number)
			personnel[clinic].append(nurse)
			nurses[clinic].append(Nurse(nurse))
		physicians[clinic] = []
		for _ in range(100):
			phys = Personnel(employment_numbers, ssns, clinic)
			ssns.append(phys.SSN)
			employment_numbers.append(phys.employment_number)
			personnel[clinic].append(phys)
			physicians[clinic].append(Physician(phys))
			if _ == 0:
				chiefs[clinic] = [phys.employment_number, 10]
		support[clinic] = []
		for _ in range(50):
			supp = Personnel(employment_numbers, ssns, clinic)
			ssns.append(supp.SSN)
			employment_numbers.append(supp.employment_number)
			personnel[clinic].append(supp)
			support[clinic].append(Support_Staff(supp))
		surgeons[clinic] = []
		for _ in range(50):
			surg = Personnel(employment_numbers, ssns, clinic)
			ssns.append(surg.SSN)
			employment_numbers.append(surg.employment_number)
			personnel[clinic].append(surg)
			surgeons[clinic].append(Surgeon(surg))

	return ssns, nurses, physicians, support, surgeons, personnel, chiefs

def Create_Patients(clinics, ssns):
	patients = dict()
	patient_numbers = []
	for clinic in clinics:
		print(clinic, "Patients started")
		patients[clinic] = []
		for _ in range(1000):
			pat = Patient(patient_numbers, ssns, clinic)
			ssns.append(pat.SSN)
			patient_numbers.append(pat.patient_number)
			patients[clinic].append(pat)
	return patients

def Create_Surgery_Schedule(nurses, surgeons, clinics):
	surgery_schedule = dict()
	for clinic in clinics:
		surgery_schedule[clinic] = []
		surgery_schedule[clinic].append(Surgery_Schedule(nurses[clinic], surgeons[clinic], clinic))
	return surgery_schedule

def Nurse_Patient(clinics, nurses, patients):
	np = dict()
	for clinic in clinics:
		np[clinic] = []
		for i in range(200):
			j = 5 * i
			np[clinic].append([nurses[clinic][i].employment_number, patients[clinic][j].patient_number])
			np[clinic].append([nurses[clinic][i].employment_number, patients[clinic][j+1].patient_number])
			np[clinic].append([nurses[clinic][i].employment_number, patients[clinic][j+2].patient_number])
			np[clinic].append([nurses[clinic][i].employment_number, patients[clinic][j+3].patient_number])
			np[clinic].append([nurses[clinic][i].employment_number, patients[clinic][j+4].patient_number])
	return np

def Physician_Patient(clinics, physicians, patients):
	np = dict()
	for clinic in clinics:
		np[clinic] = []
		for i in range(100):
			j = 10 * i
			np[clinic].append([physicians[clinic][i].employment_number, patients[clinic][j].patient_number])
			np[clinic].append([physicians[clinic][i].employment_number, patients[clinic][j+1].patient_number])
			np[clinic].append([physicians[clinic][i].employment_number, patients[clinic][j+2].patient_number])
			np[clinic].append([physicians[clinic][i].employment_number, patients[clinic][j+3].patient_number])
			np[clinic].append([physicians[clinic][i].employment_number, patients[clinic][j+4].patient_number])
			np[clinic].append([physicians[clinic][i].employment_number, patients[clinic][j+5].patient_number])
			np[clinic].append([physicians[clinic][i].employment_number, patients[clinic][j+6].patient_number])
			np[clinic].append([physicians[clinic][i].employment_number, patients[clinic][j+7].patient_number])
			np[clinic].append([physicians[clinic][i].employment_number, patients[clinic][j+8].patient_number])
			np[clinic].append([physicians[clinic][i].employment_number, patients[clinic][j+9].patient_number])
	return np

def Medicines(medicines, clinics):
	meds = dict()
	med_code = 0
	for medicine in medicines:
		med = Medications(medicines, medicine, med_code, clinics)
		meds[medicine] = med
		med_code += 1
	return meds

def Create_Corporations(clinics, corpos):
	corporations = dict()
	c_codes = []
	for corp in corpos:
		corporations[corp] = dict()
		c = Corporation(corp, c_codes)
		c_codes.append(c.code)
		corporations[corp]["info"] = c
		corporations[corp]["ownership"] = dict()
		for clinic in clinics:
			corporations[corp]["ownership"][clinic] = 5
	return corporations

def Consultations(physicians, patients, clinics):
	cons = []
	patient_medication = []
	for clinic in clinics:
		for patient in patients[clinic]:
			if random.random() < 0.6:
				phys = random.choice(physicians[clinic])
				start = GenerateTime()
				end = GenerateTime(start)
				date = GenerateDate(year=2020)
				consultation = f"{patient.patient_number}, {phys.employment_number}, '{date.to_str()}', '{start}', '{end}', '{clinic}'"
				cons.append(consultation)
				if random.random() < 0.8:
					pm = f"{patient.patient_number}, {phys.employment_number}, {random.randint(0, 248)}, {random.choice([1,2,3,4])}, '{random.choice(['daily', 'weekly', 'monthly'])}'"
					patient_medication.append(pm)
	return cons, patient_medication

if __name__ == "__main__":
	clinics = ["Clinic of Charles", "Clinic of Porter", "Clinic of Verghese", "Clinic of Dexter", "Clinic of Vivek"]
	illnesses= {"Acute Bronchitis": 0, "Common Cold": 1, "Ear Infection": 2, "Influenza": 3, "Sinusitis": 4, "Skin Infection": 5, "Sore Throat": 6, "UTI": 7}
	all_inserts = []
	
	ill_inserts = []
	for illness, code in illnesses.items():
		ill_inserts.append(f"INSERT INTO Illness (Illness_Code, Illness_Description) VALUES ({code}, '{illness}');")
	
	all_inserts.append("\n".join(ill_inserts))

	medications = Medicines(medicines, clinics)
	print("Medicines Done")
	medications_inserts = []
	reactions_inserts = []

	for med_name, med_instance in medications.items():
		medications_inserts.append(med_instance.to_sql_insert(clinics))

		# Medicine reactions
		for other_med, reaction in med_instance.medicine_reactions.items():
			reactions_inserts.append(f"INSERT INTO Medication_Reaction (Medication_1, Medication_2, Severity) VALUES ('{med_name}', '{other_med}', '{reaction}');")

	all_inserts.append("\n".join(medications_inserts))
	all_inserts.append("\n".join(reactions_inserts))

	ssns, nurses, physicians, support, surgeons, personnel, chiefs = Create_Personnel(clinics)
	print("Personnel Done")

	patients = Create_Patients(clinics, ssns)
	print("Patients Done")
	# SQL inserts for Patient
	patient_inserts = []
	patient_allergies = []
	patient_illnesses = []
	patient_admittances = []
	for clinic in clinics:
		for patient in patients[clinic]:
			pi1, pi2, pi3, pi4 = patient.to_sql_insert()
			if pi1:
				patient_inserts.append(pi1)
			if pi2:
				patient_admittances.append(pi2)
			if pi3:
				patient_illnesses.append(pi3)
			if pi4:
				patient_allergies.append(pi4)
	
	all_inserts.append("\n".join(patient_inserts))
	all_inserts.append("\n".join(patient_admittances))
	all_inserts.append("\n".join(patient_illnesses))
	all_inserts.append("\n".join(patient_allergies))

	# SQL inserts for Personnel
	personnel_inserts = []
	for clinic, pers_list in personnel.items():
		for pers in pers_list:
			personnel_inserts.append(pers.to_sql_insert())
	all_inserts.append("\n".join(personnel_inserts))

	# SQL inserts for Nurses
	nurse_inserts = []
	for clinic, nurse_list in nurses.items():
		for nurse in nurse_list:
			nurse_inserts.append(nurse.to_sql_insert())
	all_inserts.append("\n".join(nurse_inserts))

	# SQL inserts for Physicians
	physician_inserts = []
	for clinic, physician_list in physicians.items():
		for physician in physician_list:
			physician_inserts.append(physician.to_sql_insert())
	all_inserts.append("\n".join(physician_inserts))

	# SQL inserts for Support Staff
	support_inserts = []
	for clinic, support_list in support.items():
		for staff in support_list:
			support_inserts.append(staff.to_sql_insert())
	all_inserts.append("\n".join(support_inserts))

	# SQL inserts for Surgeons
	surgeon_inserts = []
	for clinic, surgeon_list in surgeons.items():
		for surgeon in surgeon_list:
			surgeon_inserts.append(surgeon.to_sql_insert())
	all_inserts.append("\n".join(surgeon_inserts))

	consultations, patient_medications = Consultations(physicians, patients, clinics)
	print("Consultations Done")
	consultation_inserts = []
	pms = []

	for cons in consultations:
		consultation_inserts.append(f"INSERT INTO Consultation (Patient_Number, Employment_Number, Date_of_Appointment, Start_Time, End_Time, Clinic) VALUES ({cons});")
		
	for pm in patient_medications:
		pms.append(f"INSERT INTO Patient_Medication (Patient_Number, Employment_Number, Medication_Code, Dosage, Frequency) VALUES ({pm});")

	all_inserts.append("\n".join(consultation_inserts))
	all_inserts.append("\n".join(pms))

	# SQL inserts for Chiefs
	ownership_inserts = []
	chief_inserts = []
	for clinic, chief_info in chiefs.items():
		employment_number, ownership_stake = chief_info
		chief_inserts.append(f"INSERT INTO Chief_Of_Staff (Clinic, Employment_Number) VALUES ('{clinic}', {employment_number});")

	# Insert into Ownership table for Chief of Staff
		chief_employment_number, chief_ownership_stake = chiefs[clinic]
		ownership_inserts.append(f"INSERT INTO Ownership (Owner_Code, Clinic, Percentage_Stake) VALUES ({chief_employment_number}, '{clinic}', {chief_ownership_stake});")
	all_inserts.append("\n".join(chief_inserts))

	corporation_inserts = []
	corporations = Create_Corporations(clinics, corps)
	print("Corporations Done")
	for corp, corp_data in corporations.items():
		corp_info = corp_data["info"]

		# Insert into Corporation table
		corporation_inserts.append(corp_info.to_sql_insert())

		for clinic in clinics:
			# Insert into Ownership table for Corporation
			ownership_inserts.append(f"INSERT INTO Ownership (Owner_Code, Clinic, Percentage_Stake) VALUES ({corp_info.code}, '{clinic}', {corp_data['ownership'][clinic]});")

	all_inserts.append("\n".join(corporation_inserts))
	all_inserts.append("\n".join(ownership_inserts))

	# SQL inserts for Nurse_Patient
	nurse_patient_relationships = Nurse_Patient(clinics, nurses, patients)
	print("Nurse Patient Done")
	nurse_patient_inserts = []
	for clinic, relationships in nurse_patient_relationships.items():
		for relationship in relationships:
			nurse_employment_number, patient_number = relationship
			nurse_patient_inserts.append(f"INSERT INTO Nurse_Patient (Employment_Number, Patient_Number, Clinic) VALUES ({nurse_employment_number}, {patient_number}, '{clinic}');")

	all_inserts.append("\n".join(nurse_patient_inserts))

	# SQL inserts for Physician_Patient
	physician_patient_relationships = Physician_Patient(clinics, physicians, patients)
	print("Physician Patient Done")
	physician_patient_inserts = []
	for clinic, relationships in physician_patient_relationships.items():
		for relationship in relationships:
			physician_employment_number, patient_number = relationship
			physician_patient_inserts.append(f"INSERT INTO Physician_Patient (Employment_Number, Patient_Number, Clinic) VALUES ({physician_employment_number}, {patient_number}, '{clinic}');")

	all_inserts.append("\n".join(physician_patient_inserts))

	surg_type_needs = []
	surg_type = []
	for st in list(surgery_types.keys()):
		surg_type.append(f"INSERT INTO Surgery_Type (Surgery_Type_Code, Name, Anatomical_Location, Patient_Category) VALUES ({surgery_types[st][2]}, '{st}', '{surgery_types[st][1]}', 'H');")
		surg_type_needs.append(f"INSERT INTO Surgery_Type_Special_Needs (Surgery_Type_Code, Special_Need) VALUES ({surgery_types[st][2]}, '{surgery_types[st][3]}');")
	all_inserts.append("\n".join(surg_type))
	all_inserts.append("\n".join(surg_type_needs))

	with open('Database Insert Statements.sql', 'w') as sql_file:
		sql_file.write("\n".join(all_inserts))

	print("Owari da.")