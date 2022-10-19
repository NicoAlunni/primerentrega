from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppGuitarras.models import Avatar


class FenderFormulario(forms.Form):

    fenderguitarra = forms.CharField()
    serie = forms.IntegerField()


class GibsonFormulario(forms.Form):

    gibsonguitarra = forms.CharField()
    serie = forms.IntegerField()


class IbanezFormulario(forms.Form):

    ibanezguitarra = forms.CharField()
    serie = forms.IntegerField()


class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["usurname", "email", "first name", "last name", "password1", "password2"]


class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first name", "last name", "password1", "password2"]


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen"]

