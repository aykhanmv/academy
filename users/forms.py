from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
User._meta.get_field('email')._unique = True

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label='Ad')
    last_name = forms.CharField(max_length=50, label='Soyad')
    username = forms.CharField(label='İstifadəçi adı')
    email = forms.CharField(label='E-poçt')
    password1 = forms.CharField(label='Şifrə', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Təkrar şifrə', widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'İstifadəçi adı və ya şifrəsi yalnışdır!'
        super().__init__(*args, **kwargs)
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
