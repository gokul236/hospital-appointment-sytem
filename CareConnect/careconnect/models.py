from django.db import models

class PatientDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)  # Store hashed in production

    def __str__(self):
        return self.name

class DoctorDetails(models.Model):
    name = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AppointmentDetails(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    specialization = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} ({self.date} {self.time})"