from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
from .models import User, Patient, Appointment, Prescription
from .forms import UserCreateForm
from django.contrib.auth import get_user_model
custom_user_model = get_user_model()

class CustomUserAdmin(UserAdmin):

    model = User

    list_display = ("id",'email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_team',"is_doctor","is_recep")
    list_editable=["is_recep","is_doctor"]
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login',)

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('first_name','last_name','email',"is_recep","is_doctor")}),
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("id","doctor",'patient', 'date', 'symptoms', 'prescription')
    
    

admin.site.register(custom_user_model, CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Prescription,PrescriptionAdmin)