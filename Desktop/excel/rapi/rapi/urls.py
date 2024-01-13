from django.contrib import admin
from django.urls import path, include
from apps.prueba.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name='inicio'),
    path('prueba/', include('apps.prueba.urls')),
]
