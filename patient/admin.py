from django.contrib import admin

from .models import Patient, Consultation, Staff, inpatientCare,room, doctorSchedule, jobShift, surgery


admin.site.register(Patient)
admin.site.register(Consultation)
admin.site.register(Staff)
admin.site.register(inpatientCare)
admin.site.register(room)
admin.site.register(doctorSchedule)
admin.site.register(jobShift)
admin.site.register(surgery)