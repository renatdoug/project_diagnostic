from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def entrar(request):
    return HttpResponse('Essa pagina esta vindo da views em diagnostics. Aqui será pagina de login')

#def my_csand(request):
#    return HttpResponse('MInha página da Aplicação de apoio clinico para Diagnóstico de Enfermagem')

def my_csand(request):
    return render(request, "diagnostics/my_csand.html")