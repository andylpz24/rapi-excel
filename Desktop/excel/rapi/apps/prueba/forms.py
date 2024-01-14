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

class AbrirPromoEscolarForm(forms.ModelForm):
    class Meta:
        model = AbrirPromoEscolar
        fields = '__all__'  

class RegistrarPagoNaranjaForm(forms.ModelForm):
    class Meta:
        model = RegistartPagoNaranja
        fields = '__all__'  

class BuscarPagoForm(forms.Form):
    nombre_titular = forms.CharField(label='Nombre Titular', max_length=250, required=False)