from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("docregister", views.doctorregister, name="docregister"),   
    path("addpatient", views.addpatient, name="addpatient"),
    path("patients", views.patients, name="patients"),
    path("updatepatient/<int:patient_id>", views.updatepatient, name="updatepatient"),
    path("createappointment", views.createappointment, name="createappointment"),
    path("recepappoedit", views.recepappoedit, name="recepappoedit"),
    path("updateappointme/<int:appointment_id>", views.updateappointme, name="updateappointme"),
    path("removeappointme/<int:appointment_id>", views.removeappointme, name="removeappointme"),
    path("docappointmentview/", views.docappointmentview, name="docappointmentview"),
    path("patientview/<str:patient_name>", views.patientview, name="patientview"),
    path("modalview/<int:prescription_id>", views.modalview, name="modalview"),
    path("docpescrition/", views.docpescrition, name="docpescrition"),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)