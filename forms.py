from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nombre_de_la_empresa = forms.CharField(required=False, max_length=100)
    años_en_el_mercado = forms.CharField(required=False, max_length=100)
    actividad_económica = forms.CharField(required=False, max_length=100)
    teléfono = forms.CharField(required=False, max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'nombre_de_la_empresa', 'años_en_el_mercado', 'actividad_económica', 'teléfono']