from django import forms
from .models import Conta


class DateInput(forms.DateInput):
    input_type = 'date'


class ContaFormulario(forms.ModelForm):
    data_vencimento = forms.DateField(widget=DateInput())
    data_compra = forms.DateField(widget=DateInput())
    class Meta:
        model = Conta
        exclude = ["usuario"]
