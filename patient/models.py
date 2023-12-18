from django.db import models
from django.forms import ModelForm
from datetime import date


class Staff(models.Model):
    employment_Number = models.DecimalField(max_digits=6, decimal_places=0)
    employee_Name = models.CharField(max_length=256)
    gender = models.CharField(
        max_length=1,
        choices = [

            ('M', 'M'),
            ('F','F'),
        ]
    )
    address = models.CharField(max_length=256)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    SSN = models.DecimalField(max_digits=9, decimal_places=0)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employee_type = models.CharField(
        max_length=2,
        choices = [

            ('DR', 'Doctor'),
            ('G', 'Surgeon'),
            ('N', 'Nurse'),
            ('ST', 'Staff'),
        ]
    )
    def __str__(self):
        return f"{self.employment_Number}"

class Patient(models.Model):
    patient_Number = models.DecimalField(max_digits=10, decimal_places=0)
    patient_Name = models.CharField(max_length=256)
    gender = models.CharField(
        max_length=1,
        choices = [

            ('M', 'M'),
            ('F','F'),
        ]
    )
    address = models.CharField(max_length=256)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    SSN = models.DecimalField(max_digits=9, decimal_places=0)
    Blood_Type = models.CharField(
        max_length=3,
        choices = [

            ('O+', 'O+'),
            ('O-', 'O-'),
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB+','AB+'),
        ]
    )
    Blood_Sugar = models.DecimalField(max_digits=5, decimal_places=3)
    HDL = models.DecimalField(max_digits=3, decimal_places=0)
    LDL = models.DecimalField(max_digits=3, decimal_places=0)
    Triglycerides =  models.DecimalField(max_digits=3, decimal_places=0)
    CR =  models.DecimalField(max_digits=3, decimal_places=2)
    Heart_Disease_Risk = models.CharField(max_length=8)
    illness_Desc = models.TextField()
    illness_Code_1 = models.DecimalField(max_digits=3, decimal_places=0)
    illness_Code_2 = models.DecimalField(max_digits=3, decimal_places=0)
    illness_Code_3 = models.DecimalField(max_digits=3, decimal_places=0)
    illness_Code_4 = models.DecimalField(max_digits=3, decimal_places=0)
    illness_Code_5 = models.DecimalField(max_digits=3, decimal_places=0)

    
    def __str__(self):
        return f"{self.patient_Number}"
    
    
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_Number', 'patient_Name', 'gender', 'address', 
                  'phone', 'SSN', 'Blood_Type', 'Blood_Sugar', 'HDL',
                    'LDL', 'Triglycerides', 'CR', 'Heart_Disease_Risk', 'illness_Desc',
                    'illness_Code_1', 'illness_Code_2', 'illness_Code_3', 
                    'illness_Code_4', 'illness_Code_5'
                    ]




class Consultation(models.Model):

    consultaion_Number = models.DecimalField(max_digits=9, decimal_places=0)
    employment_Number= models.ForeignKey(Staff, on_delete = models.CASCADE)
    start_Time = models.DateTimeField()
    end_Time = models.DateTimeField()



    
class ConsultationForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ['consultaion_Number', 'employment_Number', 'start_Time', 'end_Time']

class doctorSchedule(models.Model):

    employment_Number= models.ForeignKey(Staff, on_delete = models.CASCADE)
    patient_Number = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor_schedule_start = models.DateTimeField()
    doctor_schedule_end = models.DateTimeField()

class doctorScheduleForm(ModelForm):
    class Meta:
        model= doctorSchedule
        fields = ['employment_Number', 'patient_Number', 'doctor_schedule_start', 'doctor_schedule_end']



class room(models.Model):
    room_number = models.DecimalField(max_digits = 4, decimal_places = 0)
    room_avail_start = models.DateTimeField()
    room_avail_end = models.DateTimeField()

    def __str__(self):
        return f"{self.room_number} {self.room_avail_start} {self.room_avail_end}"

class roomCheck(ModelForm):
    class Meta:
        model = room
        fields = ['room_number', 'room_avail_start', 'room_avail_end']

class inpatientCare(models.Model):
    patient_Number = models.ForeignKey(Patient, on_delete = models.CASCADE)
    employment_Number = models.ForeignKey(Staff, on_delete = models.CASCADE)
    room = models.ForeignKey(room, on_delete = models.CASCADE)


class inPatientForm(ModelForm):
    class Meta:
        model = inpatientCare
        fields = ['patient_Number', 'employment_Number', 'room']

class surgery(models.Model):
    employment_Number = models.ForeignKey(Staff, on_delete = models.CASCADE)
    patient_Number = models.ForeignKey(Patient, on_delete = models.CASCADE)

    room = models.ForeignKey(room, on_delete = models.CASCADE)


class surgeryForm(ModelForm):
        class Meta:
            model = surgery
            fields = ['employment_Number', 'room']
    




        

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['employment_Number', 'employee_Name', 'gender',
        'address', 'phone', 'SSN', 'salary', 'employee_type'
    ]


class jobShift(models.Model):
   employment_Number = models.ForeignKey(Staff, on_delete = models.CASCADE)
  
   shift_start = models.DateTimeField()
   shift_end = models.DateTimeField()

class jobShiftForm(ModelForm):
        class Meta:
            model = jobShift
            fields = ['employment_Number', 'shift_start', 'shift_end']


