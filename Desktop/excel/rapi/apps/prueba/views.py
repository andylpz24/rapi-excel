from django.shortcuts import render, redirect
from .forms import TicketPersonalizadoForm, TicketSameepForm, AbrirPromoEscolarForm, RegistrarPagoNaranjaForm
from django.http import HttpResponse
import os
from django.templatetags.static import static

def inicio(request):
    return render(request,'index.html')

def navegacion_naranja(request):
    return render(request, 'navegacion_naranja.html')

def configuracion(request):
    return render(request, 'configuracion.html')

def ticket_servicekairos(request):
    return render(request, 'ticket_servicekairos.html')

def registrar_adicional(request):
    return render(request, 'registrar_adicional.html')

def abrir_promo_escolar(request):
    if request.method == 'POST':
        form = AbrirPromoEscolarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_sameep')
    else:
        form = AbrirPromoEscolarForm()
    
    return render(request, 'abrir_promo_escolar.html', {'form': form})

def ticket_personalizado(request):
    if request.method == 'POST':
        form = TicketPersonalizadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_personalizado')
    else:
        form = TicketPersonalizadoForm()
    
    return render(request, 'ticket_personalizado.html', {'form': form})

def ticket_sameep(request):
    if request.method == 'POST':
        form = TicketSameepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_sameep')
    else:
        form = TicketPersonalizadoForm()
    
    return render(request, 'ticket_sameep.html', {'form': form})

def registrar_pago_naranja(request):
    if request.method == 'POST':
        form = RegistrarPagoNaranjaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_pago_naranja')
    else:
        form = RegistrarPagoNaranjaForm()
    
    return render(request, 'registrar_pago_naranja.html', {'form': form})