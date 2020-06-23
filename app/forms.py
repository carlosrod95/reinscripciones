"""
Definition of forms.
"""


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from app.models import Profile
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30,label="Nombre Usuario:  ",required=True)
    apepaterno = forms.CharField(max_length=30,label="Apellido Paterno:  ",required=True)
    apematerno = forms.CharField(max_length=30,label="Apellido Materno:  ")
    curp = forms.CharField(max_length=18,label="CURP 18 DIGITOS:  ",required=True)
    tutor = forms.CharField(max_length=40,label="Nombre Tutor:  ",required=True)
    #grado = forms.IntegerField(required=True) 
    grupo = forms.CharField(max_length=1,required=True)
    fechanacimiento = forms.DateField(input_formats=['%Y-%m-%d'])
    class Meta:
        model = Profile
        fields = ( 'apepaterno', 'apematerno','nombre','grado','grupo','curp','tutor','escuela_type','fechanacimiento')




class CreaProfileFORM(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'apepaterno', 'apematerno','nombre','grado','grupo','curp','tutor')




class SignUpForm(UserCreationForm):
    email= forms.EmailField(max_length=254, label='Correo Electronico',help_text='Valor Necesario para continuar.',required=True)
    username= forms.CharField(max_length=100, label='Usuario',help_text='Nombre unico con el que te identificaras en la pagina',required=True)
    password1= forms.CharField(min_length=8,label='Contraseña',required=True,help_text='<br> Su contraseña no puede ser muy similar a su otra información personal. <br> Su contraseña debe contener al menos 8 caracteres. <br> Su contraseña no puede ser una contraseña de uso común. <br>  Su contraseña no puede ser enteramente numérica.')
    password2= forms.CharField(min_length=8,label='Confirma Contraseña',required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
