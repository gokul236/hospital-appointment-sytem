from django import forms
from .models import PatientDetails

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = PatientDetails
        fields = ['name', 'age', 'gender', 'contact', 'address', 'phone_number', 'password']

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)