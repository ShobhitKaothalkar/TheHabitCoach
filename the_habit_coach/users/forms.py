from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "dob", "gender")
        widgets = {
            'dob': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

