# Introduction

The main objective of the project is to facilitate the listing of consultations of a medical clinic, which uses as a basis the **Emergency Care Units (ECU)** of the **Unified Health System (UHS)**. The main focus was the security of the database, considering a local server with external access, for the creation of a receptionist user, through the superuser. Doctor's require registration as a regular user, with permission received as part of the team. Patients cannot create user accounts, in which case they are registered by the receptionists. With the possibility of expanding various functions in order to expand access to information.

## Distinctiveness:

This project has as main objective to facilitate the listing of consultations of a medical clinic, which uses as a basis the **Emergency Care Units (ECU)** of the **Unified Health System (UHS)**, which makes it distinct from the projects presented in the course CS50 - Web, because it is not an e-commerce,  it is not a social network, it is not an email and it is not a search system.

## Complexity:

- Uses the Python Django structure, incorporating Django forms, models and templates.

- Has 5 models

- Use bootstrap libraries to make the web application responsive.

- Makes use of JavaScript on the front-end, for the editing of consultations and patients.

## What’s contained in each file you created

```
│   db.sqlite3
│   manage.py
│   README.md
│   requirements.txt
│
├───ClinicMan
│   │   admin.py: Allows users to be created, and can modify permissions if necessary, outside the other admin permissions

│   │   apps.py
│   │   forms.py
            - MyDateInput: serves to pick up the date to all form's.

            - UserCreateForm: Form for user creation.

            - AddPatientForm: Form for the registration of patients uses, MyDateInput on the date of birth limiting the date of entry into the registry.

            - CreateAppointmentForm: Form for creating a consultation, picks up users who are registered as a doctor and are part of the team, as well as lists all patients.
│   │   models.py
            - CustomAccountManager: Uses thebase user driver to use the permissions of each user.

            - User:Usesu abstract base suário, plus mixed permission.

            - Patient: Contains the patient information returns the patient's name.

            - Appointment: Contains the information of the consultations receives the medical user and the patient as a foreign key.

            - Prescription: Contains all prescription information receives the medical user and the patient as a foreign key.
│   │   tests.py

│   │   urls.py: Has all access routes to the app as well as to static images.

│   │   views.py:Contains the view functions
            -------ALL

            - index: Where patient consultations are listed by doctor, by order of day and time.

            - login_view: Login into the application.

            - logout_view: Logout of the application.

            - doctorregister: Register a new doctor.

            ------RECEPTIONIST ONLY

            - addpatient: Adds a new patient.

            - patients: Lists registered patients ordered by name.

            - updatepatient: Allows the use of modal to update the patient.

            - createappointment: Creates a consultation between doctors registered as doctors and who are from the team and a registered patient.

            - recepappoedit: Lists all queries by order of day and time.

            - updateappointme: Allows you to update a query using a modal.

            - removeappointme: Allows the exclusion of a medical consultation.

            ------ONLY DOCTORS

            - docappointmentview: Lists all appointments that the logged-in doctor has ordered by day and time.

            - patientview: Shows the patient's name, phone number, age and gender, as well as all the consultations the patient had, along with all prescriptions that were passed through the consultations.

            - modalview: Shows patient prescription for a given medical consultation.

            - docpescrition: Allows the doctor to pass a prescription to the patient.

│   │   __init__.py
│   │
│   ├───migrations
│   │   │   0001_initial.py
│   │   │   0002_alter_prescription_doctor_alter_prescription_patient.py
│   │   │   0003_remove_prescription_appointment.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           0001_initial.cpython-310.pyc
│   │           0002_alter_prescription_doctor_alter_prescription_patient.cpython-310.pyc
│   │           0003_remove_prescription_appointment.cpython-310.pyc
│   │           __init__.cpython-310.pyc
│   │
│   ├───static
│   │   └───ClinicMan
│   │           ECU.png: Brand logo image
│   │           ECUBCG.jpg: Background image
│   │           script.js
                    - DOMContentLoaded: Loads the functions of the buttons for each of the elements

                    - updatelement: uses a click event listener, making it open the modal with data already pre-populated, uses fetch to give an update at the same time the save button is pressed. Here I tried to use ajax instead of fetch, but because it gave a lot of errors, I chose to use fetch.

                    - updatpatielement: function similar to the updatelement, with difference in the time of selecting another doctor for the consultation.

│   │           styles.css: Styles CSS
│   │           styles.scss: Styles SASS
│   │
│   ├───templates
│   │   └───ClinicMan
│   │           addpatient.html: Page to add a new patient
│   │           createappointment.html: Page to create a new consultation
│   │           docappointmentview.html: Page where it shows all the consultations that the medical user has already made
│   │           docpescrition.html: Page for the doctor to write the prescription
│   │           docregister.html: Page for medical user to register
│   │           index.html: Main page
│   │           layout.html: Layout for all pages
│   │           login.html: Web app login page
│   │           modalview.html: Shows the prescription, symptoms and date of a given appointment.
│   │           patients.html: Page for the receptionist to edit the registered patient
│   │           patientview.html: It shows the patient's name, gender, age and phone number, as well as showing all the appointments the patient has had and only show if the
                                    date appointment == date prescription.
│   │           recepappoedit.html: Page for the receptionist to edit or remove the booked appointment
│   │
│   └───__pycache__
│           admin.cpython-310.pyc
│           apps.cpython-310.pyc
│           forms.cpython-310.pyc
│           models.cpython-310.pyc
│           urls.cpython-310.pyc
│           views.cpython-310.pyc
│           __init__.cpython-310.pyc
│
└───Final_Project
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py
    │
    └───__pycache__
            settings.cpython-310.pyc
            urls.cpython-310.pyc
            wsgi.cpython-310.pyc
            __init__.cpython-310.pyc
```

## How to run your application

1. Clone this project or download

2. In your terminal, `cd` into the `ClinicMan` directory.

3. Install all necessary dependencies, `pip install -r requirements.txt`.

4. Make a migration `python manage.py makemigrations ClinicMan` to make migrations for the app.

5. Run `python manage.py migrate` to apply migrations to your database.

6. Create a superuser `python manage.py createsuperuser`.

7. Run `python manage.py runserver`

8. You can create a medical user on the registration page.

9. Enter the administration page and, after entering, give team permission to the doctor, making him part of the staff.

10. In the user table you can create a user, and give receptionist permission to this user.

11. With this it is possible to add new patients, edit the patient's, create appointment, edit appointment or delete them. `While logged in as a receptionist.`

12. When logging in with a doctor's account and having received the `team permission`, it is possible to pass the medical prescription to the patient that the doctor received, as well as it is also possible to see all the patient's appointments in which he is attending. If you have not received any permissions, you will only be able to see the logout.

## References:

Django documentation for user creation: [here](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)

Stackoveflow for modalview and other's research: [here](https://stackoverflow.com/questions/45306970/passing-data-to-bootstrap-modal-django-template)