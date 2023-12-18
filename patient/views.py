from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import * #Patient, Consultation, PatientForm, ConsultationForm, Staff, StaffForm, inPatientForm, room, roomCheck, doctorSchedulerForm, docSchIDView, docSchCalView
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PaitentSerializer, ConsultationSerializer, StaffSerialzier


def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PatientForm()

    return render(request, 'patient/patientIntake.html', {'form': form})


def patientIntake(request): 
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PatientForm()

    return render(request, 'example_app/patientIntake.html', {'form': form})


def consultationScheduler(request): 
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ConsultationForm()

    return render(request, 'example_app/consultationScheduler.html', {'form': form})

def doctorSchedule(request): 
    if request.method == 'POST':
        form = doctorSchedule(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = doctorSchedule()

    return render(request, 'example_app/doctorScheduler.html', {'form': form})

def inPatientCare(request): 
    if request.method == 'POST':
        form = inPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = inPatientForm()

    return render(request, 'example_app/inPatientCare.html', {'form': form})

def roomChecker(request): 
    if request.method == 'POST':
        form = inPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = roomCheck()

    return render(request, 'example_app/roomCheck.html', {'form': form})



def staffDirectory(request): 
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StaffForm()

    return render(request, 'example_app/staffDirectory.html', {'form': form})

def jobShiftViewer(request): 
    if request.method == 'POST':
        form = jobShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = jobShiftForm()

    return render(request, 'example_app/jobShift.html', {'form': form})

def surgeryForm(request): 
    if request.method == 'POST':
        form = surgeryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = surgeryForm()

    return render(request, 'example_app/surgery.html', {'form': form})

class PaitentViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PaitentSerializer
    permission_classes = []


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = []

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerialzier
    permission_classes = []

