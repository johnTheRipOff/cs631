from .models import PatientForm, Consultation, Staff
from rest_framework import serializers


class PaitentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientForm
        fields = ["patient_Number", "patient_Name", "gender", "address", 
                  "phone", "SSN", "Blood_Type", "Blood_Sugar", "CR", "HDL",
                    "LDL", "Triglycerides", "Heart_Disease_Risk", "illness_Names",
                    "illness_Code_1", "illness_Code_2", "illness_Code_3", 
                    "illness_Code_4", "illness_Code_5"
                    ]


class ConsultationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consultation
        fields = ["consultaion_Number", "employment_Number", "start_Time", "end_Time"]

class StaffSerialzier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ['employment_Number', 'employee_Name', 'gender',
        'address', 'phone', 'SSN', 'salary', 'employee_type'
    ]