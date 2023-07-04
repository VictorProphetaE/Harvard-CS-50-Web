from django import forms
from django.contrib.auth import get_user
from datetime import datetime
from ClinicMan.models import User, Patient, Appointment,Prescription

from django.contrib.auth import get_user_model
custom_user_model = get_user_model()

GENDER = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other")
    ]
class MyDateInput(forms.widgets.DateInput):
    input_type = "date"
    
class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = custom_user_model
        fields = ["first_name","last_name","username","email","password1"]

    def clean(self):
        cleaned_data = super(UserCreateForm, self).clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("confirm_password")

        if password1 != password2:
            self.add_error("confirm_password", "Password does not match")

        return cleaned_data

class AddPatientForm(forms.ModelForm):
    datenow2 = datetime.now().date()
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={"placeholder": "Patient Name"}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Patient Email "}))
    gender = forms.ChoiceField(choices=GENDER, required=False, widget=forms.RadioSelect)
    address = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Patient Address "}))
    born = forms.DateField(widget=MyDateInput(attrs={"type": "date", "min":"1918-01-01","max": datenow2 }))
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Patient Phone max. 10 digits "}))

    class Meta:
        model = Patient
        fields = ["name","email","gender","born","phone","address"]

class CreateApointmentForm(forms.ModelForm):
    time = forms.TimeField(widget=MyDateInput(attrs={"type": "time"}))
    datenow = datetime.now().date()
    date = forms.DateField(widget=MyDateInput(attrs={"type": "date", "min": datenow ,"max":"2025-01-01" }))

    class Meta:
        model = Appointment
        fields = ["patient","doctor","date","time"]

    def __init__(self, *args, **kwargs):
        super(CreateApointmentForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields["patient"].queryset = Patient.objects.all()
            self.fields["doctor"].queryset = User.objects.filter(is_doctor= True)
            self.fields["date"].label = "Date (DD-MM-YYYY)"
            self.fields["time"].label = "Time 24 hr (HH:MM)"
