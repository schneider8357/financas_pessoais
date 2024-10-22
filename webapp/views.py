from django.shortcuts import render, HttpResponse
from django.utils.timezone import now

from .forms import ContaFormulario

def pagina_inicial(request):
    return render(request, "index.html", context={"hora_atual": now()})

def cadastrar_conta(request):
    form = ContaFormulario()
    return render(request, "cadastrar_conta.html", context={"form": form})