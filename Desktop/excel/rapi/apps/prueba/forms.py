from django import forms
from .models import TicketPersonalizado, TicketSameep, AbrirPromoEscolar, RegistartPagoNaranja

class TicketPersonalizadoForm(forms.ModelForm):
    class Meta:
        model = TicketPersonalizado
        fields = '__all__'  

class TicketSameepForm(forms.ModelForm):
    class Meta:
        model = TicketSameep
        fields = '__all__'  