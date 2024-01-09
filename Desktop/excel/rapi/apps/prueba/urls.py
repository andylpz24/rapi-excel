# En prueba/urls.py
from django.urls import path
from .views import VistaTicketPersonalizadoLista, VistaTicketPersonalizadoDetalle
from . import views

app_name = 'apps.prueba'

urlpatterns = [
    path('tickets/',views.VistaTicketPersonalizadoDetalle , name='tickets_personalizado'),
    path('ticket/<int:pk>/', views.VistaTicketPersonalizadoLista, name='ticket_lista'),
]
