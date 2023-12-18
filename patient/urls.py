from django.urls import path

from . import views

urlpatterns = [
    path('patientIntake', views.patientIntake, name='patientIntake'),
    path('consultationScheduler', views.consultationScheduler, name='consultationScheduler'),
    path('staffDirectory', views.staffDirectory, name='staffDirecotry'),
    path('inPatientCare', views.inPatientCare, name='inPatientCare'),
    path('roomChecker', views.roomChecker, name='roomChecker'),
    path('doctorSchedule', views.doctorSchedule, name='doctorSchedule'),
    path('jobShfit', views.jobShift, name='jobShiftViewer'),
    path('surgery',views.surgery, name='surgery')

]