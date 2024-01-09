from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TicketPersonalizado

def saludo(request):
    return render(request,'index.html')

def VistaTicketPersonalizadoLista(request):
    model = TicketPersonalizado
    template_name = 'templates/ticketpersonalizado_lista.html'  
    context_object_name = 'tickets_personalizado'

def VistaTicketPersonalizadoDetalle(request):
    model = TicketPersonalizado
    template_name = 'templates/ticketpersonalizado_detalle.html'  
    context_object_name = 'ticket_lista'

