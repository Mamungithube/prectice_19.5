from django import forms
from .models import Album
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Albumform(forms.ModelForm):
    class Meta: 
        model = Album
        fields = '__all__'

        widgets = {
            'Rating': forms.Select(choices=[(i,i) for i in range(1,6)]),
            'Album_release_date': forms.NumberInput(attrs={'type':'date'}),
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']