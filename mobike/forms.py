from django import forms
from .models import Cliente
from django.contrib.auth.models import User


class formularioCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['RUT','NOMBRE_COMPLETO','EDAD','MEDIO_PAGO','NUMERO_CELULAR','EMAIL']
