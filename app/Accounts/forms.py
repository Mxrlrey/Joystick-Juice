from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'widgets/custom_clearable_file_input.html' # Texto do botão para escolher arquivo

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username', 'email', "password1", "password2", 'birthdate', 'gender', 'avatar']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(),
        }

class UserFormUpdate(forms.ModelForm):
    avatar = forms.ImageField(widget=CustomClearableFileInput, required=False)
    class Meta:
        model = User
        fields = ['name','username', 'email', 'birthdate', 'gender', 'avatar']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(),
        }