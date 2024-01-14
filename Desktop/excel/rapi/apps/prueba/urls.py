from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('navegacion_naranja/registrar_pago_naranja/', views.registrar_pago_naranja, name='registrar_pago_naranja'),
    path('navegacion_naranja/buscar_pago_naranja/', views.buscar_pago_naranja, name='buscar_pago_naranja'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('ticket_servicekairos/', views.ticket_servicekairos, name='ticket_servicekairos'),
    path('registrar_adicional/', views.registrar_adicional, name='registrar_adicional'),
    path('abrir_promo_escolar/', views.abrir_promo_escolar, name='abrir_promo_escolar'),
    path('ticket_personalizado/', views.ticket_personalizado, name='ticket_personalizado'),
    path('ticket_sameep/', views.ticket_sameep, name='ticket_sameep'),
    path('navegacion_naranja/', views.navegacion_naranja, name='navegacion_naranja'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
