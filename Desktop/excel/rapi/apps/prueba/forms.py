from django import forms
from .models import TicketPersonalizado

class TicketPersonalizadoForm(forms.ModelForm):
    class Meta:
        model = TicketPersonalizado
        fields = '__all__'  
