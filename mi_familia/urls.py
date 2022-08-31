from django.urls import path
from mi_familia.views import listar_familia

urlpatterns = [
    path('', listar_familia)
]