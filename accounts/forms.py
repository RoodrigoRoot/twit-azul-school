from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile
import datetime


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")


class ProfileForm(forms.ModelForm):
    date_birth = forms.DateField(label='Please select your date birth', initial=datetime.date.today,
                                 widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Profile
        fields = ("biography", "location", "website", "date_birth")
        widgets = {'date_birth': forms.DateInput(attrs={'id': 'datetimepicker12'})}


class LoginForm(forms.Form):

    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

