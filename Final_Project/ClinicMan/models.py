from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers for authentication instead of usernames.
    """
    def create_user(self, email, username, first_name, last_name, password=None):
        if not last_name:
            raise ValueError(_('Users must have a last name'))
        elif not first_name:
            raise ValueError(_('Users must have a first name'))
        elif not username:
            raise ValueError(_('Users must have a username'))
        elif not email:
            raise ValueError(_('Users must provide an email address'))

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        """
        Create and save a SuperUser with the given email and password.
        """

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # basic information
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    # Registration Date
    date_joined = models.DateTimeField(default=timezone.now)  ## todo: unterschied zu 'auto_now_add=True'

    # Permissions
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_recep = models.BooleanField(default=False)
    is_team = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']  # Note: USERNAME_FIELD not to be included in this list!

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_team

class Patient(models.Model):
    GENDER = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other")
        ]
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(choices=GENDER, max_length=1, blank=True)
    born = models.DateTimeField(auto_now=False, auto_now_add=False)
    age = models.IntegerField(default=0, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name
	
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor")
    time = models.TimeField(default="")
    date = models.DateField()
    status = models.BooleanField(default=False)

class Prescription(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_prescription')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_prescription')
    date = models.DateField(auto_now_add=True)
    symptoms = models.CharField(max_length=200)
    prescription = models.CharField(max_length=300)