from django import forms
from .models import User


class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'widgets/custom_clearable_file_input.html' # Texto do botão para escolher arquivo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'birthdate', 'gender', 'password', 'nickname', 'avatar']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(),
        }

class UserFormUpdate(forms.ModelForm):
    avatar = forms.ImageField(widget=CustomClearableFileInput, required=False)
    class Meta:
        model = User
        fields = ['name', 'email', 'birthdate', 'gender', 'nickname', 'avatar']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(),
        }