from django.shortcuts import render, redirect, get_object_or_404
from .models import PatientDetails, AppointmentDetails, DoctorDetails
from .forms import RegistrationForm, LoginForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            pwd = form.cleaned_data['password']
            try:
                user = PatientDetails.objects.get(phone_number=phone, password=pwd)
                request.session['user_id'] = user.id
                messages.success(request, 'Login successful.')
                return redirect('home')
            except PatientDetails.DoesNotExist:
                messages.error(request, 'Invalid credentials.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully.')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = get_object_or_404(PatientDetails, id=user_id)
    appointments = AppointmentDetails.objects.filter(patient=user)
    return render(request, 'profile.html', {'user': user, 'appointments': appointments})

def appointments(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    doctors = DoctorDetails.objects.all()
    if request.method == 'POST':
        doctor_id = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        specialization = request.POST['specialization']
        doctor = get_object_or_404(DoctorDetails, id=doctor_id)
        patient = get_object_or_404(PatientDetails, id=user_id)
        AppointmentDetails.objects.create(
            patient=patient, doctor=doctor, date=date, time=time, specialization=specialization
        )
        messages.success(request, 'Appointment booked.')
        return redirect('active_appointments')
    return render(request, 'appointments.html', {'doctors': doctors})

def active_appointments(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    patient = get_object_or_404(PatientDetails, id=user_id)
    appointments = AppointmentDetails.objects.filter(patient=patient, status='Pending')
    return render(request, 'active_appointments.html', {'appointments': appointments})

def delete_appointment(request, appointment_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    appointment = get_object_or_404(AppointmentDetails, id=appointment_id, patient_id=user_id)
    appointment.delete()
    messages.success(request, 'Appointment deleted successfully.')
    return redirect('active_appointments')

# --- Admin views (as before) ---
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def admin_users(request):
    users = PatientDetails.objects.all()
    return render(request, 'admin_users.html', {'users': users})

def admin_appointments(request):
    appointments = AppointmentDetails.objects.all()
    return render(request, 'admin_appointments.html', {'appointments': appointments})

def admin_doctors(request):
    doctors = DoctorDetails.objects.all()
    return render(request, 'admin_doctors.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        hospital = request.POST['hospital']
        specialization = request.POST['specialization']
        DoctorDetails.objects.create(name=name, hospital=hospital, specialization=specialization)
        return redirect('admin_doctors')
    return render(request, 'add_doctor.html')

def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(DoctorDetails, id=doctor_id)
    doctor.delete()
    return redirect('admin_doctors')

def confirm_appointment(request, appointment_id):
    appointment = get_object_or_404(AppointmentDetails, id=appointment_id)
    appointment.status = 'Confirmed'
    appointment.save()
    messages.success(request, 'Appointment confirmed.')
    return redirect('admin_appointments')

def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(AppointmentDetails, id=appointment_id)
    appointment.status = 'Cancelled'
    appointment.save()
    messages.success(request, 'Appointment cancelled.')
    return redirect('admin_appointments')