import json
import traceback
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from datetime import date

from . forms import AddPatientForm, UserCreateForm, CreateApointmentForm
from . models import Patient, User, Appointment,Prescription

def index(request):
    appointments = Appointment.objects.all().order_by("date","time")

    paginator = Paginator(appointments, 10)
    if request.GET.get("page") != None:
        try:
            appointments = paginator.page(request.GET.get("page"))
        except:
            appointments = paginator.page(1)
    else:
        appointments = paginator.page(1)
    context = {
        "appointments": appointments
    }
    return render(request, "ClinicMan/index.html", context)

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "ClinicMan/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "ClinicMan/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def doctorregister(request): 
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(user.password)
                user.is_doctor = True
                user.save()
            except IntegrityError:
                return render(request, "ClinicMan/docregister.html", {
                    "message": "Username already taken."
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreateForm()
    return render(request, "ClinicMan/docregister.html",{"form":form})

###########
#recepcionist view
###########

#patient edit
@login_required
def addpatient(request):
    if request.method == "POST":
        form = AddPatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            today = date.today()
            patient.age = today.year - patient.born.year - ((today.month, today.day) < (patient.born.month, patient.born.day))
            patient.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = AddPatientForm()
    return render(request, "ClinicMan/addpatient.html",{"form":form})

@login_required
def patients(request):
    patients = Patient.objects.all().order_by("name")
    #patient = Patient.objects.filter(name = patients)

    paginator = Paginator(patients, 10)
    if request.GET.get("page") != None:
        try:
            patients = paginator.page(request.GET.get("page"))
        except:
            patients = paginator.page(1)
    else:
        patients = paginator.page(1)
    context = {
        "patients": patients
    }
    return render(request, "ClinicMan/patients.html", context)

@csrf_exempt
@login_required
def updatepatient(request, patient_id = 0):
    try:
        patient = Patient.objects.get(id = patient_id)
    except Patient.DoesNotExist:
        return JsonResponse({"error": "Patient not found."}, status=404)
    if request.method == "POST":
        data = json.loads(request.body)
        patient.name = data["name"]
        patient.email = data["email"]
        patient.address = data["address"]
        patient.phone = data["phone"]
        patient.save()
        return JsonResponse({}, status=201)
    return JsonResponse({ "error": "GET or PUT request required." }, status=400)

#appointment edit
@login_required
def createappointment(request):
    if request.method == "POST":
        form = CreateApointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.status = True
            appointment.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CreateApointmentForm()
    return render(request, "ClinicMan/createappointment.html",{"form":form})

@login_required
def recepappoedit(request):
    appointments = Appointment.objects.all().order_by("date","time")
    users = User.objects.filter(is_doctor= True)

    paginator = Paginator(appointments, 10)
    if request.GET.get("page") != None:
        try:
            appointments = paginator.page(request.GET.get("page"))
        except:
            appointments = paginator.page(1)
    else:
        appointments = paginator.page(1)

    context = {
        "users":users,
        "appointments": appointments
    }
    return render(request, "ClinicMan/recepappoedit.html", context)

@csrf_exempt
@login_required
def updateappointme(request, appointment_id = 0):
    try:
        appointment = Appointment.objects.get(id = appointment_id)
    except Patient.DoesNotExist:
        return JsonResponse({"error": "Patient not found."}, status=404)
    if request.method == "POST":
        data = json.loads(request.body)
        doc_user = data["doctor"]
        user = User.objects.get(username = doc_user)
        appointment.doctor = user
        appointment.date = data["date"]
        appointment.time = data["time"]
        appointment.save()
        return JsonResponse({}, status=201)
    return JsonResponse({ "error": "GET or PUT request required." }, status=400)

def removeappointme(request, appointment_id):
    appointment = Appointment.objects.get(id = appointment_id)
    appointment.delete()
    return HttpResponseRedirect(reverse("recepappoedit"))

###########
#doctor's view
#################

@login_required
def docappointmentview(request):
    try:
        user = User.objects.get(username = request.user, is_doctor= True)
        appointments = Appointment.objects.filter(doctor = user).order_by("date","time")
        paginator = Paginator(appointments, 10)
        if request.GET.get("page") != None:
            try:
                appointments = paginator.page(request.GET.get("page"))
            except:
                appointments = paginator.page(1)
        else:
            appointments = paginator.page(1)
    except:
        return render(request, "ClinicMan/docappointmentview.html")
    context = {
        "user":user,
        "appointments": appointments,
    }
    return render(request, "ClinicMan/docappointmentview.html", context)

@login_required
def patientview(request,patient_name):
    try:
        patients = Patient.objects.get(name = patient_name)
        appointments = Appointment.objects.filter(patient = patients.id).order_by("date","time")
        prescriptions = Prescription.objects.filter(patient = patients.id)
        paginator = Paginator(appointments, 10)
        if request.GET.get("page") != None:
            try:
                appointments = paginator.page(request.GET.get("page"))
            except:
                appointments = paginator.page(1)
        else:
            appointments = paginator.page(1)
    except:
        return render(request, "ClinicMan/patientview.html")
    context = {
        "patients": patients,
        "appointments":appointments,
        "prescriptions":prescriptions,
    }
    return render(request, "ClinicMan/patientview.html", context)

def modalview(request, prescription_id):
    prescription = Prescription.objects.get(id = prescription_id)
    context={
        "prescription": prescription
    }
    return render(request, "ClinicMan/modalview.html", context)

@login_required
def docpescrition(request):
    if request.method == "POST":
        user = User.objects.get(username = request.user, is_doctor= True)   
        appointment = Appointment.objects.get(doctor = user, status = True)
        if user == appointment.doctor:
            prescription = Prescription(
                    doctor = user,
                    patient = appointment.patient,
                    symptoms = request.POST.get("symptoms"),
                    prescription = request.POST.get("prescription"),
            ) 
            prescription.save()
            appointment.status = False
            appointment.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        user = User.objects.get(username = request.user, is_doctor= True)
        appointments = Appointment.objects.filter(doctor = user)
        return render(request, "ClinicMan/docpescrition.html",{"user":user,"appointments":appointments })