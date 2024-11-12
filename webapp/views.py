from django.shortcuts import render, HttpResponse
from django.utils.timezone import now

from .forms import ContaFormulario

def pagina_inicial(request):
    return render(request, "index.html", context={"hora_atual": now()})

def cadastrar_conta(request):
    if request.method == "GET":
        form = ContaFormulario()
        return render(request, "cadastrar_conta.html", context={"form": form})
    elif request.method == "POST":
        form = ContaFormulario(request.POST)
        if form.is_valid():
            form.usuario = request.user
            form.save()
            return HttpResponse("Conta criada com sucesso!", status=200)
        return render(request, "cadastrar_conta.html", context={"form": form})
