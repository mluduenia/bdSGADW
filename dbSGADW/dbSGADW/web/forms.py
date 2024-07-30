# forms.py
from django import forms
from .utils import obtener_tablas, extraer_numero_de_tabla

class TablaSeleccionForm(forms.Form):
    tabla = forms.ChoiceField(choices=[])
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tabla'].choices = [(tabla, extraer_numero_de_tabla(tabla)) for tabla in obtener_tablas()]
