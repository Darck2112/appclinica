from django import forms
from django.db.models import fields
from .models import Paciente, Doctor


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente

        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sangre': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hijos': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"

        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numero de cedula'
                }
            ),

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus nombres'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su direccion domiciliaria'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numero de telefono'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'youremail@example.com'
                }
            ),

             'foto': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            ),  

            'consultoria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de consultorio'

                }
            ),
            'lugar': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Direccion del consultorio'
                }
            ),
            'logo': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            ),
            'horario': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Registro Medico'
                }
            ),
            'duracion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Duracion de consultas'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            )                                           
        }