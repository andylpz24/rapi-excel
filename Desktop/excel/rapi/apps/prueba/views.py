from django.shortcuts import render, redirect
from .forms import TicketPersonalizadoForm, TicketSameepForm, AbrirPromoEscolarForm, RegistrarPagoNaranjaForm,BuscarPagoForm
from django.templatetags.static import static
from .models import RegistartPagoNaranja

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

def buscar_pago_naranja(request):
    registros = RegistartPagoNaranja.objects.all()

    # Procesar el formulario si se envió
    if request.method == 'POST':
        form = BuscarPagoForm(request.POST)
        if form.is_valid():
            nombre_titular = form.cleaned_data.get('nombre_titular')
            
            # Filtrar los registros por nombre si se proporciona
            if nombre_titular:
                registros = registros.filter(Nombre_Titular__icontains=nombre_titular)
    else:
        form = BuscarPagoForm()

    return render(request, 'buscar_pago_naranja.html', {'registros': registros, 'form': form})