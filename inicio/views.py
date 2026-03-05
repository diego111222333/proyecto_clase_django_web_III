from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse('Este es el inicio de la pagina😎😎')
def perro(request):
    return HttpResponse("Guau Guau")
def gato(request):
    return HttpResponse("Miau Miau")
