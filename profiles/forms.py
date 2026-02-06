from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    fname = forms.CharField(max_length=30, label='First Name')
    lname = forms.CharField(max_length=30, label='Last Name')
    tech = forms.CharField(max_length=100, label='Technology')
    email = forms.EmailField(label='Email Address')
    photo = forms.ImageField(label='Profile Photo')
    doc = forms.FileField(label='Upload Document')
    class Meta:
        model = profiles
        fields = '__all__'

class SearchForm(forms.Form):
    profile_id = forms.IntegerField(label='Profile ID')