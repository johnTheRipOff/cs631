-- <-- signifies this is done in the row creation program
PRAGMA foreign_keys=off;
ATTACH DATABASE 'Hospital.db' AS mydb;
PRAGMA foreign_keys=on;
--
CREATE TABLE IF NOT EXISTS Personnel (
    Employment_Number INTEGER PRIMARY KEY,
    Salary INTEGER CHECK (Salary BETWEEN 25000 AND 300000 OR Salary IS NULL),
    Clinic TEXT,
    Name TEXT,
    Gender TEXT,
    Address TEXT,
    Phone TEXT,
    SSN INTEGER
);
--
CREATE TABLE IF NOT EXISTS Nurse (
    Employment_Number INTEGER PRIMARY KEY,
    Grade TEXT,
    Years_Experience INTEGER,
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number)
);
--
CREATE TABLE IF NOT EXISTS Physician (
    Employment_Number INTEGER PRIMARY KEY,
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number)
);
--
CREATE TABLE IF NOT EXISTS Support_Staff (
    Employment_Number INTEGER PRIMARY KEY,
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number)
);
--
CREATE TABLE IF NOT EXISTS Surgeon (
    Employment_Number INTEGER PRIMARY KEY,
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number)
);
--
CREATE TABLE IF NOT EXISTS Physician_Specializations (
    Employment_Number INTEGER,
    Specialization TEXT,
    PRIMARY KEY (Employment_Number, Specialization),
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number)
);
--
CREATE TABLE IF NOT EXISTS Surgery_Schedule (
    Surgery_ID INTEGER PRIMARY KEY,
    Operating_Room INTEGER,
    Surgery_Type_Code INTEGER,
    Scheduled_Date TEXT,
    Scheduled_Time TEXT,
    Room_Number INTEGER,
    Surgeon INTEGER,
    Clinic TEXT,
    FOREIGN KEY (Surgeon) REFERENCES Personnel(Employment_Number),
    FOREIGN KEY (Clinic) REFERENCES Personnel(Employment_Number),
    FOREIGN KEY (Surgery_Type_Code) REFERENCES Surgery_Type(Surgery_Type_Code)
);
--
CREATE TABLE IF NOT EXISTS Nurse_Surgery_Schedule (
    Employment_Number INTEGER,
    Surgery_ID INTEGER,
    PRIMARY KEY (Employment_Number, Surgery_ID),
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number),
    FOREIGN KEY (Surgery_ID) REFERENCES Surgery_Schedule(Surgery_ID)
);
--
CREATE TABLE IF NOT EXISTS Patient (
    Patient_Number INTEGER PRIMARY KEY,
    Name TEXT,
    Gender TEXT,
    Address TEXT,
    Phone TEXT,
    SSN INTEGER,
    Date_of_Birth TEXT,
    Blood_Type TEXT,
    Blood_Sugar INTEGER,
    CR INTEGER,
    HDL INTEGER,
    LDL INTEGER,
    Triglycerides INTEGER,
    Heart_Disease_Risk TEXT
);
--
CREATE TABLE IF NOT EXISTS Patient_Admittance (
    Patient_Number INTEGER,
    Date_of_Admittance TEXT,
    Check_Out TEXT,
    Clinic TEXT,
    Nursing_Unit INTEGER,
    Wing TEXT,
    Room_Number INTEGER,
    Bed TEXT,
    PRIMARY KEY (Patient_Number, Date_of_Admittance),
    FOREIGN KEY (Patient_Number) REFERENCES Patient(Patient_Number)
);
--
CREATE TABLE IF NOT EXISTS Nurse_Patient (
    Employment_Number INTEGER,
    Patient_Number INTEGER,
    PRIMARY KEY (Employment_Number, Patient_Number),
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number),
    FOREIGN KEY (Patient_Number) REFERENCES Patient(Patient_Number)
);
--
CREATE TABLE IF NOT EXISTS Nurse_Surgery (
    Employment_Number INTEGER,
    Surgery_Type_Code INTEGER,
    PRIMARY KEY (Employment_Number, Surgery_Type_Code),
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number),
    FOREIGN KEY (Surgery_Type_Code) REFERENCES Surgery_Schedule(Surgery_Type_Code)
);
--
CREATE TABLE IF NOT EXISTS Physician_Patient (
    Employment_Number INTEGER,
    Patient_Number INTEGER,
    PRIMARY KEY (Employment_Number, Patient_Number),
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number),
    FOREIGN KEY (Patient_Number) REFERENCES Patient(Patient_Number)
);
--
CREATE TABLE IF NOT EXISTS Illness (
    Illness_Code INTEGER PRIMARY KEY,
    Illness_Description TEXT
);
--
CREATE TABLE IF NOT EXISTS Patient_Illness (
    Patient_Number INTEGER,
    Illness_Code INTEGER,
    PRIMARY KEY (Patient_Number, Illness_Code),
    FOREIGN KEY (Patient_Number) REFERENCES Patient(Patient_Number),
    FOREIGN KEY (Illness_Code) REFERENCES Illness(Illness_Code)
);

CREATE TABLE IF NOT EXISTS Consultation (
    Patient_Number INTEGER,
    Employment_Number INTEGER,
    Date_of_Appointment TEXT,
    Start_Time TEXT,
    End_Time TEXT,
    Clinic TEXT,
    PRIMARY KEY (Patient_Number, Employment_Number, Date_of_Appointment, Start_Time),
    FOREIGN KEY (Patient_Number) REFERENCES Patient(Patient_Number),
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number)
);
--
CREATE TABLE IF NOT EXISTS Patient_Allergy (
    Patient_Number INTEGER,
    Allergy_Code INTEGER,
    Allergy_Name TEXT,
    PRIMARY KEY (Patient_Number, Allergy_Code),
    FOREIGN KEY (Patient_Number) REFERENCES Patient(Patient_Number)
);
--
CREATE TABLE IF NOT EXISTS Medication (
    Medication_Code INTEGER,
    Clinic TEXT,
    Medication_Name TEXT,
    Quantity_Stored INTEGER,
    Quantity_Ordered INTEGER,
    Cost INTEGER,
    YTD_Usage INTEGER,
    PRIMARY KEY (Medication_Code, Clinic),
    FOREIGN KEY (Medication_Code) REFERENCES Medication(Medication_Code),
    FOREIGN KEY (Clinic) REFERENCES Personnel(Clinic)
);
--
CREATE TABLE IF NOT EXISTS Medication_Reaction (
    Medication_1 INTEGER,
    Medication_2 INTEGER,
    Severity TEXT,
    PRIMARY KEY (Medication_1, Medication_2),
    FOREIGN KEY (Medication_1) REFERENCES Medication(Medication_Code),
    FOREIGN KEY (Medication_2) REFERENCES Medication(Medication_Code),
);

CREATE TABLE IF NOT EXISTS Patient_Medication (
    Patient_Number INTEGER,
    Employment_Number INTEGER,
    Medication_Code INTEGER,
    Dosage INTEGER,
    Frequency INTEGER,
    PRIMARY KEY (Patient_Number, Employment_Number),
    FOREIGN KEY (Patient_Number) REFERENCES Patient(Patient_Number),
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number),
    FOREIGN KEY (Medication_Code) REFERENCES Medication(Medication_Code)
);
--
CREATE TABLE IF NOT EXISTS Corporation (
    Corporation_Name TEXT PRIMARY KEY,
    Corporation_Code INTEGER,
    Headquarters TEXT
);
--
CREATE TABLE IF NOT EXISTS Ownership (
    Owner_Code INTEGER,
    Clinic TEXT,
    Percentage_Stake DECIMAL(5, 2),
    PRIMARY KEY (Owner_Code, Clinic),
    FOREIGN KEY (Owner_Code) REFERENCES Physician(Employment_Number) CHECK (Owner_Code IN (SELECT Employment_Number FROM Physician)),
    FOREIGN KEY (Owner_Code) REFERENCES Corporation(Corporation_Code) CHECK (Owner_Code IN (SELECT Corporation_Code FROM Corporation))
);
--
CREATE TABLE IF NOT EXISTS Chief_Of_Staff (
    Clinic TEXT,
    Employment_Number INTEGER,
    PRIMARY KEY (Clinic, Employment_Number),
    FOREIGN KEY (Clinic) REFERENCES Personnel(Clinic),
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number)
);

-- CREATE TABLE IF NOT EXISTS Chief_Of_Staff_Patients (
--     Employment_Number INTEGER,
--     Patient_Number INTEGER,
--     PRIMARY KEY (Employment_Number, Patient_Number),
--     FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number),
--     FOREIGN KEY (Patient_Number) REFERENCES Personnel(Patient_Number)
-- );
--
CREATE TABLE IF NOT EXISTS Surgeon_Contract (
    Employment_Number INTEGER,
    Surgeon_Specialization TEXT,
    Contract_Type TEXT,
    Contract_Start_Date TEXT,
    Contract_Length INTEGER,
    PRIMARY KEY (Employment_Number, Surgeon_Specialization, Contract_Type, Contract_Start_Date),
    FOREIGN KEY (Employment_Number) REFERENCES Personnel(Employment_Number)
);
--
CREATE TABLE IF NOT EXISTS Surgery_Type (
    Surgery_Type_Code INTEGER PRIMARY KEY,
    Name TEXT,
    Anatomical_Location TEXT,
    Patient_Category TEXT
);
--
CREATE TABLE IF NOT EXISTS Surgery_Type_Special_Needs (
    Surgery_Type_Code INTEGER,
    Special_Need TEXT,
    PRIMARY KEY (Surgery_Type_Code, Special_Need),
    FOREIGN KEY (Surgery_Type_Code) REFERENCES Surgery_Type(Surgery_Type_Code)
);
--
CREATE TABLE IF NOT EXISTS Surgery_Skill (
    Surgery_Skill_Code INTEGER PRIMARY KEY,
    Description TEXT
);
--
CREATE TABLE IF NOT EXISTS Surgery_Type_Surgery_Skill (
    Surgery_Type_Code INTEGER,
    Surgery_Skill_Code INTEGER,
    PRIMARY KEY (Surgery_Type_Code, Surgery_Skill_Code),
    FOREIGN KEY (Surgery_Type_Code) REFERENCES Surgery_Type(Surgery_Type_Code),
    FOREIGN KEY (Surgery_Skill_Code) REFERENCES Surgery_Skill(Surgery_Skill_Code)
);

DETACH DATABASE mydb;