from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form


User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    firstname = forms.CharField()
    lastname  = forms.CharField()
    email     = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError("Username is taken")
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError("This email has already been used.")
        
        return email


    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        password2 = data.get("password2")
        if password != password2:
            raise ValidationError("Passwords do not match.")
        return super().clean()

