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
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua Senha'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua Senha novamente'}),
            'birthdate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'},format='%Y-%m-%d' ),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha novamente'})

class UserFormUpdate(forms.ModelForm):
    avatar = forms.ImageField(widget=CustomClearableFileInput, required=False)
    class Meta:
        model = User
        fields = ['name','username', 'email', 'birthdate', 'gender', 'avatar']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'birthdate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'},format='%Y-%m-%d' ),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': '', 
            'email': '',
        }