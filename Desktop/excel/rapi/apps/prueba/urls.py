from django.urls import path
from . import views
from .views import ticket_personalizado
urlpatterns = [
    path('ticket_naranja/', views.ticket_naranja, name='ticket_naranja'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('ticket_servicekairos/', views.ticket_servicekairos, name='ticket_servicekairos'),
    path('registrar_adicional/', views.registrar_adicional, name='registrar_adicional'),
    path('abrir_promo_escolar/', views.abrir_promo_escolar, name='abrir_promo_escolar'),
    path('ticket_personalizado/', views.ticket_personalizado, name='ticket_personalizado'),
    path('ticket_sameep/', views.ticket_sameep, name='ticket_sameep'),
    path('ticket_personalizado/', ticket_personalizado, name='ticket_personalizado'),
]
