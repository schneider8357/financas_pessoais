from django.shortcuts import render, HttpResponse
from django.utils.timezone import now


def pagina_inicial(request):
    return render(request, "index.html", context={"hora_atual": now()})
