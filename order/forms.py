from django.forms import ModelForm
from django import forms
from order.models import Publicadore,Libro,Autore


class ContactoForm(forms.Form):
  correo = forms.EmailField(label='Ingrese su correo electronico')
  mensaje = forms.CharField(widget=forms.Textarea)
