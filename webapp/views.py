from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib.auth import authenticate, login

from .forms import ContaFormulario


def pagina_inicial(request):
    return render(request, "index.html", context={"hora_atual": now()})

@login_required
def cadastrar_conta(request):
    if request.method == "GET":
        form = ContaFormulario()
        return render(request, "cadastrar_conta.html", context={"form": form})
    elif request.method == "POST":
        form = ContaFormulario(request.POST)
        if form.is_valid():
            form.instance.usuario = request.user
            form.save()
            return HttpResponse("Conta criada com sucesso!", status=200)
        return render(request, "cadastrar_conta.html", context={"form": form})

def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request.GET.get("next", "index"))
    else:
        return HttpResponse("Login ou senha incorretos", status=401)
