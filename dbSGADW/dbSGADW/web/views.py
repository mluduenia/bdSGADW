# views.py
from django.shortcuts import render
from django.db import connection
from .forms import TablaSeleccionForm
from .utils import extraer_numero_de_tabla

def seleccionar_tabla(request):
    form = TablaSeleccionForm()
    datos = None
    columnas = []
    numero_tabla = None

    if request.method == 'POST':
        form = TablaSeleccionForm(request.POST)
        if form.is_valid():
            tabla_seleccionada = form.cleaned_data['tabla']
            numero_tabla = extraer_numero_de_tabla(tabla_seleccionada)
            fecha_seleccionada = form.cleaned_data['fecha']

            with connection.cursor() as cursor:
                if fecha_seleccionada:
                    cursor.execute(f"SELECT * FROM {tabla_seleccionada} WHERE DATE(T_TIME) = %s", [fecha_seleccionada])
                else:
                    cursor.execute(f"SELECT * FROM {tabla_seleccionada}")
                columnas = [col[0] for col in cursor.description]
                datos = cursor.fetchall()

    return render(request, 'web/mostrar_datos.html', {'form': form, 'datos': datos, 'columnas': columnas, 'numero_tabla': numero_tabla})
