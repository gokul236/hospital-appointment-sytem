from django.contrib import admin
from .models import PatientDetails, AppointmentDetails, DoctorDetails

class PatientDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'contact', 'address', 'phone_number')
    search_fields = ('name', 'contact', 'phone_number')

class AppointmentDetailsAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'specialization', 'status')
    search_fields = ('patient__name', 'doctor__name', 'specialization')

class DoctorDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital', 'specialization')
    search_fields = ('name', 'hospital', 'specialization')

admin.site.register(PatientDetails, PatientDetailsAdmin)
admin.site.register(AppointmentDetails, AppointmentDetailsAdmin)
admin.site.register(DoctorDetails, DoctorDetailsAdmin)