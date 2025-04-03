from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'tipo_identificacion',
            'numero_identificacion',
            'nombre_completo',
            'correo_electronico',
            'telefono_movil',
            'tipo',
            'validacion',
        ]
        widgets = {
            'tipo_identificacion': forms.Select(attrs={'class': 'form-control'}),
            'numero_identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono_movil': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'validacion': forms.Select(attrs={'class': 'form-control'}),
        }