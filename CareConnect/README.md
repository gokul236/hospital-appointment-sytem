# CareConnect Hospital Appointment System

## Overview
CareConnect is a Django-based web application designed to facilitate hospital appointment management. It allows patients to register, log in, and manage their appointments with doctors. The application also provides an admin interface for managing users, appointments, and doctor details.

## Features
- User registration and login using phone number and password.
- Patient management with personal details and appointment history.
- Appointment scheduling with available doctors based on specialization.
- Admin dashboard for managing users, appointments, and doctors.
- Active appointment management with options to confirm or cancel.

## Models
1. **PatientDetails**
   - Fields: name, age, gender, contact, address.
   
2. **AppointmentDetails**
   - Fields: patient name, doctor name, time, date, specialization.
   
3. **DoctorDetails**
   - Fields: name, hospital, specialization.

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd CareConnect
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Use the login page to access your account or register as a new user.
- Navigate through the home page to manage appointments and view your profile.
- Admins can log in to manage users and appointments through the admin dashboard.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.