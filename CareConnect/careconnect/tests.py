from django.test import TestCase
from .models import PatientDetails, AppointmentDetails, DoctorDetails

class PatientDetailsModelTest(TestCase):
    def setUp(self):
        self.patient = PatientDetails.objects.create(
            name="John Doe",
            age=30,
            gender="Male",
            contact="1234567890",
            address="123 Main St"
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.name, "John Doe")
        self.assertEqual(self.patient.age, 30)
        self.assertEqual(self.patient.gender, "Male")
        self.assertEqual(self.patient.contact, "1234567890")
        self.assertEqual(self.patient.address, "123 Main St")

class DoctorDetailsModelTest(TestCase):
    def setUp(self):
        self.doctor = DoctorDetails.objects.create(
            name="Dr. Smith",
            hospital="City Hospital",
            specialization="Cardiology"
        )

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.name, "Dr. Smith")
        self.assertEqual(self.doctor.hospital, "City Hospital")
        self.assertEqual(self.doctor.specialization, "Cardiology")

class AppointmentDetailsModelTest(TestCase):
    def setUp(self):
        self.patient = PatientDetails.objects.create(
            name="John Doe",
            age=30,
            gender="Male",
            contact="1234567890",
            address="123 Main St"
        )
        self.doctor = DoctorDetails.objects.create(
            name="Dr. Smith",
            hospital="City Hospital",
            specialization="Cardiology"
        )
        self.appointment = AppointmentDetails.objects.create(
            patient_name=self.patient.name,
            doctor_name=self.doctor.name,
            time="10:00 AM",
            date="2023-10-01",
            specialization=self.doctor.specialization
        )

    def test_appointment_creation(self):
        self.assertEqual(self.appointment.patient_name, "John Doe")
        self.assertEqual(self.appointment.doctor_name, "Dr. Smith")
        self.assertEqual(self.appointment.time, "10:00 AM")
        self.assertEqual(self.appointment.date, "2023-10-01")
        self.assertEqual(self.appointment.specialization, "Cardiology")