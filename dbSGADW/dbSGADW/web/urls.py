# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('seleccionar_tabla/', views.seleccionar_tabla, name='seleccionar_tabla'),
]
